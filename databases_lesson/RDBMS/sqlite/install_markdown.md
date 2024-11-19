
# **Setting Up SQLite on Windows**

## **Step 1: Download SQLite**

1. Visit the official SQLite download page:  
   [SQLite Download Page](https://www.sqlite.org/download.html)

2. Under the **Precompiled Binaries for Windows** section, download:
   - `sqlite-tools-win32-x86-x.x.x.zip`

3. Extract the ZIP file to a directory, e.g., `C:\Users\atew\sqlite`.

---

## **Step 2: Add SQLite to the System Environment Variables**

### **Using PowerShell**

1. **Run PowerShell as Administrator**
   - Search for **PowerShell** in the Start menu, right-click, and select **Run as Administrator**.

2. **Add SQLite to the System `PATH` Variable**

   Run the following commands:

   ```powershell
   # Get the current PATH variable
   $currentPath = [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::Machine)

   # Add SQLite directory to PATH
   $newPath = $currentPath + ";C:\Users\atew\sqlite"
   [System.Environment]::SetEnvironmentVariable("Path", $newPath, [System.EnvironmentVariableTarget]::Machine)
   ```

3. **Verify the Update**

   Run the following to confirm the `PATH` includes SQLite:
   ```powershell
   [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::Machine)
   ```

4. **Refresh Environment Variables**

   Reload the updated `PATH` variable in the current session:
   ```powershell
   $env:Path = [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::Machine)
   ```

---

### **Using the GUI**

1. **Open System Properties**
   - Press `Win + R`, type `sysdm.cpl`, and press Enter.

2. **Access Environment Variables**
   - In the **System Properties** window, go to the **Advanced** tab.
   - Click **Environment Variables**.

3. **Edit the System `PATH` Variable**
   - Under **System variables**, find and select `Path`, then click **Edit**.
   - Click **New**, and add:
     ```
     C:\Users\atew\sqlite
     ```
   - Click **OK** to save.

4. **Restart Command Prompt**
   - Close and reopen Command Prompt or PowerShell to load the updated `PATH`.

---

## **Step 3: Verify SQLite Installation**

1. Open a new Command Prompt or PowerShell window.
2. Type:
   ```cmd
   sqlite3
   ```
3. You should see the SQLite shell:
   ```
   SQLite version 3.x.x 2024-xx-xx xx:xx:xx
   Enter ".help" for usage hints.
   sqlite>
   ```

---

## **Step 4: Test SQLite Commands**

- To create a database or open an existing one:
  ```cmd
  sqlite3 my_database.db
  ```

- To list all tables in the database:
  ```sql
  .tables
  ```

- To exit SQLite:
  ```sql
  .exit
  ```

---

## **Useful Resources**

- [SQLite Official Documentation](https://www.sqlite.org/docs.html)
- [SQLite Command Line Documentation](https://www.sqlite.org/cli.html)

--- 

This guide ensures that SQLite is properly set up and accessible from any terminal on your Windows system.
