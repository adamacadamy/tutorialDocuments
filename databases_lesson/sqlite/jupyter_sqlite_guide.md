
# Using Jupyter Notebook for SQLite Queries

You can use Jupyter Notebook with the `sqlite3` library or the `ipython-sql` extension to write and execute SQLite queries interactively.

## Setup
1. Install the necessary packages:
   ```bash
   pip install jupyter ipython-sql sqlite3
   ```

2. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

3. Enable the SQL extension in your Jupyter Notebook:
   ```python
   %load_ext sql
   ```

4. Connect to an SQLite database (create `example.db` if it doesn’t exist):
   ```python
   %sql sqlite:///example.db
   ```

## Example: Creating and Querying a Table
1. Create a sample table and insert data:
   ```sql
   %%sql
   CREATE TABLE users (
       id INTEGER PRIMARY KEY,
       name TEXT,
       age INTEGER
   );

   INSERT INTO users (name, age) VALUES
   ('Alice', 30),
   ('Bob', 25),
   ('Charlie', 35);
   ```

2. Query the table:
   ```sql
   %%sql
   SELECT * FROM users;
   ```

3. Perform a simple analysis (e.g., average age):
   ```sql
   %%sql
   SELECT AVG(age) as average_age FROM users;
   ```

## Notes
- The `%%sql` cell magic allows you to write entire cells in SQL.
- The `%sql` line magic allows you to run a single line of SQL code.

This setup allows you to run and test your SQLite queries directly within the Jupyter Notebook interface.
