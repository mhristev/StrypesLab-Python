import sqlite3

class BaseRepository:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BaseRepository, cls).__new__(cls)
            cls._instance.connect_to_database()
        return cls._instance
    
    def __del__(self):
        self.close_connection()
        
    def connect_to_database(self):
        self.conn = sqlite3.connect('media_manager.db')
        self.cursor = self.conn.cursor()

    def close_connection(self):
        self.conn.commit()
        self.conn.close()