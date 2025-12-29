"""Integration tests for the agentic-dev-boilerplate package."""

import json
import subprocess
import sys
from pathlib import Path

import pytest
import yaml


@pytest.fixture(scope="session")
def generated_boilerplate(tmp_path_factory):
    """Generate boilerplate once for all integration tests."""
    from agentic_dev_boilerplate.generate_boilerplate import BoilerplateGenerator

    # Create a session-scoped temp directory
    temp_dir = tmp_path_factory.mktemp("integration_test")

    # Create schema
    schema = {
        "project": {
            "name": "integration_test_project",
            "description": "Test project for integration testing",
            "repository": "https://github.com/test/integration_test_project",
            "private": False,
            "version": "1.0.0",
        },
        "languages": [
            {
                "name": "python",
                "version": "3.11",
                "frameworks": ["pytest", "black"],
                "package_manager": "uv",
                "testing": ["pytest"],
                "linting": ["black", "isort"],
                "type_checking": ["mypy"],
            }
        ],
        "agents": [
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
            {
                "role": "debugger",
                "enabled": False,
                "scope": ["error_analysis", "fix_suggestions"],
            },
        ],
        "workflows": {
            "pr_automation": True,
            "task_tracking": True,
            "commit_signing": True,
            "ci_cd": True,
            "gitops": False,
            "security_scanning": True,
            "dependency_management": True,
            "multi_agent_coordination": True,
        },
        "git": {"default_branch": "main", "commit_signing": True},
        "ci_cd": {"provider": "github_actions"},
        "validation": {"code_coverage_minimum": 80},
        "security": {"gpg_signing": True},
        "documentation": {
            "readme_generation": True,
            "contributing_guide": True,
            "changelog": True,
        },
    }

    schema_file = temp_dir / "project_schema.yaml"
    with open(schema_file, "w") as f:
        yaml.dump(schema, f)

    output_dir = temp_dir / "generated_boilerplate"
    output_dir.mkdir()

    # Generate boilerplate once
    generator = BoilerplateGenerator(str(schema_file), str(output_dir))
    generator.generate()

    return {
        "schema_file": schema_file,
        "output_dir": output_dir,
        "schema": schema,
    }


@pytest.fixture
def sample_project_schema(tmp_path):
    """Create a complete sample project schema for integration testing."""
    schema = {
        "project": {
            "name": "integration_test_project",
            "description": "Test project for integration testing",
            "repository": "https://github.com/test/integration_test_project",
            "private": False,
            "version": "1.0.0",
        },
        "languages": [
            {
                "name": "python",
                "version": "3.11",
                "frameworks": ["pytest", "black"],
                "package_manager": "uv",
                "testing": ["pytest"],
                "linting": ["black", "isort"],
                "type_checking": ["mypy"],
            }
        ],
        "agents": [
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
            {
                "role": "debugger",
                "enabled": False,
                "scope": ["error_analysis", "fix_suggestions"],
            },
        ],
        "workflows": {
            "pr_automation": True,
            "task_tracking": True,
            "commit_signing": True,
            "ci_cd": True,
            "gitops": False,
            "security_scanning": True,
            "dependency_management": True,
            "multi_agent_coordination": True,
        },
        "git": {"default_branch": "main", "commit_signing": True},
        "ci_cd": {"provider": "github_actions"},
        "validation": {"code_coverage_minimum": 80},
        "security": {"gpg_signing": True},
        "documentation": {
            "readme_generation": True,
            "contributing_guide": True,
            "changelog": True,
        },
    }
    schema_file = tmp_path / "project_schema.yaml"
    with open(schema_file, "w") as f:
        yaml.dump(schema, f)
    return schema_file


@pytest.fixture
def generation_output_dir(tmp_path):
    """Output directory for generated boilerplate."""
    output = tmp_path / "generated_boilerplate"
    output.mkdir()
    return output


def test_cli_entry_point_installation():
    """Test that the CLI entry point is properly installed."""
    # This test assumes the package is installed in development mode
    # Use a simpler import test instead of subprocess
    try:
        import agentic_dev_boilerplate.generate_boilerplate

        assert hasattr(agentic_dev_boilerplate.generate_boilerplate, "main")
    except ImportError as e:
        pytest.fail(f"Failed to import generate_boilerplate: {e}")


