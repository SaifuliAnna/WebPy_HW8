from random import randint, choice
from datetime import datetime
from pprint import pprint


list_id_groups = [6, 7, 8]
list_id_subjects = [1006, 1007, 1008, 2006, 3006]

print('INSERT INTO points (id,points,id_groups,id_students,id_subjects,id_professors,date_class) VALUES')

for id in range(1, 3001):
    points = randint(9, 12)

    for _ in range(21):
        id_groups = choice(list_id_groups)

        if id_groups == 6:
            id_students = randint(1, 10)
            id_subjects = choice(list_id_subjects[:3])
            id_professors = 606

        if id_groups == 7:
            id_students = randint(11, 20)
            id_subjects = list_id_subjects[3]
            id_professors = 707

        if id_groups == 8:
            id_students = randint(21, 30)
            id_subjects = list_id_subjects[4]
            id_professors = 808

    for month in range(1, 10):
        date_class = datetime(2021, month, randint(10, 20)).date()

    print(f"({id},{points},{id_groups},{id_students},{id_subjects},{id_professors},{date_class}),")

print(f';')
