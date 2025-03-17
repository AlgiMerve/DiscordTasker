
import unittest
from database import TaskDatabase

class TestCompleteTask(unittest.TestCase):
    def setUp(self):
        self.db = TaskDatabase()
        self.db.add_task('Test görev tamamlama')

    def test_complete_task(self):
        task_id = self.db.get_all_tasks()[0][0]
        self.db.complete_task(task_id)
        task = self.db.get_all_tasks()[0]
        self.assertEqual(task[2], 1)  # Görev tamamlanmış olmalı (completed = 1)