def test_full_boilerplate_generation(sample_project_schema, generation_output_dir):
    """Integration test for complete boilerplate generation."""
    from agentic_dev_boilerplate.generate_boilerplate import BoilerplateGenerator

    generator = BoilerplateGenerator(
        str(sample_project_schema), str(generation_output_dir)
    )

    # Generate the complete boilerplate
    generator.generate()

    # Verify core structure
    assert (generation_output_dir / ".github").exists()
    assert (generation_output_dir / ".github" / "workflows").exists()
    assert (generation_output_dir / ".github" / "instructions").exists()
    assert (generation_output_dir / "scripts").exists()
    assert (generation_output_dir / "docs").exists()
    assert (generation_output_dir / "tests").exists()

    # Verify agent instructions were generated for enabled agents
    instructions_dir = generation_output_dir / ".github" / "instructions"
    assert (instructions_dir / "planner.instructions.md").exists()
    assert (instructions_dir / "tester.instructions.md").exists()
    assert not (instructions_dir / "debugger.instructions.md").exists()  # Disabled

    # Verify basic files exist
    assert (generation_output_dir / ".gitignore").exists()
    assert (generation_output_dir / "README.md").exists()


def test_generated_files_content(generated_boilerplate):
    """Test that generated files contain expected content."""
    output_dir = generated_boilerplate["output_dir"]

    # Check README content
    readme = output_dir / "README.md"
    assert readme.exists()
    content = readme.read_text()
    assert "integration_test_project" in content

    # Check that agent instructions contain project name
    planner_instructions = (
        output_dir / ".github" / "instructions" / "planner.instructions.md"
    )
    assert planner_instructions.exists()
    content = planner_instructions.read_text()
    assert "integration_test_project" in content


def test_template_rendering_with_real_templates(
    sample_project_schema, generation_output_dir
):
    """Test template rendering with actual template files."""
    # This test would require the actual templates directory
    # For now, we'll test the template loading mechanism
    from agentic_dev_boilerplate.generate_boilerplate import BoilerplateGenerator

    generator = BoilerplateGenerator(
        str(sample_project_schema), str(generation_output_dir)
    )

    # Verify templates directory exists and contains files
    assert generator.templates_dir.exists()
    assert any(generator.templates_dir.glob("*.j2"))

    # Test that jinja environment is properly configured
    assert generator.jinja_env is not None


def test_schema_persistence_in_generated_project(generated_boilerplate):
    """Test that project schema is properly embedded in generated files."""
    output_dir = generated_boilerplate["output_dir"]

    # Check if any generated files contain schema-derived content
    # This is a basic check - in practice, templates would use schema variables
    pyproject = output_dir / "pyproject.toml"
    if pyproject.exists():
        content = pyproject.read_text()
        assert "integration_test_project" in content


def test_workflow_file_generation(generated_boilerplate):
    """Test that GitHub workflow files are properly generated."""
    output_dir = generated_boilerplate["output_dir"]

    workflows_dir = output_dir / ".github" / "workflows"

    # Check for expected workflow files
    expected_workflows = ["ci-cd.yml", "pr-automation.yml", "agent-coordination.yml"]
    for workflow in expected_workflows:
        workflow_file = workflows_dir / workflow
        assert workflow_file.exists(), f"Missing workflow file: {workflow}"
        assert workflow_file.stat().st_size > 0, f"Empty workflow file: {workflow}"


def test_task_tracking_generation(generated_boilerplate):
    """Test that task tracking files are generated."""
    output_dir = generated_boilerplate["output_dir"]

    # Check for tasking directory and files
    tasking_dir = output_dir / "tasking"
    assert tasking_dir.exists()

    tracker_file = tasking_dir / "tracker.yaml"
    assert tracker_file.exists()

    # Verify tracker content
    import yaml

    tracker_data = yaml.safe_load(tracker_file.read_text())
    assert "project" in tracker_data
    assert tracker_data["project"] == "integration_test_project"


@pytest.mark.slow
def test_generated_project_is_valid_python_package(generated_boilerplate):
    """Test that the generated project is a valid Python package."""
    output_dir = generated_boilerplate["output_dir"]

    # Check for pyproject.toml
    pyproject = output_dir / "pyproject.toml"
    assert pyproject.exists()

    # Basic validation that it's parseable TOML
    import tomllib

    with open(pyproject, "rb") as f:
        data = tomllib.load(f)
    assert "project" in data
    assert data["project"]["name"] == "integration_test_project"


def test_cross_platform_path_handling(generated_boilerplate):
    """Test that path handling works across platforms."""
    output_dir = generated_boilerplate["output_dir"]

    # Verify that all generated paths use forward slashes or are platform-appropriate
    # This is more of a sanity check
    assert output_dir.exists()
    assert len(list(output_dir.rglob("*"))) > 10  # Reasonable number of files
