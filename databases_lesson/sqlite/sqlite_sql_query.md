
# Comprehensive Lesson: SQL with SQLite Using VS Code

This lesson covers SQL concepts using **SQLite** and provides a guide for setting up **Visual Studio Code (VS Code)** to write, run, and manage SQLite queries effectively.

## Lesson Outline

1. **Introduction to SQLite**
2. **Setting Up VS Code for SQLite Development**
3. **Basic SQLite Commands**
4. **Data Definition Language (DDL)**
5. **Data Types in SQLite**
6. **Data Manipulation Language (DML)**
7. **Filtering Data (`WHERE` clause)**
8. **Sorting Data (`ORDER BY` clause)**
9. **Aggregating Data (`GROUP BY`, `HAVING` clauses)**
10. **Joining Tables (`INNER JOIN`, `LEFT JOIN`, etc.)**
11. **Subqueries and Nested Queries**
12. **Views in SQLite**
13. **SQLite Functions**
14. **Indexes and Performance Optimization**
15. **Practical Examples and Exercises**

---

## 1. Introduction to SQLite

SQLite is a lightweight, serverless SQL database engine. It is self-contained, requires no configuration, and stores data in a single file.

Start SQLite in your terminal:

```bash
sqlite3 mydatabase.db
```

### Basic Commands

- `.tables`: List all tables.
- `.schema <table_name>`: Display the schema of a table.
- `.exit`: Exit the SQLite shell.

---

## 2. Setting Up VS Code for SQLite Development

### Required Extensions

1. **SQLite** by Alex Covizzi
2. **SQLTools** by Matheus Teixeira
3. **SQLTools SQLite Driver**

### Installation

1. Open **VS Code** and go to the Extensions view (`Ctrl + Shift + X`).
2. Search and install the following:
   - **SQLite**
   - **SQLTools**
   - **SQLTools SQLite Driver**
3. Open the Command Palette (`Ctrl + Shift + P`) and type **"SQLite: Open Database"** to connect your database (e.g., `mydatabase.db`).

---

## 3. Basic SQLite Commands

### Example Database

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
);

INSERT INTO students (name, age, grade) VALUES ('Alice', 20, 'A'), ('Bob', 22, 'B');
```

- `SELECT * FROM students;`: Retrieves all records from the `students` table.
- `DROP TABLE students;`: Deletes the table.

---

## 4. Data Definition Language (DDL)

### Creating Tables

```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT,
    price REAL
);
```

### Altering Tables

```sql
ALTER TABLE products ADD COLUMN stock INTEGER DEFAULT 0;
```

### Dropping Tables

```sql
DROP TABLE IF EXISTS products;
```

---

## 5. Data Types in SQLite

SQLite supports:

- **INTEGER**: Whole numbers
- **REAL**: Floating-point numbers
- **TEXT**: Strings
- **BLOB**: Binary data
- **NULL**: No value

---

## 6. Data Manipulation Language (DML)

### Inserting Data

```sql
INSERT INTO products (name, category, price, stock) VALUES ('Laptop', 'Electronics', 1200.99, 10);
```

### Selecting Data

```sql
SELECT name, price FROM products;
```

### Updating Data

```sql
UPDATE products SET stock = 15 WHERE name = 'Laptop';
```

### Deleting Data

```sql
DELETE FROM products WHERE stock = 0;
```

---

## 7. Filtering Data (`WHERE` clause)

```sql
SELECT * FROM products WHERE price > 500 AND category = 'Electronics';
```

---

## 8. Sorting Data (`ORDER BY` clause)

```sql
SELECT * FROM products ORDER BY price DESC;
```

---

## 9. Aggregating Data (`GROUP BY`, `HAVING` clauses)

```sql
SELECT category, AVG(price) as average_price
FROM products
GROUP BY category
HAVING AVG(price) > 100;
```

---

## 10. Joining Tables

### Sample Tables

```sql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

INSERT INTO orders (product_id, quantity) VALUES (1, 5);
```

### Inner Join

```sql
SELECT products.name, orders.quantity
FROM products
INNER JOIN orders ON products.id = orders.product_id;
```

### Left Join

```sql
SELECT products.name, orders.quantity
FROM products
LEFT JOIN orders ON products.id = orders.product_id;
```

---

## 11. Subqueries and Nested Queries

```sql
SELECT name FROM products WHERE price > (SELECT AVG(price) FROM products);
```

---

## 12. Views in SQLite

Views are virtual tables defined by queries.

### Creating a View

```sql
CREATE VIEW expensive_products AS
SELECT name, price FROM products WHERE price > 1000;
```

### Using a View

```sql
SELECT * FROM expensive_products;
```

### Dropping a View

```sql
DROP VIEW IF EXISTS expensive_products;
```

---

## 13. SQLite Functions

- `COUNT()`: Counts rows
- `SUM()`: Calculates total
- `AVG()`: Computes average
- `MIN()` / `MAX()`: Finds minimum/maximum values

### Examples

```sql
SELECT COUNT(*) FROM products;
SELECT SUM(stock) FROM products;
SELECT AVG(price) FROM products;
```

---

## 14. Indexes and Performance Optimization

### Creating an Index

```sql
CREATE INDEX idx_product_name ON products (name);
```

### Dropping an Index

```sql
DROP INDEX idx_product_name;
```

---

## 15. Practical Examples and Exercises

### Exercise 1: Movie Database

1. Create `movies` and `reviews` tables.
2. Insert sample data.
3. Write a query to get the average rating for each movie.

**Solution:**

```sql
CREATE TABLE movies (
    movie_id INTEGER PRIMARY KEY,
    title TEXT,
    director TEXT
);

CREATE TABLE reviews (
    review_id INTEGER PRIMARY KEY,
    movie_id INTEGER,
    rating REAL,
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);

INSERT INTO movies (title, director) VALUES ('Inception', 'Nolan'), ('Matrix', 'Wachowskis');
INSERT INTO reviews (movie_id, rating) VALUES (1, 5.0), (1, 4.5), (2, 4.0);

SELECT movies.title, AVG(reviews.rating) as average_rating
FROM movies
INNER JOIN reviews ON movies.movie_id = reviews.movie_id
GROUP BY movies.title;
```

---

### Using VS Code to Run Your Queries

1. Write your queries in a file (e.g., `queries.sql`).
2. Use the **SQLTools** extension (`F5` or `Ctrl + Enter`) to execute the query.
3. View results in the integrated **SQLite Explorer** panel.

### Tips

- Use **IntelliSense** for auto-complete in SQL files.
- Format queries with **Prettier** (`Shift + Alt + F`).
- Create snippets for frequently used queries in VS Code.

---

This lesson provides a complete guide to using SQLite with VS Code effectively. Practice the exercises to deepen your understanding.
