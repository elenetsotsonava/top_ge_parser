import sqlite3


class DB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS top_info(
                id INTEGER PRIMARY KEY,
                name TEXT,
                topic TEXT,
                description TEXT
            )
        ''')

    def add_info(self, info):
        self.cursor.execute("INSERT INTO top_info(name, topic, description) VALUES (?, ?, ?)",
                            (info.name,  info.topic, info.description))
        self.conn.commit()
