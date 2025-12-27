# Agentic Development Boilerplate

A templatized repository that generates tailored agentic development workflows and automations for any project.

## Overview

This repository contains reusable components for creating sophisticated development workflows with:
- 🤖 Multi-agent coordination and task management
- 🔄 Automated PR creation, validation, and enrichment
- 📋 Intelligent task tracking and status management
- 🔐 Commit signing enforcement
- 🚀 CI/CD automation with phased testing
- 📊 Comprehensive validation and quality gates

## Quick Start

1. **Define your project schema** in `project-schema.yaml`
2. **Run the generator**: `python generate_boilerplate.py`
3. **Apply to your project**: Copy generated files to your target repository

## Project Schema

Define your project characteristics in `project-schema.yaml`:

```yaml
project:
  name: "my-awesome-project"
  description: "A description of what this project does"
  repository: "https://github.com/username/my-awesome-project"
  private: true

languages:
  - name: "python"
    version: "3.11"
    frameworks: ["fastapi", "pytest"]
  - name: "typescript"
    version: "5.0"
    frameworks: ["react", "node"]

agents:
  - role: "tester"
    enabled: true
    scope: ["unit", "integration", "system"]
  - role: "debugger"
    enabled: true
    scope: ["error-analysis", "performance"]
  - role: "deployer"
    enabled: true
    scope: ["staging", "production"]

workflows:
  pr_automation: true
  task_tracking: true
  commit_signing: true
  ci_cd: true

git:
  default_branch: "main"
  commit_signing: true
  pull_rebase: true
  push_default: "current"
```

## Generated Components

The generator creates:

### 🤖 Agent System
- **Instructions**: Specialized agent roles with domain expertise
- **Prompts**: Reusable prompt templates for common tasks
- **Coordination**: Multi-agent handoffs and workflow orchestration

### 🔄 PR Automation
- **GitHub Actions**: Automated PR enrichment and validation
- **Scripts**: PR creation, labeling, milestone assignment
- **Validation**: Commit message format, task alignment, quality checks

### 📋 Task Management
- **Tracker**: YAML-based task tracking with status management
- **Context**: Structured context files for task scoping
- **Automation**: Status updates and progress tracking

### 🔐 Security & Quality
- **Commit Signing**: GPG key setup and enforcement
- **Validation**: Code quality, security scanning, dependency checks
- **CI/CD**: Automated testing and deployment pipelines

### 🛠️ Development Tools
- **Git Configuration**: Optimized git settings and aliases
- **Scripts**: Repository management and setup utilities
- **Documentation**: Comprehensive guides and troubleshooting

## Agent Roles

### Core Agents
- **Planner**: Task decomposition and roadmap generation
- **Tester**: Validation suites and quality assurance
- **Debugger**: Root cause analysis and issue resolution
- **Deployer**: Production deployment and rollback orchestration

### Specialized Agents
- **Code Reviewer**: Code quality and best practices
- **Security Auditor**: Vulnerability assessment and compliance
- **Performance Analyst**: Benchmarking and optimization
- **Documentation Specialist**: Technical writing and maintenance

## Customization

### Language-Specific Templates
- **Python**: pytest, black, mypy, poetry
- **JavaScript/TypeScript**: jest, eslint, prettier, npm/yarn
- **Go**: go test, golint, goreleaser
- **Rust**: cargo test, clippy, rustfmt
- **Java**: maven/gradle, junit, spotbugs

### Framework Integration
- **Web Frameworks**: React, Vue, Angular, FastAPI, Django
- **Cloud Platforms**: AWS, GCP, Azure, Kubernetes
- **Databases**: PostgreSQL, MySQL, MongoDB, Redis
- **Infrastructure**: Terraform, Ansible, Docker, Helm

## Usage Examples

### Python Web API
```yaml
project:
  name: "user-api"
  description: "REST API for user management"

languages:
  - name: "python"
    version: "3.11"
    frameworks: ["fastapi", "sqlalchemy", "pytest"]

agents:
  - role: "tester"
  - role: "debugger"
  - role: "deployer"

workflows:
  pr_automation: true
  commit_signing: true
  ci_cd: true
```

### React Application
```yaml
project:
  name: "dashboard-ui"
  description: "Admin dashboard built with React"

languages:
  - name: "typescript"
    version: "5.0"
    frameworks: ["react", "jest"]

agents:
  - role: "tester"
  - role: "debugger"

workflows:
  pr_automation: true
  task_tracking: true
```

## Requirements

- Python 3.11+
- **uv** (fast Python package installer and virtual environment manager)
- Git 2.30+
{% if schema.git.commit_signing %}- **GPG** (for commit signing){% endif %}
- GitHub CLI (optional, for PR management)

## Contributing

This boilerplate repository itself uses the generated workflows! See `project-schema.yaml` for the configuration that generates this repository's own automation.