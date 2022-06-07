import sqlite3, csv

# connection = database.connect()


CREATE_TABLE = """CREATE TABLE IF NOT EXISTS tests ( num INTEGER,question TEXT,a TEXT,b TEXT,c TEXT,answer TEXT )"""

INSERT_TO_TABLE = "INSERT INTO tests (num,question,a,b,c,answer) VALUES (?,?,?,?,?,?)"

INSERT_ALL = "SELECT * FROM tests"

ONLY_QUESTIONS = "SELECT  question, * FROM tests"


GET_RANDOM = "SELECT * FROM tests ORDER BY random() LIMIT 5;"


# Connect to DATABASE
def connect():
    return sqlite3.connect("tests.db")


# Create table in DATABASE
def create_table(connection):
    with connection:
        connection.execute(CREATE_TABLE)


# Insert info to DATABASE
def add_tests_to_table(connection, num, question, a, b, c, answer):
    with connection:
        connection.execute(INSERT_TO_TABLE, (num, question, a, b, c, answer))


# Show all info of DATABASE
def show_all(connection):
    with connection:
        return connection.execute(INSERT_ALL).fetchall()


# Take 5 random rows from DATABASE
def random(connection):
    with connection:
        return connection.execute(GET_RANDOM).fetchall()


# Import CSV to SQLite
def import_csv(connection):
    with open("data.csv", "r") as file:
        num_records = 0
        for row in file:
            connection.execute("INSERT INTO tests VALUES (?,?,?,?,?,?)", row.split(","))
        connection.commit()
        num_records += 1
    connection.close()
    print(f"{num_records} Records Transferred!")
