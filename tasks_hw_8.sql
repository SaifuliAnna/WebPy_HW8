--1
--


--2
--
SELECT AVG(points), id_students 
FROM points 
WHERE  id_subjects == 1006;

--3
--
SELECT AVG(points), id_groups  
FROM points 
WHERE  id_subjects == 2006;

--4
--


--5
--
SELECT AVG(points), id_groups  
FROM points 
WHERE  id_subjects = 2006;

--6
--
SELECT students_name 
FROM students
WHERE groups_id = 6;

--7
--


--8
--
SELECT DISTINCT id_subjects , id_students 
FROM points 
WHERE id_students = 2;

--9
--


--SELECT  id_subjects , id_students, id_professors, AVG(points) 
--FROM points 
--WHERE id_students = 2 
--AND id_subjects = 1007
--;
--
--SELECT  id_subjects , id_students, id_professors, AVG(points) 
--FROM points 
--WHERE id_students = 2;
--
--SELECT  id_subjects , id_students, id_professors, AVG(points) 
--FROM points 
--;

--10
--SELECT AVG(points) FROM points;

SELECT AVG(points), id_professors
FROM points 
WHERE  id_professors = 606;

SELECT AVG(points), id_professors
FROM points 
WHERE  id_professors = 707;

SELECT AVG(points), id_professors
FROM points 
WHERE  id_professors = 808;
