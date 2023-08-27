import sqlite3

conn = sqlite3.connect('media_manager.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Media (
            id INTEGER PRIMARY KEY,
            title TEXT,
            release_date TEXT,
            genre TEXT,
            synopsis TEXT,
            image_path TEXT);''')

c.execute('''CREATE TABLE IF NOT EXISTS Book (
            media_id INTEGER,
            author TEXT,
            page_count INTEGER,
            language TEXT,
            FOREIGN KEY (media_id) REFERENCES media(id));'''
            )

c.execute('''CREATE TABLE IF NOT EXISTS Game (
            media_id INTEGER, 
            developer TEXT,
            platform TEXT,
            multiplayer_mode INTEGER,
            FOREIGN KEY (media_id) REFERENCES media(id));'''
            )

c.execute('''CREATE TABLE IF NOT EXISTS Movie (
            media_id INTEGER, 
            director TEXT,
            runtime_in_minutes INTEGER,
            production_company TEXT,
            language TEXT,
            country TEXT,
            FOREIGN KEY (media_id) REFERENCES media(id));'''
            )


conn.commit()
conn.close()