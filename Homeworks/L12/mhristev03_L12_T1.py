import sys
import sqlite3

def create_and_insert_db(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    del_table = "DROP TABLE IF EXISTS food;"
    cursor.execute(del_table)

    create_table_query = """
    CREATE TABLE IF NOT EXISTS food (
        code TEXT,
        descript TEXT,
        nmbr TEXT,
        nutname TEXT,
        retention TEXT
    );
    """
    cursor.execute(create_table_query)

    with open("retn5_dat.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            data = [column.strip('~') for column in line.split('^')]
            if len(data) >= 5:
                code, descript, nmbr, nutname, retention = data[:5]
                cursor.execute("INSERT INTO food (code, descript, nmbr, nutname, retention) VALUES (?, ?, ?, ?, ?);", (code, descript, nmbr, nutname, retention))

    connection.commit()
    connection.close()


db_name = "mhristev03-food.db"
create_and_insert_db(db_name)

query = sys.argv[1]

connection = sqlite3.connect(db_name)
cursor = connection.cursor()

cursor.execute(query)
result = cursor.fetchone()

print(result[0])

connection.close()
