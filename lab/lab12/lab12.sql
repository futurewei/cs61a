.read data.sql

-- Q2
CREATE TABLE obedience as
  -- REPLACE THIS LINE
  SELECT seven, denero from students;


-- Q3
CREATE TABLE blue_dog as
  -- REPLACE THIS LINE
  SELECT color, pet from students WHERE color="blue" and pet="dog";


-- Q4
CREATE TABLE smallest_int as
  -- REPLACE THIS LINE
  SELECT time, smallest from students WHERE smallest>6 ORDER BY smallest LIMIT 20;


-- Q5
CREATE TABLE sevens as
  -- REPLACE THIS LINE
  SELECT seven from students, checkboxes WHERE students.time=checkboxes.time and number=7 and checkboxes.'7'="True" LIMIT 14;

-- Q6
CREATE TABLE matchmaker as
  -- REPLACE THIS LINE
  SELECT a.pet, a.song, a.color, b.color from students as a, students as b WHERE a.pet=b.pet AND a.song=b.song and a.time<b.time;


