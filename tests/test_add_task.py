
import unittest
from database import TaskDatabase

class TestTaskDatabase(unittest.TestCase):
    def setUp(self):
        """Her testten önce çalışacak fonksiyon"""
        self.db = TaskDatabase()

    def test_add_task(self):
        """Görev ekleme fonksiyonunu test eder"""
        task_id = self.db.add_task("Yeni görev")
        tasks = self.db.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][1], "Yeni görev")
        self.assertFalse(tasks[0][2])  # Görev tamamlanmadı

if __name__ == "__main__":
    unittest.main()
