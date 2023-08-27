import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('media_manager.db')
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS books
             (id INTEGER PRIMARY KEY,
             title TEXT,
             author TEXT,
             release_date TEXT,
             genre TEXT,
             page_count INTEGER,
             synopsis TEXT,
             language TEXT,
             image TEXT)''')

# Create a table for games
c.execute('''CREATE TABLE IF NOT EXISTS games
             (id INTEGER PRIMARY KEY,
             title TEXT,
             genre TEXT,
             release_date TEXT,
             developer TEXT,
             platform TEXT,
             synopsis TEXT,
             multiplayer_mode TEXT,
             price REAL,
             image TEXT)''')

# Create a table for movies
c.execute('''CREATE TABLE IF NOT EXISTS movies
             (id INTEGER PRIMARY KEY,
             title TEXT,
             director TEXT,
             release_date TEXT,
             genre TEXT,
             runtime INTEGER,
             synopsis TEXT,
             production_company TEXT,
             language TEXT,
             country TEXT,
             image TEXT,
             trailer TEXT)''')
