
import unittest
from database import TaskDatabase

class TestShowTasks(unittest.TestCase):
    def setUp(self):
        self.db = TaskDatabase()
        self.db.add_task('Test görev gösterme')

    def test_show_tasks(self):
        tasks = self.db.get_all_tasks()
        self.assertGreater(len(tasks), 0)  # Görevler listelenmeli
        self.assertIn('Test görev gösterme', [task[1] for task in tasks])  # Görev açıklaması doğru olmalı
