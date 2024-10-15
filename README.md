# Lecture # 6 - SQL Fundamentals & Table Relations

## Lecture Topics

- SQL statements
  - `CREATE TABLE table_name (id INTEGER PRIMARY KEY, column2 TEXT, column3 INTEGER);`
  - `ALTER TABLE table_name ADD COLUMN column4 TEXT;`
  - `DROP TABLE table_name;`
- SQL commands
  - `.help`
  - `.tables`
  - `.schema`
  - `.quit`
  - `.headers on` (Formats SQL output - output the name of each column)
  - `.mode column` (Formats SQL output - now we are in column mode, enabling us to run .width commands)
  - `.width auto` (Formats SQL output - adjusts and normalizes column width)
- SQLite Data Types
  - `INTEGER`
  - `REAL`
  - `TEXT`
  - `NULL`
- Writing SQL statements to a File
  - Execute the code from the file in the terminal `sqlite3 example.db < example.sql`
- CRUD Operations in SQL
  - INSERT: `INSERT INTO table_name (column2, column3, column4) VALUES ('value1', 2, 'value3');`
  - SELECT (all rows and all columns): `SELECT * FROM table_name;`
  - SELECT (all rows and only column2 and column3): `SELECT column2, column3 FROM table_name;`
  - SELECT with WHERE (=): `SELECT * FROM table_name WHERE column2 = "value1";`
  - SELECT with WHERE value (<): `SELECT * FROM table_name WHERE column3 < 7;`
  - UPDATE: `UPDATE table_name SET column2 = "another value" WHERE column2 = "value1";`
  - DELETE: `DELETE FROM table_name WHERE id = 1;`
- Other SQL Queries
  - ORDER BY: `SELECT * FROM table_name ORDER BY column3;`
  - ORDER BY with DESC: `SELECT * FROM table_name ORDER BY column3 DESC;`
  - ORDER BY with LIMIT: `SELECT * FROM table_name ORDER BY column3 DESC LIMIT 1;`
  - BETWEEN: `SELECT * FROM table_name WHERE column3 BETWEEN 2 AND 4;`
- SQL Aggregate function (COUNT): `SELECT COUNT(column3) FROM table_name WHERE column3 = 2;`
- Primary Keys
- Foreign Keys: `reviews.hotel_id`, `reviews.customer_id`
- SQL Joins: `SELECT * FROM hotels INNER JOIN reviews ON hotels.id = reviews.hotel_id`
- Creating Join Tables

## Introduction

In today's lecture, we will discuss the SQL Fundamentals & Table Relations between tables in a relational database that we will build and interact with using SQL code.

## Setup

1. Run `sqlite3 hotel_reviews.db` in your terminal to enter the sqlite3 environment and begin writing SQL code to create tables and rows in the hotel_reviews database.

## Deliverables

1. In the `sql_code_files` directory (folder), there is a file named `create_tables_if_not_exists.sql`. Inside of this file, write SQL statements using `CREATE TABLE IF NOT EXISTS` to create the following tables:
   - A table named `hotels` with 2 columns:
     - `id` with the `INTEGER` datatype and should be a `PRIMARY KEY`.
     - `name` with the `TEXT` datatype.
   - A table named `customers` with 3 columns:
     - `id` with the `INTEGER` datatype and should be a `PRIMARY KEY`.
     - `first_name` with the `TEXT` datatype.
     - `last_name` with the `TEXT` datatype.
   - A table named `reviews` with 5 columns:
     - `id` with the `INTEGER` datatype and should be a `PRIMARY KEY`.
     - `rating` with the `INTEGER` datatype.
     - `text` with the `TEXT` datatype.
     - `hotel_id` with the `INTEGER` datatype.
     - `customer_id` with the `INTEGER` datatype.

Note: You can run `sqlite3 hotel_reviews.db < sql_code_files/create_tables_if_not_exists.sql` to run your SQL code from the `create_tables_if_not_exists.sql` to make changes to the `hotel_reviews.db` database file.

2. In the `sql_code_files` directory (folder), there is a file named `drop_tables_if_exists.sql`. Inside of this file, write SQL statements using `DROP TABLE IF EXISTS` to drop the `hotels`, `customers`, and `reviews` tables.

Note: You can run `sqlite3 hotel_reviews.db < sql_code_files/drop_tables_if_exists.sql` to run your SQL code from the `drop_tables_if_exists.sql` to make changes to the `hotel_reviews.db` database file. When successfully executed, the code for Deliverable # 2 will drop the tables from the `hotel_reviews.db` database, so make sure to run `sqlite3 hotel_reviews.db < sql_code_files/create_tables_if_not_exists.sql` to run your code to create the tables again before moving on to Deliverable # 3.

