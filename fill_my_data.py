import sqlite3
from sqlite3 import Error
from contextlib import contextmanager


# підключення до бази даних SQLite у файлі
@contextmanager
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        yield conn
        conn.commit()
    except Error as e:
        conn.rollback()
        print(e)
    finally:
        conn.close()


# Створимо допоміжну функцію для створення таблиць
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


# SQL запити для створення таблиць:
sql_create_groups_table = """CREATE TABLE IF NOT EXISTS 
groups (
id INTEGER PRIMARY KEY,
groups_name VARCHAR(50) NOT NULL
);"""


sql_create_students_table = """CREATE TABLE IF NOT EXISTS 
students (
id INTEGER PRIMARY KEY,
students_name VARCHAR(50) NOT NULL,
groups_id INTEGER,
FOREIGN KEY (groups_id) REFERENCES groups (id)
);"""


sql_create_subjects_table = """CREATE TABLE IF NOT EXISTS 
subjects (
id INTEGER PRIMARY KEY,
subjects_name VARCHAR(50) NOT NULL,
groups_id INTEGER,
FOREIGN KEY (groups_id) REFERENCES groups (id)
);"""


sql_create_professors_table = """CREATE TABLE IF NOT EXISTS 
professors (
id INTEGER PRIMARY KEY,
professors_name VARCHAR(50) NOT NULL,
groups_id INTEGER,
FOREIGN KEY (groups_id) REFERENCES groups (id)
);"""


sql_create_points_table = """CREATE TABLE IF NOT EXISTS points (
id INTEGER PRIMARY KEY,
points INTEGER,
groups_id integer NOT NULL,
students_id integer NOT NULL,
subjects_id integer NOT NULL,
professors_id integer NOT NULL,
date_class VARCHAR(50) NOT NULL,
FOREIGN KEY (students_id) REFERENCES students (id)
);"""


database = './points.db'
with create_connection(database) as conn:
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_groups_table)
        # create tasks table
        create_table(conn, sql_create_students_table)

        create_table(conn, sql_create_professors_table)
        create_table(conn, sql_create_subjects_table)
        create_table(conn, sql_create_points_table)

    else:
        print("Error! cannot create the database connection.")

