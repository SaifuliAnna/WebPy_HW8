--1
--
SELECT id_students, id_subjects 
FROM points
WHERE (SELECT AVG(points) from points p)
LIMIT 5;

SELECT points, id_students, id_subjects 
FROM points
WHERE points >= (SELECT AVG(points) from points p)
LIMIT 5;

--2
--
SELECT points, id_students, id_subjects 
FROM points
WHERE points >= (SELECT AVG(points) from points p) AND id_subjects = 1006
LIMIT 1;

SELECT points, id_students, id_subjects 
FROM points
WHERE points >= (SELECT AVG(points) from points p) 
LIMIT 1;

SELECT AVG(points), id_students 
FROM points 
WHERE  id_subjects = 1006;

--3
--
SELECT points, id_groups, id_subjects 
FROM points
WHERE points >= (SELECT AVG(points) from points p) 
;

SELECT AVG(points), id_groups, id_subjects
FROM points
WHERE id_groups = 6 AND id_subjects = 1006
;

SELECT AVG(points), id_professors, id_subjects
FROM points
WHERE id_professors = 606 AND id_subjects = 1006
;

--4
--
SELECT points, id_professors, id_subjects 
FROM points
WHERE points >= (SELECT AVG(points) from points p) 
;

SELECT AVG(points), id_groups  
FROM points 
WHERE  id_subjects = 2006;

--5
--
SELECT groups_id, students_name 
FROM students
WHERE groups_id = 6;

SELECT groups_id, students_name 
FROM students
;

--6
--
SELECT points, id_groups, id_subjects  
FROM points 
WHERE  id_subjects = 2006;

SELECT points, id_groups, id_subjects  
FROM points 
;

--7
--
SELECT points, date_class, id_students, id_groups
FROM points 
WHERE date_class = '1992';

--8
--
SELECT DISTINCT id_subjects , id_students 
FROM points 
WHERE id_students = 2;

SELECT DISTINCT id_subjects , id_students 
FROM points 
;

--9
--
SELECT DISTINCT id_subjects , id_students, id_professors
FROM points p 
;

SELECT DISTINCT points, id_subjects , id_students, id_professors
FROM points p 
WHERE points >= (SELECT AVG(points) from points p) 
;

--10

SELECT DISTINCT points, id_professors
FROM points p 
WHERE points >= (SELECT AVG(points) from points p) 
;

SELECT AVG(points), id_professors
FROM points 
WHERE  id_professors = 606;

SELECT AVG(points), id_professors
FROM points 
WHERE  id_professors = 707;

SELECT AVG(points), id_professors
FROM points 
WHERE  id_professors = 808;
