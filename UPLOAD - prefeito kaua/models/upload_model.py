import sqlite3
from database.db import get_db_connection

class UploadModel:
    @staticmethod
    def save_file(filename, filepath):
        conn = get_db_connection()
        try:
            conn.execute('''
            INSERT INTO uploads (filename, filepath)
            VALEUS (?,?)
        ''',(filename,filepath))
        conn.comit()
    except sqlite3.IntegrityError:
        return None
    finally:
        conn.close()
    return True

@staticmethod
def find_by_filename(filename):
    conn = get_db__connection()
    file = conn.execute('SELECT*')
''')