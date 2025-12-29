# Changelog

All notable changes to agentic-dev-boilerplate will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
## [1.1.3] - 2025-12-29

### Added
- Optimized GitHub Copilot customizations for agentic development workflows
- Added specialized instructions for Python, Rust agents, and APIs
- Created prompts for agent architecture design, API security, and testing framework
- Aligned agent schemas with extracted patterns from install-arch project
- Enhanced security posture and code quality guidelines

### Fixed
- Corrected syntax error in generate_boilerplate.py (duplicate main() call)
- Added missing newline at end of file
- Updated agent handoff schemas to structured format



## [1.1.2] - 2025-12-27

### Fixed
- Corrected Jinja2 template rendering issues causing YAML syntax errors in generated workflows
- Fixed test mocking issues for proper CI/CD validation
- Improved error handling in temporary file management
- Resolved directory pruning logic in TmpManager

### Changed
- Updated GitHub Actions to latest versions (checkout@v6, setup-python@v6, etc.)
- Enhanced test coverage and reliability

## [1.1.1] - 2025-12-27

### Added
- Comprehensive test suite with `test-package.sh` script
- Docker container for isolated testing and validation
- UV lock file for reproducible dependency management

### Changed
- Pinned all dependencies to specific versions for reproducibility
- Updated to use UV for all Python package management
- Improved package structure with templates included in wheel
- Enhanced CI/CD with comprehensive testing

### Fixed
- Template path resolution for packaged installation
- Package build configuration to include all necessary files

### Security
- N/A

### Added
- Initial project setup with agentic development boilerplate
- Automated PR creation, validation, and enrichment
- Task tracking and status management
- Commit signing enforcement
- CI/CD automation with phased testing

### Changed
- N/A

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- N/A

### Security
- N/A
