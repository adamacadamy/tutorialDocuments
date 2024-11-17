
# SQLite Tutorial

## 1. **Lesson: Understanding RDBMS**

### 1.1 **What is an RDBMS?**

A **Relational Database Management System (RDBMS)** is software designed to manage data using the relational model. It organizes data into **tables** (relations), consisting of rows and columns. Each table represents a specific entity, and relationships can be established between tables using keys.

### 1.2 **Key Features of RDBMS**

1. **Tables**: The main structure for storing data.
2. **Primary Key**: Unique identifier for each row.
3. **Foreign Key**: Establishes relationships between tables.
4. **SQL**: Language used for interacting with the database.
5. **ACID Compliance**:
   - **Atomicity**: All-or-nothing transactions.
   - **Consistency**: Maintains valid database state.
   - **Isolation**: Transactions do not interfere with each other.
   - **Durability**: Ensures changes are permanent.

---

## 2. **Introduction to SQLite**

SQLite is a lightweight, serverless RDBMS that stores data in a single file. It is an excellent choice for local data storage and development.

### **Why Use SQLite?**

- **Ease of Use**: No setup needed.
- **Portability**: Entire database in a single file.
- **Lightweight**: Minimal resource usage.
- **Cross-Platform**: Works on all major OS.

---

## 3. **Installation of SQLite**

### 3.1 **Installation on Windows (Detailed Steps)**

1. **Download SQLite:**
   - Go to the [official SQLite download page](https://www.sqlite.org/download.html).
   - Under the **Precompiled Binaries for Windows** section, download **sqlite-tools-win32-x86-*.zip**.

2. **Extract the `.zip` File:**
   - Locate the downloaded `.zip` file (e.g., `sqlite-tools-win32-x86-*.zip`).
   - Right-click on the file and select **Extract All...**.
   - Choose a location to extract the files (e.g., `C:\sqlite`).

3. **Add SQLite to the System PATH:**

   - Open the **Start Menu** and search for **Environment Variables**.
   - Click on **Edit the system environment variables**.
   - In the **System Properties** window, click on the **Environment Variables** button.
   - In the **System Variables** section, find the variable named **Path** and click **Edit**.
   - Click **New** and add the folder path where you extracted SQLite (e.g., `C:\sqlite`).
   - Click **OK** to save the changes.

4. **Verify the Installation:**

   Open **Command Prompt** (`cmd`) or **PowerShell** and type:

   ```shell
   sqlite3 --version
   ```

   You should see the version of SQLite displayed, indicating that it has been successfully added to your system `PATH`.

### 3.2 **Installation on macOS**

```shell
brew install sqlite
```

### 3.3 **Installation on Linux (Ubuntu/Debian)**

```shell
sudo apt update
sudo apt install sqlite3
```

---

## 4. **UI Tools for SQLite**

### 4.1 **DB Browser for SQLite**

- **DB Browser for SQLite** is a free, open-source tool for working with SQLite databases.
- Download from the [official website](https://sqlitebrowser.org/).

### 4.2 **SQLiteStudio**

- **SQLiteStudio** is another free and open-source SQLite GUI tool.
- Download from the [official SQLiteStudio website](https://sqlitestudio.pl/).

### 4.3 **DBeaver**

- **DBeaver** supports multiple databases, including SQLite.
- Download from the [DBeaver website](https://dbeaver.io/download/).

---

## 5. **SQLite VSCode Extensions**

### 5.1 **SQLite Viewer**

- Provides a tree view of the database structure and allows executing SQL queries.
- Install via VSCode Extensions Marketplace.

### 5.2 **SQLite (by alexcvzz)**

- Offers an integrated query editor and result viewer.
- Install via VSCode Extensions Marketplace.

---

## 6. **Basic SQLite Commands**

```shell
sqlite3 my_database.db
```

```sql
CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT);
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
SELECT * FROM users;
```

---

## 7. **Using SQLite with Python**

```python
import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL)')
cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', ('Laptop', 1200.00))
conn.commit()
rows = cursor.execute('SELECT * FROM products').fetchall()
print(rows)
conn.close()
```

---

## 8. **Backup and Restore**

### **Backup:**

```shell
cp my_database.db my_database_backup.db
```

### **Restore:**

```shell
cp my_database_backup.db my_database.db
```

---

## 9. **Advantages of SQLite**

- Serverless, self-contained, and easy to use.
- Highly portable with minimal configuration.
- ACID-compliant for safe transactions.

---

## 10. **Conclusion**

SQLite is an excellent choice for lightweight database needs. It is ideal for local storage in applications and is easy to integrate with programming languages like Python.

---

## 11. **Additional Resources**

- [Official SQLite Documentation](https://www.sqlite.org/docs.html)
- [DB Browser for SQLite](https://sqlitebrowser.org/)
- [SQLiteStudio](https://sqlitestudio.pl/)
- [DBeaver](https://dbeaver.io/)
- [VSCode SQLite Viewer Extension](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer)
- [VSCode SQLite by alexcvzz Extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite)

