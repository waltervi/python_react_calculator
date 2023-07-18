-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS operation;
DROP TABLE IF EXISTS record;

-- User
-- ○ id
-- ○ username (email)
-- ○ password
-- ○ status (active, inactive)
-- ○ current_balance (New filed added)
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  status INTEGER,
  user_balance REAL NOT NULL
);

-- Operation
-- ○ id
-- ○ type (addition, subtraction, multiplication, division, square_root, random_string) 
-- ○ cost
CREATE TABLE operation (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  type INTEGER NOT NULL,
  cost REAL NOT NULL
);

-- Record
-- ○ id
-- ○ operation_id
-- ○ user_id
-- ○ amount
-- ○ user_balance
-- ○ operation_response
-- ○ date
CREATE TABLE record (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  operation_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  amount REAL NOT NULL,
  operation_response INTEGER NOT NULL,
  user_balance REAL NOT NULL,
  date INTEGER NOT NULL,
  deleted  INTEGER
);

INSERT INTO operation (type, cost) VALUES("ADDITION",10);
INSERT INTO operation (type, cost) VALUES("SUBSTRACTION",20);
INSERT INTO operation (type, cost) VALUES("MULTIPLICATION",30);
INSERT INTO operation (type, cost) VALUES("DIVISION",40);
INSERT INTO operation (type, cost) VALUES("SQUARE_ROOT",50);
INSERT INTO operation (type, cost) VALUES("RANDOM_STRING",60);

