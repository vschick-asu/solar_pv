-- Vladimir Schick

-- create test database
CREATE DATABASE IF NOT EXISTS deleteme;

-- switch to our database
USE deleteme;



-- create publisher table
CREATE TABLE IF NOT EXISTS publisher (
  Name char NOT NULL PRIMARY KEY,
  Address char NOT NULL,
  Phone int NOT NULL
  );

-- create library_branch table
CREATE TABLE IF NOT EXISTS library_branch (
  Branch_id char NOT NULL PRIMARY KEY,
  Branch_name char NOT NULL,
  Address char NOT NULL
  );

-- create borrower table
CREATE TABLE IF NOT EXISTS borrower (
  Card_no int NOT NULL PRIMARY KEY,
  Name char NOT NULL,
  Address char NOT NULL,
  Phone int NOT NULL
  );

-- create book table
CREATE TABLE IF NOT EXISTS book (
  Book_id char NOT NULL PRIMARY KEY,
  Title char NOT NULL,
  Publisher_name char NOT NULL,
  FOREIGN KEY (Publisher_name) REFERENCES publisher(Name)
  );
-- create book_copies table
CREATE TABLE IF NOT EXISTS book_copies (
  Book_id char NOT NULL PRIMARY KEY,
  FOREIGN KEY (Book_id) REFERENCES book(Book_id),
  Branch_id char NOT NULL,
  FOREIGN KEY (Branch_id) REFERENCES library_branch(Branch_id),
  No_of_copies int NOT NULL
  );


-- create author table
CREATE TABLE IF NOT EXISTS book_authors (
  Book_id char NOT NULL PRIMARY KEY,
  Author_name char NOT NULL,
  FOREIGN KEY (Book_id) REFERENCES book(Book_id)
  );

-- create book_loans table
CREATE TABLE IF NOT EXISTS book_loans (
  Book_id char NOT NULL PRIMARY KEY,
  FOREIGN KEY (Book_id) REFERENCES book(Book_id),
  Branch_id char NOT NULL,
  FOREIGN KEY (Branch_id) REFERENCES library_branch(Branch_id),
  Card_no int NOT NULL,
  FOREIGN KEY (Card_no) REFERENCES borrower(Card_no),
  Date_out int NOT NULL
  );
