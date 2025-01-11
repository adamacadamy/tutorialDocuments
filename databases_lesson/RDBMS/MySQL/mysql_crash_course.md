### **Complete MySQL Crash Course**
![alt text](../images/mysql_dark_logo.png)

---
 

## **1. Basics of MySQL**

### **Connecting to MySQL**
Open your MySQL client or use the terminal:
```bash
docker exec -it mysql bash
mysql -u root -p
```
Replace `root` with your username and enter the password when prompted.

### **Selecting a Database**
```sql
USE database_name;
```

### **Show All Databases**
```sql
SHOW DATABASES;
```

---

## **2. Database and Table Management**

### **Create a Database**
```sql
CREATE DATABASE my_database;
```

#### Result:
```bash
SHOW DATABASES;
```
| Database         |
|------------------|
| information_schema |
| my_database      |

---

### **Create a Table**
```sql
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date DATE
);
```

#### Result:
```sql
SHOW TABLES IN my_database;
```
| Tables_in_my_database |
|------------------------|
| employees             |

---

### **Insert Data into a Table**
```sql
INSERT INTO employees (name, department, salary, hire_date)
VALUES
('Alice', 'HR', 50000, '2023-01-15'),
('Bob', 'IT', 60000, '2023-03-20'),
('Charlie', 'Finance', 55000, '2023-06-10');
```

#### Result:
```sql
SELECT * FROM employees;
```
| id  | name      | department | salary  | hire_date  |
|-----|-----------|------------|---------|------------|
| 1   | Alice     | HR         | 50000.00 | 2023-01-15 |
| 2   | Bob       | IT         | 60000.00 | 2023-03-20 |
| 3   | Charlie   | Finance    | 55000.00 | 2023-06-10 |

---

### **Show Tables**
```sql
SHOW TABLES;
```

#### Result:
| Tables_in_my_database |
|------------------------|
| employees             |

---

### **Describe a Table**
```sql
DESCRIBE employees;
```

#### Result:
| Field      | Type          | Null | Key | Default | Extra          |
|------------|---------------|------|-----|---------|----------------|
| id         | int           | NO   | PRI | NULL    | auto_increment |
| name       | varchar(100)  | YES  |     | NULL    |                |
| department | varchar(50)   | YES  |     | NULL    |                |
| salary     | decimal(10,2) | YES  |     | NULL    |                |
| hire_date  | date          | YES  |     | NULL    |                |

---

### **Create a View**
A **view** is a virtual table based on the result set of a query.  

#### Create a View:
```sql
CREATE VIEW high_salary_employees AS
SELECT name, salary, department
FROM employees
WHERE salary > 55000;
```

#### Query the View:
```sql
SELECT * FROM high_salary_employees;
```

#### Result:
| name | salary  | department |
|------|---------|------------|
| Bob  | 60000.00 | IT         |

---

### **Drop a View**
```sql
DROP VIEW high_salary_employees;
```

---

### **Drop a Table or Database**
#### Drop a Table:
```sql
DROP TABLE employees;
```

#### Drop a Database:
```sql
DROP DATABASE my_database;
```

---

## **3. Basic CRUD Operations**

### **Insert Data**
```sql
INSERT INTO employees (name, department, salary, hire_date)
VALUES ('Alice', 'HR', 50000, '2023-01-15');
```

### **Select Data**
```sql
SELECT * FROM employees;
```

### **Update Data**
```sql
UPDATE employees
SET salary = 55000
WHERE name = 'Alice';
```

### **Delete Data**
```sql
DELETE FROM employees
WHERE name = 'Alice';
```

---

## **4. Querying Data**

### **Filtering**
```sql
SELECT * FROM employees WHERE department = 'HR';
```

### **Sorting**
```sql
SELECT * FROM employees ORDER BY salary DESC;
```

### **Limiting Results**
```sql
SELECT * FROM employees LIMIT 5;
```

