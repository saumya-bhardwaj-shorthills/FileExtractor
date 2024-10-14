import sqlite3
from storage.storage import Storage

class SQLStorage(Storage):
    def __init__(self, db_path: str):
        """Initialize with the path to the SQLite database."""
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        """Create the 'extracted_data' table if it doesn't exist."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS extracted_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT,
                content TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def save(self, data, data_type: str):
        """Save extracted data based on its type (text, image, url, table)."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        if data_type == 'table':
            # Convert the table (list of lists) into a string format to store in the database
            for table in data:
                if isinstance(table, list):
                    # Create tab-separated rows to store table data in string format
                    table_content = "\n".join(["\t".join(map(str, row)) for row in table if isinstance(row, (list, tuple))])
                    cursor.execute('INSERT INTO extracted_data (type, content) VALUES (?, ?)', (data_type, table_content))
                else:
                    # If table is not a list of lists, handle it as a simple data type
                    cursor.execute('INSERT INTO extracted_data (type, content) VALUES (?, ?)', (data_type, str(table)))
        else:
            # Save text, images, and URLs normally
            for item in data:
                if isinstance(item, (list, dict)):
                    item = str(item)  # Convert lists/dicts to strings for storage
                cursor.execute('INSERT INTO extracted_data (type, content) VALUES (?, ?)', (data_type, item))

        conn.commit()
        conn.close()


 
