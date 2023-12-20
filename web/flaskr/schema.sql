DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS credit;
DROP TABLE IF EXISTS who_borrow;
DROP TABLE IF EXISTS loans;

CREATE TABLE user (
  id VARCHAR(255) PRIMARY KEY NOT NULL,
  phone VARCHAR(255) UNIQUE NOT NULL,
  username TEXT NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE credit(
  id VARCHAR(255)  PRIMARY KEY REFERENCES user(id),
  rank TEXT NOT NULL
);

CREATE TABLE who_borrow(
  borrow_id INTEGER PRIMARY KEY AUTOINCREMENT,
  id VARCHAR(255) NOT NULL REFERENCES user(id),
  loan_id INTEGER NOT NULL REFERENCES loans(loan_id),
  loan_date date NOT NULL
);

CREATE TABLE loans(
  loan_id INTEGER PRIMARY KEY NOT NULL,
  rank TEXT NOT NULL REFERENCES credit(rank),
  loan_type TEXT NOT NULL,
  amount INTEGER NOT NULL,
  interest DECIMAL(5, 2),
  repay TEXT NOT NULL,
  loan_period INTEGER NOT NULL
);


