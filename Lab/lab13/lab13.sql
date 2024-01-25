.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color = 'blue' AND pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color = "blue" AND pet = "dog";


CREATE TABLE smallest_int_having AS
  SELECT time, smallest from students group by smallest having count(*) = 1;


CREATE TABLE matchmaker AS
  SELECT first.pet, first.song, first.color, second.color from students as first, students as second where first.time < second.time and first.pet = second.pet and first.song = second.song;


CREATE TABLE sevens AS
  SELECT s.seven from students as s, numbers as n where n.'7' = "True" and s.smallest <= 7 and s.time = n.time;

