"""Tests for tmp_manager module."""

import pytest
import tempfile
import shutil
from pathlib import Path
from unittest.mock import patch
import time

from agentic_dev_boilerplate.tmp_manager import TmpManager, TmpConfig, get_tmp_manager


class TestTmpManager:
    """Test cases for TmpManager."""

    def setup_method(self):
        """Set up test environment."""
        self.config = TmpConfig(
            base_tmp_dir=Path(tempfile.mkdtemp()),
            max_age_hours=0.001,  # Very short for testing
            max_project_dirs=5
        )
        self.project_name = "test_project"
        self.manager = TmpManager(self.project_name, self.config)

    def teardown_method(self):
        """Clean up test environment."""
        if self.config.base_tmp_dir.exists():
            shutil.rmtree(self.config.base_tmp_dir)

    def test_initialization(self):
        """Test TmpManager initialization."""
        assert self.manager.project_name == self.project_name
        assert self.manager.project_tmp_dir.exists()
        assert self.manager.project_tmp_dir.name == self.manager.project_hash

    def test_get_task_dir(self):
        """Test getting task directory."""
        task_id = "task_123"
        task_dir = self.manager.get_task_dir(task_id)
        assert task_dir.exists()
        assert task_dir.name == task_id
        assert task_dir.parent == self.manager.project_tmp_dir

    def test_get_subtask_dir(self):
        """Test getting subtask directory."""
        task_id = "task_123"
        subtask_id = "subtask_456"
        subtask_dir = self.manager.get_subtask_dir(task_id, subtask_id)
        assert subtask_dir.exists()
        assert subtask_dir.name == subtask_id
        assert subtask_dir.parent.name == task_id

    def test_write_read_task_context(self):
        """Test writing and reading task context."""
        task_id = "task_123"
        context = {"key": "value", "number": 42}

        self.manager.write_task_context(task_id, context)
        read_context = self.manager.read_task_context(task_id)

        assert read_context == context

    def test_write_read_subtask_data(self):
        """Test writing and reading subtask data."""
        task_id = "task_123"
        subtask_id = "subtask_456"
        filename = "data.bin"
        data = b"test binary data"

        self.manager.write_subtask_data(task_id, subtask_id, filename, data)
        read_data = self.manager.read_subtask_data(task_id, subtask_id, filename)

        assert read_data == data

    def test_cleanup_task(self):
        """Test cleaning up task directory."""
        task_id = "task_123"
        task_dir = self.manager.get_task_dir(task_id)
        assert task_dir.exists()

        self.manager.cleanup_task(task_id)
        assert not task_dir.exists()

    def test_cleanup_subtask(self):
        """Test cleaning up subtask directory."""
        task_id = "task_123"
        subtask_id = "subtask_456"
        subtask_dir = self.manager.get_subtask_dir(task_id, subtask_id)
        assert subtask_dir.exists()

        self.manager.cleanup_subtask(task_id, subtask_id)
        assert not subtask_dir.exists()
        # Task dir should still exist
        assert self.manager.get_task_dir(task_id).exists()

    def test_prune_old_directories(self):
        """Test pruning old directories."""
        # Create some old directories
        old_dir = self.config.base_tmp_dir / "old_project"
        old_dir.mkdir()
        old_dir.touch()  # Make it old
        old_dir_stat = old_dir.stat()
        # Set mtime to old
        old_time = time.time() - 3600 * 2  # 2 hours ago
        Path(old_dir, ".touch").touch()
        old_dir.stat().st_mtime = old_time  # This doesn't work, need os.utime

        import os
        os.utime(old_dir, (old_time, old_time))

        # Create a new directory
        new_dir = self.config.base_tmp_dir / "new_project"
        new_dir.mkdir()

        self.manager.prune_old_directories()

        # Old dir should be gone, new should remain
        assert not old_dir.exists()
        assert new_dir.exists()

    def test_get_project_info(self):
        """Test getting project info."""
        # Create some files
        task_dir = self.manager.get_task_dir("task1")
        (task_dir / "file1.txt").write_text("content")
        (task_dir / "file2.txt").write_text("content2")

        info = self.manager.get_project_info()
        assert info["project_name"] == self.project_name
        assert info["file_count"] == 2
        assert info["dir_count"] >= 1  # At least the task dir
        assert info["total_size_bytes"] > 0

    def test_get_tmp_manager_singleton(self):
        """Test get_tmp_manager returns singleton."""
        manager1 = get_tmp_manager("project1")
        manager2 = get_tmp_manager("project1")
        assert manager1 is manager2

        manager3 = get_tmp_manager("project2")
        assert manager3 is not manager1