### **Using Aliases**
```sql
SELECT name AS EmployeeName, salary AS EmployeeSalary FROM employees;
```

---

## **5. Aggregate Functions**

### **Count**
```sql
SELECT COUNT(*) AS total_employees FROM employees;
```

### **Average**
```sql
SELECT AVG(salary) AS average_salary FROM employees;
```

### **Sum**
```sql
SELECT SUM(salary) AS total_salaries FROM employees;
```

### **Group By**
```sql
SELECT department, COUNT(*) AS num_employees
FROM employees
GROUP BY department;
```

---

## **6. Joins in SQL**

### **Sample Tables**
#### employees Table
| id  | name      | department_id |
|-----|-----------|---------------|
| 1   | Alice     | 101           |
| 2   | Bob       | 102           |
| 3   | Charlie   | NULL          |

```sql
-- Create the departments table
CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

-- Insert data into the departments table
INSERT INTO departments (id, name) VALUES
(101, 'HR'),
(102, 'IT'),
(103, 'Finance');

```

#### departments Table
| id  | name         |
|-----|-------------|
| 101 | HR          |
| 102 | IT          |
| 103 | Finance     |

```sql 
-- Create the employees table
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

-- Insert data into the employees table
INSERT INTO employees (id, name, department_id) VALUES
(1, 'Alice', 101),
(2, 'Bob', 102),
(3, 'Charlie', 103);
```
---

### **INNER JOIN**
```sql
SELECT employees.name, departments.name AS department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.id;
```

| employees.name | employees.department_id | departments.id | departments.name |
|----------------|-------------------------|----------------|------------------|
| Alice          | 101                     | 101            | HR               |
| Bob            | 102                     | 102            | IT               |

Result:
| name  | department_name |
|-------|-----------------|
| Alice | HR              |
| Bob   | IT              |

---

### **LEFT JOIN**
```sql
SELECT employees.name, departments.name AS department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.id;
```

| employees.name | employees.department_id | departments.id | departments.name |
|----------------|-------------------------|----------------|------------------|
| Alice          | 101                     | 101            | HR               |
| Bob            | 102                     | 102            | IT               |
| Charlie        | NULL                    | NULL           | NULL             |

Result:
| name      | department_name |
|-----------|-----------------|
| Alice     | HR              |
| Bob       | IT              |
| Charlie   | NULL            |

---

### **RIGHT JOIN**
```sql
SELECT employees.name, departments.name AS department_name
FROM employees
RIGHT JOIN departments ON employees.department_id = departments.id;
```

| employees.name | employees.department_id | departments.id | departments.name |
|----------------|-------------------------|----------------|------------------|
| Alice          | 101                     | 101            | HR               |
| Bob            | 102                     | 102            | IT               |
| NULL           | NULL                    | 103            | Finance          |

Result:
| name  | department_name |
|-------|-----------------|
| Alice | HR              |
| Bob   | IT              |
| NULL  | Finance         |

---

### **FULL OUTER JOIN**
```sql
SELECT employees.name, departments.name AS department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.id
UNION
SELECT employees.name, departments.name AS department_name
FROM employees
RIGHT JOIN departments ON employees.department_id = departments.id;
```

| employees.name | employees.department_id | departments.id | departments.name |
|----------------|-------------------------|----------------|------------------|
| Alice          | 101                     | 101            | HR               |
| Bob            | 102                     | 102            | IT               |
| Charlie        | NULL                    | NULL           | NULL             |
| NULL           | NULL                    | 103            | Finance          |

Result:
| name      | department_name |
|-----------|-----------------|
| Alice     | HR              |
| Bob       | IT              |
| Charlie   | NULL            |
| NULL      | Finance         |

---

### **CROSS JOIN**
```sql
SELECT employees.name, departments.name AS department_name
FROM employees
CROSS JOIN departments;
```

| employees.name | departments.name |
|----------------|------------------|
| Alice          | HR               |
| Bob            | IT               |
| Charlie        | Finance          |

---
 