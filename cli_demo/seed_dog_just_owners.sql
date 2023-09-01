DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS handlers;
DROP TABLE IF EXISTS jobs;

CREATE TABLE IF NOT EXISTS owners(
  id INTEGER PRIMARY KEY,
  name TEXT,
  address TEXT,
  email TEXT,
  phone INTEGER
);


CREATE TABLE IF NOT EXISTS pets(
  id INTEGER PRIMARY KEY,
  owner_id INTEGER,
  name TEXT,
  age INTEGER,
  breed TEXT,
  favorite_treats TEXT,
    FOREIGN KEY (owner_id) REFERENCES owners(id)
);


-- Seed Owners table
INSERT INTO owners(name, address, email, phone) 
VALUES ('ix', '999 8th st Seattle Wa 90000', 'ix_is_cool@gmail.com', '9991231234');

INSERT INTO owners(name, address, email, phone) 
VALUES ('Adam', '000 dr sw San Francisco CA 90000', 'cyberpunk999@gmail.com', '0001239999');

-- Seed Pets table
INSERT INTO pets(name, age, breed, favorite_treats, owner_id) 
VALUES ('Luke', '2', 'domestic longhair', 'bacon', 2);

INSERT INTO pets(name, age, breed, favorite_treats, owner_id) 
VALUES ('rose', '11', 'domestic longhair', 'house plants', 1);

INSERT INTO pets(name, age, breed, favorite_treats, owner_id) 
VALUES ('leia', '2', 'domestic Shorthair', 'bacon', 2);

INSERT INTO pets(name, age, breed, favorite_treats, owner_id) 
VALUES ('Chop', '5', 'shiba inu', 'cheese', 1);