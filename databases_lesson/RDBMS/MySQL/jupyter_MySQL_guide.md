
# Using Jupyter Notebook for MySQL Queries

You can use Jupyter Notebook with the `mysql-connector-python` library or the `ipython-sql` extension to write and execute MySQL queries interactively.

---

## **Setup**

### 1. Install the necessary packages:
   ```bash
   pip install jupyter ipython-sql mysql-connector-python  sqlalchemy pymysql prettytable
   ```

### 2. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

### 3. Enable the SQL extension in your Jupyter Notebook:
   ```python
   %load_ext sql
   ```

### 4. Connect to a MySQL database:
   Replace `<username>`, `<password>`, `<host>`, and `<database>` with your database details:
   ```python
   %sql mysql+pymysql://<username>:<password>@<host>/<database>
   ```
   Example:
   ```python
   %sql mysql+pymysql://root:password@localhost/mydatabase
   ```

---

## **Example: Creating and Querying a Table**

### 1. Create a sample table and insert data:
   ```sql
   %%sql
   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(100),
       age INT
   );

   INSERT INTO users (name, age) VALUES
   ('Alice', 30),
   ('Bob', 25),
   ('Charlie', 35);
   ```

### 2. Query the table:
   ```sql
   %%sql
   SELECT * FROM users;
   ```

### 3. Perform a simple analysis (e.g., average age):
   ```sql
   %%sql
   SELECT AVG(age) AS average_age FROM users;
   ```

---

## **Notes**
- The `%%sql` cell magic allows you to write entire cells in SQL.
- The `%sql` line magic allows you to run a single line of SQL code.
- Ensure you have the correct connection details (`username`, `password`, `host`, `database`) when connecting to your MySQL server.

This setup allows you to interactively run and test MySQL queries directly in the Jupyter Notebook interface.
