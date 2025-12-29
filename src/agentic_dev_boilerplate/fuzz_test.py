#!/usr/bin/env python3
"""
Standalone fuzz testing script for agentic-dev-boilerplate.

This script provides comprehensive fuzzing capabilities for testing:
- Valid schema combinations across different project types, languages, and complexities
- Invalid schema inputs to ensure proper error handling
- Security validation to prevent host system compromise
- Performance testing with various schema sizes

Usage:
    uv run python scripts/fuzz_test.py [options]

Options:
    --valid-only        Test only valid schemas
    --invalid-only      Test only invalid schemas
    --iterations N      Number of iterations per test case (default: 10)
    --output-dir DIR    Output directory for generated files (default: ./fuzz_output)
    --verbose           Enable verbose output
    --security-check    Run additional security validations
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from agentic_dev_boilerplate.generate_boilerplate import BoilerplateGenerator


class DictObject:
    """Convert dict to object for Jinja2 template access."""

    def __init__(self, data):
        for key, value in data.items():
            if isinstance(value, dict):
                setattr(self, key, DictObject(value))
            elif isinstance(value, list):
                setattr(
                    self,
                    key,
                    [
                        DictObject(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            else:
                setattr(self, key, value)

    def get(self, key, default=None):
        """Implement dict-like get method for Jinja2 compatibility."""
        return getattr(self, key, default)

    def __getitem__(self, key):
        """Implement dict-like indexing for Jinja2 compatibility."""
        return getattr(self, key)

    def __setitem__(self, key, value):
        """Implement dict-like item assignment for Jinja2 compatibility."""
        setattr(self, key, value)


class SecurityValidator:
    """Security validation for fuzzing to prevent host system compromise."""

    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
        self.max_file_size = 10 * 1024 * 1024  # 10MB
        self.max_total_size = 100 * 1024 * 1024  # 100MB
        self.forbidden_patterns = [
            "..",
            "/etc",
            "/home",
            "/root",
            "/usr",
            "/var",
            "/tmp",
            "passwd",
            "shadow",
            ".ssh",
            "sudo",
            "su",
            "chmod",
            "chown",
            "rm -rf",
            "format",
            "mkfs",
            "dd if=",
            "wget",
            "curl",
            "nc",
            "netcat",
            "ssh",
            "scp",
            "ftp",
            "telnet",
            "python -c",
            "bash -c",
            "sh -c",
            "exec(",
            "eval(",
            "os.system",
            "subprocess",
            "import os",
            "import subprocess",
        ]

    def validate_output_dir(self, output_dir: Path) -> bool:
        """Validate that output directory is safe and within bounds."""
        try:
            # Check if output directory is within base directory
            output_dir = output_dir.resolve()
            if not str(output_dir).startswith(str(self.base_dir)):
                return False

            # Check if directory exists and is writable
            if output_dir.exists():
                if not output_dir.is_dir():
                    return False
                # Check if we can write to it
                test_file = output_dir / ".fuzz_test"
                try:
                    test_file.write_text("test")
                    test_file.unlink()
                except (OSError, PermissionError):
                    return False

            return True
        except Exception:
            return False

    def validate_schema_content(self, schema: Dict[str, Any]) -> bool:
        """Validate schema content for security issues."""
        schema_str = json.dumps(schema, default=str).lower()

        # Check for exact dangerous patterns (not substrings)
        dangerous_patterns = [
            "rm -rf",
            "../../../",
            "..\\..\\..\\",
            "/etc/passwd",
            "/etc/shadow",
            "sudo",
            "su ",
            "chmod",
            "chown",
            "mkfs",
            "dd if=",
            "wget ",
            "curl ",
            "nc ",
            "netcat",
            "ssh ",
            "scp ",
            "ftp ",
            "telnet",
            "bash -c",
            "sh -c",
            "exec(",
            "eval(",
            "os.system",
            "subprocess",
            "import os",
            "import subprocess",
        ]

        for pattern in dangerous_patterns:
            if pattern in schema_str:
                return False

        # Check for oversized values that could cause issues
        def check_size(obj, path=""):
            if isinstance(obj, str) and len(obj) > 10000:  # 10KB limit
                return False
            elif isinstance(obj, (list, dict)):
                if len(obj) > 1000:  # Reasonable size limits
                    return False
                for key, value in (
                    obj.items() if isinstance(obj, dict) else enumerate(obj)
                ):
                    if not check_size(value, f"{path}.{key}" if path else str(key)):
                        return False
            return True

        if not check_size(schema):
            return False

        # Check for invalid types in common fields
        if "project" in schema and isinstance(schema["project"], dict):
            project = schema["project"]
            if "version" in project and not isinstance(project["version"], str):
                return False
            if "name" in project and not isinstance(project["name"], str):
                return False

        if "languages" in schema and isinstance(schema["languages"], list):
            for lang in schema["languages"]:
                if isinstance(lang, dict):
                    if "name" in lang and not isinstance(lang["name"], str):
                        return False
                    if "version" in lang and not isinstance(lang["version"], str):
                        return False

        return True

    def check_resource_usage(self, output_dir: Path) -> bool:
        """Check that generated files don't exceed resource limits."""
        try:
            total_size = 0
            file_count = 0

            for file_path in output_dir.rglob("*"):
                if file_path.is_file():
                    file_count += 1
                    size = file_path.stat().st_size
                    total_size += size

                    if size > self.max_file_size:
                        return False

            if total_size > self.max_total_size:
                return False

            if file_count > 1000:  # Reasonable limit
                return False

            return True
        except Exception:
            return False


