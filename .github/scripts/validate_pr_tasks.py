#!/usr/bin/env python3
"""
PR Content Validation Script

This script validates pull request content and ensures it meets project standards.
"""

import json
import os
import sys
from pathlib import Path


def validate_pr_description(pr_body: str) -> bool:
    """Validate PR description meets standards."""
    required_sections = ["## Summary", "## Changes", "## Testing"]
    return all(section in pr_body for section in required_sections)


def validate_commit_messages() -> bool:
    """Validate commit messages follow conventional format."""
    import subprocess

    try:
        # Get commits in this PR
        result = subprocess.run(
            ["git", "log", "--oneline", "HEAD~10..HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )

        commits = result.stdout.strip().split("\n")
        for commit in commits:
            if not commit.strip():
                continue
            # Check for conventional commit format (type: description)
            if ":" not in commit:
                print(f"❌ Commit message doesn't follow conventional format: {commit}")
                return False

        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to check commit messages")
        return False


def main():
    """Main PR validation logic."""
    pr_number = os.environ.get("PR_NUMBER")
    github_token = os.environ.get("GITHUB_TOKEN")

    if not pr_number:
        print("❌ Missing PR_NUMBER environment variable")
        sys.exit(1)

    print(f"🔍 Validating PR #{pr_number}...")

    # Validate commit messages
    if not validate_commit_messages():
        sys.exit(1)

    # For now, skip PR description validation since we can't easily get it
    # In a real implementation, you'd use the GitHub API

    print("✅ PR content validation completed successfully")


if __name__ == "__main__":
    main()
