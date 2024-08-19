CREATE TABLE person (
id INTEGER PRIMARY KEY,
first_name TEXT,
last_name TEXT,
age INTEGER
);
CREATE TABLE pet (
id INTEGER PRIMARY KEY,
name TEXT,
breed TEXT,
age INTEGER,
dead INTEGER
);
CREATE TABLE person_pet (
person_id INTEGER,
pet_id INTEGER
);

SELECT *
FROM person
INNER JOIN person_pet ON person.id = person_pet.person_id
INNER JOIN pet ON person_pet.pet_id = pet.id;