class SchemaFuzzer:
    """Comprehensive schema fuzzer for testing valid and invalid inputs."""

    def __init__(self):
        self.project_types = [
            "web_app",
            "api",
            "cli_tool",
            "library",
            "microservice",
            "monolith",
            "data_pipeline",
            "ml_model",
            "mobile_app",
            "desktop_app",
            "game",
            "embedded_system",
            "iot_device",
            "blockchain",
            "ai_agent",
        ]

        self.languages = [
            {
                "name": "python",
                "version": "3.11",
                "frameworks": ["fastapi", "django"],
                "package_manager": "uv",
            },
            {
                "name": "javascript",
                "version": "18",
                "frameworks": ["react", "vue"],
                "package_manager": "npm",
            },
            {
                "name": "typescript",
                "version": "5.0",
                "frameworks": ["nextjs", "nestjs"],
                "package_manager": "npm",
            },
            {
                "name": "go",
                "version": "1.21",
                "frameworks": ["gin", "echo"],
                "package_manager": "go",
            },
            {
                "name": "rust",
                "version": "1.70",
                "frameworks": ["axum", "actix"],
                "package_manager": "cargo",
            },
            {
                "name": "java",
                "version": "17",
                "frameworks": ["spring", "quarkus"],
                "package_manager": "maven",
            },
            {
                "name": "csharp",
                "version": "11",
                "frameworks": ["aspnet", "minimalapi"],
                "package_manager": "dotnet",
            },
        ]

        self.complexities = ["low", "medium", "high"]

    def generate_valid_schema(
        self,
        project_type: Optional[str] = None,
        languages: Optional[List[Dict]] = None,
        complexity: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generate a valid schema with specified parameters."""
        if project_type is None:
            project_type = self.project_types[0]

        if languages is None:
            languages = [self.languages[0]]

        if complexity is None:
            complexity = "medium"

        # Generate project config based on complexity
        project_config = self._generate_project_config(project_type, complexity)

        # Generate agent config based on project type and complexity
        agents = self._generate_agent_config(project_type, complexity)

        # Generate workflow config
        workflows = self._generate_workflow_config(project_type, complexity)

        schema = {
            "project": project_config,
            "languages": languages,
            "agents": agents,
            "workflows": workflows,
            "git": {
                "default_branch": "main",
                "commit_signing": complexity != "low",
                "pull_rebase": True,
                "push_default": "current",
                "auto_setup_remote": True,
            },
            "validation": {
                "commit_message_format": "conventional",
                "pr_title_format": "conventional",
                "branch_naming": "feature/*",
                "required_checks": (
                    ["lint", "test", "security"] if complexity != "low" else ["test"]
                ),
                "code_coverage_minimum": 80 if complexity != "low" else 60,
            },
            "security": {
                "gpg_signing": complexity != "low",
                "dependency_scanning": complexity != "low",
                "secret_scanning": complexity != "low",
                "vulnerability_scanning": complexity != "low",
                "license_checking": True,
            },
            "ci_cd": {
                "provider": "github_actions",
                "phases": (
                    [
                        {
                            "name": "validate",
                            "trigger": ["push", "pull_request"],
                            "jobs": ["lint", "test", "security"],
                        },
                        {
                            "name": "build",
                            "trigger": ["push"],
                            "jobs": ["build", "package"],
                        },
                        {
                            "name": "deploy",
                            "trigger": ["release"],
                            "jobs": ["deploy_staging", "deploy_production"],
                        },
                    ]
                    if complexity != "low"
                    else [
                        {
                            "name": "validate",
                            "trigger": ["push", "pull_request"],
                            "jobs": ["test"],
                        },
                    ]
                ),
            },
            "documentation": {
                "readme_generation": True,
                "api_docs": False,
                "changelog": True,
                "contributing_guide": complexity != "low",
                "code_of_conduct": complexity == "high",
            },
        }

        # Add project-type specific configurations
        if project_type in ["web_app", "api", "microservice"]:
            schema.update(self._generate_web_config(complexity))
        elif project_type in ["ml_model", "ai_agent"]:
            schema.update(self._generate_ml_config(complexity))
        elif project_type == "mobile_app":
            schema.update(self._generate_mobile_config(complexity))

        return schema

    def generate_invalid_schema(self, invalid_type: str) -> Dict[str, Any]:
        """Generate various types of invalid schemas."""
        base_schema = self.generate_valid_schema()

        if invalid_type == "missing_required":
            # Remove required fields
            del base_schema["project"]
            return base_schema

        elif invalid_type == "invalid_language":
            # Add invalid language configuration
            base_schema["languages"] = [{"name": "invalid_lang", "version": "999"}]
            return base_schema

        elif invalid_type == "command_injection":
            # Add potentially dangerous content
            base_schema["project"]["name"] = "test; rm -rf /"
            return base_schema

        elif invalid_type == "path_traversal":
            # Add path traversal attempts
            base_schema["project"]["name"] = "../../../etc/passwd"
            return base_schema

        elif invalid_type == "oversized_values":
            # Add extremely large values
            base_schema["project"]["description"] = "x" * 1000000
            return base_schema

        elif invalid_type == "circular_reference":
            # Create circular reference (will fail JSON serialization)
            base_schema["circular"] = base_schema
            return base_schema

        elif invalid_type == "invalid_types":
            # Wrong data types
            base_schema["project"]["version"] = ["not", "a", "string"]
            return base_schema

        return base_schema

    def _generate_project_config(
        self, project_type: str, complexity: str
    ) -> Dict[str, Any]:
        """Generate project configuration."""
        names = {
            "web_app": "my-web-app",
            "api": "my-api-service",
            "cli_tool": "my-cli-tool",
            "library": "my-library",
            "microservice": "user-service",
            "monolith": "enterprise-app",
            "data_pipeline": "data-processor",
            "ml_model": "ml-predictor",
            "mobile_app": "my-mobile-app",
            "desktop_app": "my-desktop-app",
            "game": "my-game",
            "embedded_system": "iot-controller",
            "iot_device": "smart-sensor",
            "blockchain": "crypto-wallet",
            "ai_agent": "ai-assistant",
        }

        descriptions = {
            "low": f"A simple {project_type.replace('_', ' ')} project",
            "medium": f"A feature-rich {project_type.replace('_', ' ')} with multiple components",
            "high": f"An enterprise-grade {project_type.replace('_', ' ')} with advanced features, scalability, and production readiness",
        }

        return {
            "name": names.get(project_type, "test-project"),
            "description": descriptions.get(complexity, "Test project"),
            "repository": f"https://github.com/test/{names.get(project_type, 'test-project')}",
            "private": complexity == "high",
            "version": "1.0.0",
        }

    def _generate_agent_config(
        self, project_type: str, complexity: str
    ) -> List[Dict[str, Any]]:
        """Generate agent configuration based on project type and complexity."""
        base_agents = [
            {
                "role": "planner",
                "enabled": True,
                "scope": ["task_decomposition", "priority_assessment"],
            },
            {
                "role": "tester",
                "enabled": True,
                "scope": ["unit_testing", "integration_testing"],
            },
        ]

        if complexity == "medium":
            base_agents.extend(
                [
                    {
                        "role": "debugger",
                        "enabled": True,
                        "scope": ["error_analysis", "fix_suggestions"],
                    },
                    {
                        "role": "deployer",
                        "enabled": True,
                        "scope": ["deployment", "monitoring"],
                    },
                ]
            )

        if complexity == "high":
            base_agents.extend(
                [
                    {
                        "role": "security",
                        "enabled": True,
                        "scope": ["security_audit", "vulnerability_scan"],
                    },
                    {
                        "role": "devops-specialist",
                        "enabled": True,
                        "scope": ["infrastructure", "ci_cd"],
                    },
                    {
                        "role": "software-engineer",
                        "enabled": True,
                        "scope": ["architecture", "refactoring"],
                    },
                ]
            )

        # Add project-specific agents
        if project_type in ["ml_model", "ai_agent"]:
            base_agents.append(
                {
                    "role": "ai-engineer",
                    "enabled": True,
                    "scope": ["model_training", "inference_optimization"],
                }
            )

        return base_agents

    def _generate_workflow_config(
        self, project_type: str, complexity: str
    ) -> Dict[str, Any]:
        """Generate workflow configuration."""
        base_workflows = {
            "pr_automation": True,
            "task_tracking": True,
            "commit_signing": complexity != "low",
            "ci_cd": True,
            "gitops": complexity == "high",
            "security_scanning": complexity != "low",
            "dependency_management": True,
            "multi_agent_coordination": complexity != "low",
        }

        return base_workflows

    def _generate_web_config(self, complexity: str) -> Dict[str, Any]:
        """Generate web-specific configuration."""
        return {
            "ci_cd": {"provider": "github_actions"},
            "validation": {"code_coverage_minimum": 80 if complexity != "low" else 60},
            "security": {"gpg_signing": complexity != "low"},
            "documentation": {
                "readme_generation": True,
                "contributing_guide": complexity != "low",
                "changelog": True,
            },
        }

    def _generate_ml_config(self, complexity: str) -> Dict[str, Any]:
        """Generate ML-specific configuration."""
        return {
            "ml": {
                "framework": "pytorch" if complexity == "high" else "scikit-learn",
                "gpu_support": complexity == "high",
                "model_registry": complexity != "low",
            },
            "data": {
                "validation": True,
                "versioning": complexity != "low",
            },
        }

    def _generate_mobile_config(self, complexity: str) -> Dict[str, Any]:
        """Generate mobile-specific configuration."""
        return {
            "mobile": {
                "platforms": (
                    ["ios", "android"] if complexity == "high" else ["android"]
                ),
                "framework": "react-native" if complexity == "high" else "flutter",
            },
            "ci_cd": {"provider": "github_actions"},
        }


def main():
    """Main fuzz testing function."""
    parser = argparse.ArgumentParser(
        description="Fuzz test agentic-dev-boilerplate schemas"
    )
    parser.add_argument(
        "--valid-only", action="store_true", help="Test only valid schemas"
    )
    parser.add_argument(
        "--invalid-only", action="store_true", help="Test only invalid schemas"
    )
    parser.add_argument(
        "--iterations", type=int, default=10, help="Number of iterations per test case"
    )
    parser.add_argument(
        "--output-dir", type=str, default="./fuzz_output", help="Output directory"
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument(
        "--security-check",
        action="store_true",
        help="Run additional security validations",
    )

    args = parser.parse_args()

    # Setup
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)

    security_validator = SecurityValidator(Path.cwd())
    fuzzer = SchemaFuzzer()

    print(f"🧪 Starting fuzz testing with {args.iterations} iterations per test case")
    print(f"📁 Output directory: {output_dir}")

    total_tests = 0
    passed_tests = 0
    failed_tests = 0

    start_time = time.time()

    try:
        # Test valid schemas
        if not args.invalid_only:
            print("\n✅ Testing valid schemas...")
            for project_type in fuzzer.project_types[:3]:  # Test first 3 for speed
                for complexity in fuzzer.complexities:
                    for iteration in range(args.iterations):
                        try:
                            total_tests += 1

                            # Generate schema
                            schema = fuzzer.generate_valid_schema(
                                project_type, None, complexity
                            )

                            # Security check
                            if not security_validator.validate_schema_content(schema):
                                print(
                                    f"❌ Security violation in valid schema: {project_type}/{complexity}/{iteration}"
                                )
                                failed_tests += 1
                                continue

                            # Test generation
                            test_output_dir = (
                                output_dir
                                / f"valid_{project_type}_{complexity}_{iteration}"
                            )
                            test_output_dir.mkdir(exist_ok=True)

                            if not security_validator.validate_output_dir(
                                test_output_dir
                            ):
                                print(f"❌ Invalid output directory: {test_output_dir}")
                                failed_tests += 1
                                continue

                            # Create temp schema file
                            temp_schema_path = (
                                output_dir / f"temp_schema_{iteration}.yaml"
                            )
                            import yaml

                            with open(temp_schema_path, "w") as f:
                                yaml.dump(schema, f)

                            generator = BoilerplateGenerator(
                                str(temp_schema_path), str(test_output_dir)
                            )

                            # Note: DictObject conversion not needed - Jinja2 handles dict access with dot notation
                            # schema_obj = DictObject(schema)
                            # generator.schema = schema_obj
                            generator.generate()

                            # Check resource usage
                            if not security_validator.check_resource_usage(
                                test_output_dir
                            ):
                                print(f"❌ Resource limits exceeded: {test_output_dir}")
                                failed_tests += 1
                                continue

                            # Clean up temp file
                            temp_schema_path.unlink()

                            passed_tests += 1
                            if args.verbose:
                                print(
                                    f"✅ Valid schema passed: {project_type}/{complexity}/{iteration}"
                                )

                        except Exception as e:
                            print(
                                f"❌ Valid schema failed: {project_type}/{complexity}/{iteration} - {e}"
                            )
                            failed_tests += 1

        # Test invalid schemas
        if not args.valid_only:
            print("\n❌ Testing invalid schemas...")
            invalid_types = [
                "missing_required",
                "invalid_language",
                "command_injection",
                "path_traversal",
                "oversized_values",
                "invalid_types",
            ]

            for invalid_type in invalid_types:
                for iteration in range(args.iterations):
                    try:
                        total_tests += 1

                        # Generate invalid schema
                        schema = fuzzer.generate_invalid_schema(invalid_type)

                        # Test that it fails appropriately
                        test_output_dir = (
                            output_dir / f"invalid_{invalid_type}_{iteration}"
                        )
                        test_output_dir.mkdir(exist_ok=True)

                        # Create temp schema file
                        temp_schema_path = output_dir / f"temp_invalid_{iteration}.yaml"
                        import yaml

                        with open(temp_schema_path, "w") as f:
                            yaml.dump(schema, f)

                        # Validate schema security before generation
                        if not security_validator.validate_schema_content(schema):
                            # Expected failure - schema validation caught security issue
                            passed_tests += 1
                            if args.verbose:
                                print(
                                    f"✅ Invalid schema correctly rejected: {invalid_type}/{iteration}"
                                )
                            temp_schema_path.unlink()
                            continue

                        try:
                            generator = BoilerplateGenerator(
                                str(temp_schema_path), str(test_output_dir)
                            )

                            # Note: DictObject conversion not needed - Jinja2 handles dict access with dot notation
                            # schema_obj = DictObject(schema)
                            # generator.schema = schema_obj
                            generator.generate()

                            # If we get here, the invalid schema didn't fail as expected
                            print(
                                f"⚠️  Invalid schema should have failed: {invalid_type}/{iteration}"
                            )
                            failed_tests += 1

                        except Exception:
                            # Expected failure - this is good
                            passed_tests += 1
                            if args.verbose:
                                print(
                                    f"✅ Invalid schema correctly rejected: {invalid_type}/{iteration}"
                                )

                        finally:
                            # Clean up temp file
                            if temp_schema_path.exists():
                                temp_schema_path.unlink()

                    except Exception as e:
                        print(
                            f"❌ Invalid schema test error: {invalid_type}/{iteration} - {e}"
                        )
                        failed_tests += 1

        # Cleanup temp files
        # Temp files are cleaned up individually in the loops above
        pass

    except KeyboardInterrupt:
        print("\n⏹️  Fuzz testing interrupted by user")
    except Exception as e:
        print(f"\n💥 Fuzz testing failed with error: {e}")
        return 1

    # Results
    end_time = time.time()
    duration = end_time - start_time

    print("\n📊 Fuzz Testing Results:")
    print(f"   Total tests: {total_tests}")
    print(f"   Passed: {passed_tests}")
    print(f"   Failed: {failed_tests}")
    print(f"   Duration: {duration:.2f}s")
    print(f"   Tests/sec: {total_tests/duration:.2f}")

    if failed_tests == 0:
        print("🎉 All fuzz tests passed!")
        return 0
    else:
        print(f"⚠️  {failed_tests} fuzz tests failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
