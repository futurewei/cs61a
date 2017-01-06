create table pizzas as
  select "Pizzahhh" as name, 12 as open, 15 as close union
  select "La Val's"        , 11        , 22          union
  select "Sliver"          , 11        , 20          union
  select "Cheeseboard"     , 16        , 23          union
  select "Emilia's"        , 13        , 18;

create table meals as
  select "breakfast" as meal, 11 as time union
  select "lunch"            , 13         union
  select "dinner"           , 19         union
  select "snack"            , 22;

-- Two meals at the same place
create table double as
select a.meal, b.meal, p.name from meals as a, meals as b, pizzas as p where p.open<=a.time and a.time <=p.close 
and p.open<=b.time and b.time <=p.close and b.time-a.time>6;


-- Pizza options for every meal
create table options as
   with
       choice(mea, n, list, last, time) as (
      		select m.meal, 1, p.name, p.name, m.time from meals as m, pizzas as p where p.open<= m.time and m.time <=p.close union
      		select m.meal, n+1, list||", "||p.name, p.name, m.time from choice, meals as m, pizzas as p where m.meal=mea and p.open<= m.time and m.time <=p.close 
          and last<p.name
          )
       select mea as meal, * from choice;