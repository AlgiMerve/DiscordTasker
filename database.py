
import sqlite3

class TaskDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('tasks.db')
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        """Görevler tablosunu oluşturur."""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                description TEXT NOT NULL,
                                completed BOOLEAN NOT NULL DEFAULT 0)''')
        self.conn.commit()

    def add_task(self, description):
        """Yeni bir görev ekler"""
        self.cursor.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
        self.conn.commit()
        return self.cursor.lastrowid

    def delete_task(self, task_id):
        """Bir görevi siler"""
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def get_all_tasks(self):
        """Tüm görevleri listeler"""
        self.cursor.execute("SELECT * FROM tasks")
        return self.cursor.fetchall()

    def complete_task(self, task_id):
        """Bir görevi tamamlanmış olarak işaretler"""
        self.cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0
