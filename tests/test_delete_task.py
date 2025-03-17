
import unittest
from database import TaskDatabase

class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        self.db = TaskDatabase()
        self.db.add_task('Test görev silme')

    def test_delete_task(self):
        tasks_before = self.db.get_all_tasks()
        task_id = tasks_before[0][0]
        self.db.delete_task(task_id)
        tasks_after = self.db.get_all_tasks()
        self.assertLess(len(tasks_after), len(tasks_before))  # Görev silinmiş olmalı