3. In the `sql_code_files` directory (folder), there is a file named `insert_into_tables.sql`. Inside of this file, write SQL statements using `INSERT INTO` to insert (create) the following rows:
   - A row in the `hotels` table with the `name` "Marriott".
   - A row in the `customers` table with the `first_name` of "Alice" and `last_name` of "Baker".
   - A row in the `reviews` table with a `rating` of 5, `text` that says "Best hotel ever!", a `hotel_id` of 1, and a `customer_id` of 1.

Note: You can run `sqlite3 hotel_reviews.db < sql_code_files/insert_into_tables.sql` to run your SQL code from the `insert_into_tables.sql` to make changes to the `hotel_reviews.db` database file.

4. In the `sql_code_files` directory (folder), there is a file named `delete_before_insert.sql`. Inside of this file, write SQL statements using `DELETE FROM` to delete all rows from the `hotels`, `customers`, and `reviews` tables. Then, write SQL statements using `INSERT INTO` to insert (create) the following rows:
   - A row in the `hotels` table with the `name` "Marriott".
   - A row in the `hotels` table with the `name` "Hampton Inn".
   - A row in the `hotels` table with the `name` "Flatiron Resort".
   - A row in the `customers` table with the `first_name` of "Alice" and `last_name` of "Baker".
   - A row in the `customers` table with the `first_name` of "Bob" and `last_name` of "Carter".
   - A row in the `customers` table with the `first_name` of "Chris" and `last_name` of "Dawson".
   - A row in the `reviews` table with a `rating` of 5, `text` that says "Best hotel ever!", a `hotel_id` of 1, and a `customer_id` of 1.
   - A row in the `reviews` table with a `rating` of 4, `text` that says "Great hotel!", a `hotel_id` of 1, and a `customer_id` of 2.
   - A row in the `reviews` table with a `rating` of 5, `text` that says "Flatiron Resort is the best vacation spot ever!", a `hotel_id` of 3, and `customer_id` of 3.
   - A row in the `reviews` table with a `rating` of 4, `text` that says "Great hotel!", a `hotel_id` of 2, and a `customer_id` of 2.
   - A row in the `reviews` table with a `rating` of 3, `text` that says "Not as good as the first time I visited.", a `hotel_id` of 1, and a `customer_id` of 1.

Note: You can run `sqlite3 hotel_reviews.db < sql_code_files/delete_before_insert.sql` to run your SQL code from the `delete_before_insert.sql` to make changes to the `hotel_reviews.db` database file.

5. In the `sql_code_files` directory (folder), there is a file named `update_hotel_name.sql`. Inside of this file, write an SQL statement using `UPDATE` to update the hotel name(s) from "Marriott" to "Hilton Resort" for rows in the `hotels` table that currently have the name "Marriott".

Note: You can run `sqlite3 hotel_reviews.db < sql_code_files/update_hotel_name.sql` to run your SQL code from the `update_hotel_name.sql` to make changes to the `hotel_reviews.db` database file.

6. In the `sql_code_files` directory (folder), there is a file named `select_reviews_from_first_hotel.sql`. Inside of this file, `.mode column` has been included on line 1 to output the name of each column and adjust and normalize the column width. Write your SQL statement inside of the `select_reviews_from_first_hotel.sql` starting after line 1 to retrieve data for the reviews that belong to the first hotel (the hotel row with the `id` of 1). You can access data for the hotel that a review belongs to from the `reviews` table foreign key of `hotel_id`. You will need to use `SELECT`, `FROM`, `INNER JOIN`, `ON`, and `WHERE` appropriately in your solution. You should only `SELECT` the columns from the `reviews` table, so that the output in the terminal shows data only from the `reviews` table.

Note: You can run `sqlite3 hotel_reviews.db < sql_code_files/select_reviews_from_first_hotel.sql` to run your SQL code from the `select_reviews_from_first_hotel.sql` to make changes to the `hotel_reviews.db` database file.

7. In the `sql_code_files` directory (folder), there is a file named `select_customers_from_first_hotel.sql`. Inside of this file, `.mode column` has been included on line 1 to output the name of each column and adjust and normalize the column width. Write your SQL statement inside of the `select_customers_from_first_hotel.sql` starting after line 1 to retrieve data for the customers that left reviews for the first hotel (the hotel row with the `id` of 1). The `reviews` table is the `join table`. You can access data for the customer that a review belongs to from the `reviews` table foreign key of `customer_id`. You will need to use `SELECT`, `FROM`, `INNER JOIN`, `ON`, and `WHERE` appropriately in your solution. You should only `SELECT` the columns from the `customers` table, so that the output in the terminal shows data only from the `customers` table. Use `GROUP BY` to remove duplicate output.

Note: You can run `sqlite3 hotel_reviews.db < sql_code_files/select_customers_from_first_hotel.sql` to run your SQL code from the `select_customers_from_first_hotel.sql` to make changes to the `hotel_reviews.db` database file.