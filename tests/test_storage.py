import unittest
import os
import sqlite3
from storage import FileStorage, SQLStorage
from unittest.mock import patch

class TestFileStorage(unittest.TestCase):

    def test_save_text(self):
        storage = FileStorage()
        file_path = "test_output.txt"
        text = "Sample text to save"
        
        storage.save(file_path, text)
        
        # Check if the file is created and content is correct
        self.assertTrue(os.path.exists(file_path))
        with open(file_path, 'r') as file:
            saved_text = file.read()
            self.assertEqual(saved_text, text)
        
        # Clean up
        os.remove(file_path)

class TestSQLStorage(unittest.TestCase):

    def setUp(self):
        # Setup in-memory SQLite database
        self.db_path = ":memory:"
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tables (Header1 TEXT, Header2 TEXT)")
        self.connection.commit()

    def tearDown(self):
        # Close connection after each test
        self.connection.close()

    def test_save_table(self):
        sql_storage = SQLStorage(self.db_path)

        # Sample table data
        table_data = [('Header1', 'Header2'), ('Data1', 'Data2')]
        
        with patch.object(sql_storage, 'connection', self.connection):
            sql_storage.save(table_data)

            # Verify the data was saved to the database
            self.cursor.execute("SELECT * FROM tables")
            rows = self.cursor.fetchall()
            self.assertEqual(len(rows), 2)  # Header + Data
            self.assertEqual(rows[0], ('Header1', 'Header2'))
            self.assertEqual(rows[1], ('Data1', 'Data2'))

if __name__ == '__main__':
    unittest.main()
