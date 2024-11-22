
# Using Jupyter Notebook for PostgreSQL Queries

You can use Jupyter Notebook with the `psycopg2` library or the `ipython-sql` extension to write and execute PostgreSQL queries interactively.

---

## **Setup**

### 1. Install the necessary packages:
   ```bash
   pip install jupyter ipython-sql psycopg2-binary sqlalchemy
   ```

### 2. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

### 3. Enable the SQL extension in your Jupyter Notebook:
   ```python
   %load_ext sql
   ```

### 4. Connect to a PostgreSQL database:
   Replace `<username>`, `<password>`, `<host>`, `<port>`, and `<database>` with your database details:
   ```python
   %sql postgresql://<username>:<password>@<host>:<port>/<database>
   ```
   Example:
   ```python
   %sql postgresql://postgres:password@localhost:5432/mydatabase
   ```

---

## **Example: Creating and Querying a Table**

### 1. Create a sample table and insert data:
   ```sql
   %%sql
   CREATE TABLE users (
       id SERIAL PRIMARY KEY,
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
- Ensure you have the correct connection details (`username`, `password`, `host`, `port`, `database`) when connecting to your PostgreSQL server.

This setup allows you to interactively run and test PostgreSQL queries directly in the Jupyter Notebook interface.
