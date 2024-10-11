
# SQLite Tutorial from Beginner to Advanced

### 1. Introduction to RDBMS and SQLite

#### What is an RDBMS?
- **Definition**: A Relational Database Management System (RDBMS) is a software that uses a relational model to manage data.
- **Basic Concepts**: Tables, rows (records), columns (fields), primary keys, and foreign keys.
- **SQL (Structured Query Language)**: The language used to interact with RDBMS.

#### Why SQLite?
- **Lightweight, serverless, and self-contained**.
- **Ideal for embedded systems, desktop applications, and rapid prototyping**.
- **Popular in mobile development** (e.g., Android, iOS).

#### SQLite Use Cases
- **Rapid development**: Useful for testing and prototyping.
- **Small to medium-sized databases**: Suitable for single-user applications.
- **Embedded databases**: Ideal for IoT devices and small software applications.

### 2. Setting Up SQLite in VSCode

#### Installing SQLite
- [Download SQLite](https://www.sqlite.org/download.html) for your OS.
- Verify installation: `sqlite3 --version`.

#### Recommended VSCode Extensions
1. **SQLite** ([SQLite extension for VSCode](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite)).
2. **SQLTools** ([SQLTools extension for VSCode](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools)).
3. **SQLTools SQLite Driver** ([SQLTools SQLite Driver](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools-sqlite)).

#### Configure SQLTools for SQLite
1. Open the Command Palette (`Ctrl+Shift+P`).
2. Type "SQLTools: Add New Connection" and select it.
3. Choose "SQLite" as the driver and select the SQLite database file.
4. Save the configuration.

### 3. Basic SQLite Operations

#### Data Definition Language (DDL)

1. **Creating a Database**
   - SQLite creates a database file automatically:
     ```bash
     sqlite3 my_database.db
     ```

2. **Create a Table**
   ```sql
   CREATE TABLE students (
       student_id INTEGER PRIMARY KEY,
       name TEXT NOT NULL,
       age INTEGER,
       enrollment_date TEXT DEFAULT CURRENT_DATE
   );
   ```
   - **Explanation**: Creates a `students` table with columns for `student_id`, `name`, `age`, and `enrollment_date`.

3. **Alter a Table**
   ```sql
   ALTER TABLE students ADD COLUMN email TEXT;
   ```
   - **Explanation**: Adds an `email` column to the `students` table.

4. **Drop a Table**
   ```sql
   DROP TABLE IF EXISTS students;
   ```
   - **Explanation**: Deletes the `students` table.

#### Data Manipulation Language (DML)

1. **Inserting Data**
   ```sql
   INSERT INTO students (name, age, email) VALUES ('Alice', 22, 'alice@example.com');
   INSERT INTO students (name, age) VALUES ('Bob', 25);
   ```
   - **Explanation**: Inserts records into the `students` table.

2. **Selecting Data**
   ```sql
   SELECT * FROM students;
   SELECT name, age FROM students WHERE age > 20;
   ```
   - **Explanation**: Retrieves all or specific records based on conditions.

3. **Updating Data**
   ```sql
   UPDATE students SET age = 23 WHERE name = 'Alice';
   ```
   - **Explanation**: Updates Alice's age to 23.

4. **Deleting Data**
   ```sql
   DELETE FROM students WHERE name = 'Alice';
   ```
   - **Explanation**: Removes the record where the name is 'Alice'.

#### Data Control Language (DCL)

1. **Grant and Revoke Permissions**
   - SQLite does not support DCL commands (e.g., `GRANT`, `REVOKE`) as it is a file-based database.

#### Transaction Control Language (TCL)

1. **Using Transactions**
   ```sql
   BEGIN TRANSACTION;
   UPDATE students SET age = 24 WHERE name = 'Bob';
   COMMIT;
   ```
   - **Explanation**: Starts a transaction, performs an update, and commits the changes.

2. **Rollback a Transaction**
   ```sql
   BEGIN TRANSACTION;
   DELETE FROM students WHERE name = 'Bob';
   ROLLBACK;
   ```
   - **Explanation**: Reverts changes made during the transaction.

### 4. Intermediate SQLite Concepts

#### Indexes
1. **Creating an Index**
   ```sql
   CREATE INDEX idx_student_name ON students(name);
   ```
   - **Explanation**: Improves query performance on the `name` column.

2. **Dropping an Index**
   ```sql
   DROP INDEX IF EXISTS idx_student_name;
   ```
   - **Explanation**: Deletes the index from the database.

#### Joins
1. **Inner Join**
   ```sql
   SELECT s.name, c.course_name
   FROM students s
   INNER JOIN enrollments e ON s.student_id = e.student_id
   INNER JOIN courses c ON e.course_id = c.course_id;
   ```
   - **Explanation**: Joins the `students`, `enrollments`, and `courses` tables.

2. **Left Join**
   ```sql
   SELECT s.name, c.course_name
   FROM students s
   LEFT JOIN enrollments e ON s.student_id = e.student_id
   LEFT JOIN courses c ON e.course_id = c.course_id;
   ```
   - **Explanation**: Returns all students, even if they aren't enrolled in any courses.

#### Views
1. **Create a View**
   ```sql
   CREATE VIEW adult_students AS
   SELECT name, age FROM students WHERE age >= 18;
   ```
   - **Explanation**: Creates a view for students aged 18 or older.

#### Common Table Expressions (CTEs)
1. **CTE Example**
   ```sql
   WITH AgeGroup AS (
       SELECT name, age FROM students WHERE age > 21
   )
   SELECT * FROM AgeGroup;
   ```
   - **Explanation**: Creates a temporary result set for use in the main query.

### 5. Advanced SQLite Concepts

#### Triggers
1. **Create a Trigger**
   ```sql
   CREATE TRIGGER validate_age
   BEFORE INSERT ON students
   FOR EACH ROW
   BEGIN
       SELECT CASE
           WHEN NEW.age < 0 THEN
               RAISE (ABORT, 'Age must be a positive number')
       END;
   END;
   ```
   - **Explanation**: Prevents inserting negative ages.

#### Recursive Queries
1. **Recursive CTE Example**
   ```sql
   WITH RECURSIVE numbers(x) AS (
       VALUES(1)
       UNION ALL
       SELECT x+1 FROM numbers WHERE x < 10
   )
   SELECT * FROM numbers;
   ```
   - **Explanation**: Generates numbers from 1 to 10.

#### Using JSON in SQLite
1. **Create a Table with JSON Data**
   ```sql
   CREATE TABLE config (data JSON);
   INSERT INTO config (data) VALUES ('{"key": "value"}');

   SELECT json_extract(data, '$.key') FROM config;
   ```
   - **Explanation**: Demonstrates handling JSON data in SQLite.

### 6. Integrating SQLite with Applications

#### Using SQLite in Python
1. **Basic Python Script**
   ```python
   import sqlite3

   conn = sqlite3.connect('my_database.db')
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM students")
   rows = cursor.fetchall()

   for row in rows:
       print(row)

   conn.close()
   ```
   - **Explanation**: Connects to SQLite and prints all student records.

#### Using SQLite in JavaScript
1. **Node.js Example with `better-sqlite3`**
   ```javascript
   const Database = require('better-sqlite3');
   const db = new Database('my_database.db');

   const rows = db.prepare('SELECT * FROM students').all();
   console.log(rows);
   ```
   - **Explanation**: Fetches all student records using Node.js.

### 7. Backup, Restore, and Optimization

#### Backup and Restore
1. **Backup**
   ```bash
   sqlite3 my_database.db ".backup 'backup_file.db'"
   ```
2. **Restore**
   ```bash
   sqlite3 backup_file.db ".restore 'my_database.db'"
   ```

#### Optimization
1. **Run `VACUUM`**
   ```sql
   VACUUM;
   ```
   - **Explanation**: Reclaims free space and reduces file size.

2. **Analyze Database**
   ```sql
   ANALYZE;
   ```
   - **Explanation**: Collects statistics to improve query performance.
