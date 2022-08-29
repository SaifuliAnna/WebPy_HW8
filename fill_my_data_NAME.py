from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_STUDENTS = 30
NUMBER_PROFESSORS = 3

def generate_fake_data(number_students, number_professors) -> tuple():
    fake_students = []
    fake_professors = []

    fake_data = faker.Faker('ru-RU')

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    for _ in range(number_professors):
        fake_professors.append(fake_data.name())

    return fake_students, fake_professors


def prepare_data(students, professors) -> tuple():
    for_students = []
    for_professors = []

    for student in students:
        for_students.append((student, ))

    for professor in professors:
        for_professors.append((professor, ))

    return for_students, for_professors


def insert_data_to_db(students, professors) -> None:

    with sqlite3.connect('points.db') as con:
        cur = con.cursor()
        sql_to_students = """INSERT INTO students(students_name)
                               VALUES (?)"""
        cur.executemany(sql_to_students, students)

        sql_to_professors = """INSERT INTO professors(professors_name)
                               VALUES (?)"""
        cur.executemany(sql_to_professors, professors)

        con.commit()


if __name__ == "__main__":
    students, professors = generate_fake_data(NUMBER_STUDENTS, NUMBER_PROFESSORS)
    students, professors = prepare_data(students, professors)
    insert_data_to_db(students, professors)