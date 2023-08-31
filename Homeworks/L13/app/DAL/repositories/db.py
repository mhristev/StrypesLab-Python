import sqlite3
import random

conn = sqlite3.connect('media_manager.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Media (
            id INTEGER PRIMARY KEY,
            title TEXT,
            release_date TEXT,
            genre TEXT,
            synopsis TEXT,
            image_path TEXT);''')

c.execute('''CREATE TABLE IF NOT EXISTS Author (
            id INTEGER PRIMARY KEY,
            name TEXT);''')

c.execute('''CREATE TABLE IF NOT EXISTS Director (
            id INTEGER PRIMARY KEY,
            name TEXT);''')

c.execute('''CREATE TABLE IF NOT EXISTS Developer (
            id INTEGER PRIMARY KEY,
            name TEXT);''')

c.execute('''CREATE TABLE IF NOT EXISTS Book (
            media_id INTEGER PRIMARY KEY,
            author_id INTEGER,
            page_count INTEGER,
            language TEXT,
            FOREIGN KEY (media_id) REFERENCES Media(id),
            FOREIGN KEY (author_id) REFERENCES Author(id));'''
            )

c.execute('''CREATE TABLE IF NOT EXISTS Game (
            media_id INTEGER PRIMARY KEY,
            developer_id INTEGER,
            platform TEXT,
            multiplayer_mode INTEGER,
            FOREIGN KEY (media_id) REFERENCES Media(id),
            FOREIGN KEY (developer_id) REFERENCES Developer(id));'''
            )

c.execute('''CREATE TABLE IF NOT EXISTS Movie (
            media_id INTEGER PRIMARY KEY,
            director_id INTEGER,
            runtime_in_minutes INTEGER,
            production_company TEXT,
            language TEXT,
            country TEXT,
            FOREIGN KEY (media_id) REFERENCES Media(id),
            FOREIGN KEY (director_id) REFERENCES Director(id));'''
            )

conn.commit()
conn.close()

conn = sqlite3.connect('media_manager.db')
c = conn.cursor()

authors = [('J.K. Rowling',), ('George Orwell',), ('Stephen King',)]
directors = [('Christopher Nolan',), ('Quentin Tarantino',), ('Steven Spielberg',)]
developers = [('Rockstar Games',), ('CD Projekt Red',), ('Ubisoft',)]

c.executemany('INSERT INTO Author (name) VALUES (?)', authors)
c.executemany('INSERT INTO Director (name) VALUES (?)', directors)
c.executemany('INSERT INTO Developer (name) VALUES (?)', developers)

media_data = [
    ('Harry Potter and the Sorcerer\'s Stone', '2001-11-16', 'Fantasy', 'A young wizard\'s journey.', 'path_to_image1.jpg'),
    ('1984', '1950-06-08', 'Dystopian', 'A totalitarian regime.', 'path_to_image2.jpg'),
    ('The Shining', '1977-01-28', 'Horror', 'A haunted hotel.', 'path_to_image3.jpg'),
    ('Inception', '2010-07-16', 'Science Fiction', 'Dream within a dream.', 'path_to_image4.jpg'),
    ('Pulp Fiction', '1994-10-14', 'Crime', 'Interwoven stories.', 'path_to_image5.jpg'),
    ('Jurassic Park', '1993-06-11', 'Science Fiction', 'Dinosaurs come back to life.', 'path_to_image6.jpg'),
    ('Grand Theft Auto V', '2013-09-17', 'Action', 'Open-world mayhem.', 'path_to_image7.jpg'),
    ('The Witcher 3: Wild Hunt', '2015-05-19', 'Role-Playing', 'Monster hunter\'s quest.', 'path_to_image8.jpg'),
    ('Assassin\'s Creed Odyssey', '2018-10-05', 'Action', 'Ancient Greece adventure.', 'path_to_image9.jpg')
]

for media in media_data:
    c.execute('INSERT INTO Media (title, release_date, genre, synopsis, image_path) VALUES (?, ?, ?, ?, ?)', media)

for i in range(1, len(media_data) + 1):
    if i <= 3:
        author_id = random.randint(1, len(authors))
        c.execute('INSERT INTO Book (media_id, author_id, page_count, language) VALUES (?, ?, ?, ?)', (i, author_id, random.randint(200, 800), 'English'))
    elif i <= 6:
        director_id = random.randint(1, len(directors))
        c.execute('INSERT INTO Movie (media_id, director_id, runtime_in_minutes,language, country) VALUES (?, ?, ?, ?, ?)',
                  (i, director_id, random.randint(90, 180), 'English', 'USA'))
    else:
        developer_id = random.randint(1, len(developers))
        c.execute('INSERT INTO Game (media_id, developer_id, platform, multiplayer_mode) VALUES (?, ?, ?, ?)',
                  (i, developer_id, 'Platform', random.randint(0, 1)))

conn.commit()
conn.close()

print("Dummy data inserted successfully!")