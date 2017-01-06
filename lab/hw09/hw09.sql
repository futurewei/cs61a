create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
select dogs.name as name, sizes.size as size from dogs, sizes where 
sizes.min<dogs.height and dogs.height<=sizes.max;


-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
select child from parents, dogs where parent=dogs.name order by -dogs.height;


-- Sentences about siblings that are the same size
create table sentences as
select p1.child ||" and "|| p2.child||" are "||s1.size ||" siblings"
from parents as p1, parents as p2, size_of_dogs as s1, size_of_dogs as s2 where  p1.parent=p2.parent 
and p1.child !=p2.child and p1.child=s1.name and p2.child=s2.name and s1.size=s2.size and s1.name<s2.name
;


-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
 with 
    stack_table(names, total, n, last) as (
       select  name, height, 1, height from dogs union
       select  names||", "||name, total + height, n+1, height from stack_table, dogs where n < 4 and height>last
       )
  select names, total from stack_table where n=4 and total>=170 order by total;



create table tallest as
  with 
    range(name, digit) as (
       select "abraham" , 20  union
       select "barack"  , 50  union
       select "clinton" , 40  union
       select "delano"  , 40  union
       select "eisenhower" , 30  union
       select "fillmore" , 30  union
       select "grover", 20  union
       select "herbert", 30
      )
select max(dogs.height), dogs.name from dogs, range where dogs.name=range.name group by range.digit having count(range.digit)>1;


-- All non-parent relations ordered by height difference
create table non_parents as
select "REPLACE THIS LINE WITH YOUR SOLUTION";


