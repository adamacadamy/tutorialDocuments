
# Linux Terminal CLI Basics for Beginners

## **1. Open the Terminal**
- **Shortcut to open the terminal:**
  - **Ubuntu:** `Ctrl + Alt + T`
  - **Mac:** Search "Terminal" in Spotlight (`Cmd + Space`) or use iTerm.
  - **Windows (via WSL):** Open "Ubuntu" or use `Win + R` -> `wsl`.

---

## **2. Navigating the File System**
- **pwd** (Print Working Directory):
  ```bash
  pwd
  ```
  Displays the current directory you're in.

- **ls** (List Files and Directories):
  ```bash
  ls
  ls -l   # Long listing format
  ls -a   # Includes hidden files
  ```

- **cd** (Change Directory):
  ```bash
  cd <directory_name>
  cd ..   # Move one directory up
  cd ~    # Move to the home directory
  cd /    # Move to the root directory
  ```

---

## **3. Working with Files**
- **touch** (Create an empty file):
  ```bash
  touch <file_name>
  ```

- **cat** (View contents of a file):
  ```bash
  cat <file_name>
  ```

- **nano** or **vim** (Edit a file):
  ```bash
  nano <file_name>  # Simple text editor
  vim <file_name>   # Advanced editor
  ```

- **cp** (Copy a file):
  ```bash
  cp <source_file> <destination_file>
  ```

- **mv** (Move or rename a file):
  ```bash
  mv <source_file> <destination_file>
  ```

- **rm** (Remove a file):
  ```bash
  rm <file_name>
  rm -r <directory_name>  # Remove a directory
  ```

---

## **4. Creating and Managing Directories**
- **mkdir** (Make Directory):
  ```bash
  mkdir <directory_name>
  mkdir -p a/b/c   # Create nested directories
  ```

- **rmdir** (Remove an empty directory):
  ```bash
  rmdir <directory_name>
  ```

---

## **5. Viewing and Searching Files**
- **less** (View file contents interactively):
  ```bash
  less <file_name>
  ```

- **grep** (Search for patterns in a file):
  ```bash
  grep "search_term" <file_name>
  grep -r "search_term" <directory_name>  # Recursive search
  ```

---

## **6. Permissions**
- **chmod** (Change file permissions):
  ```bash
  chmod 644 <file_name>  # Owner: read/write, Group: read, Others: read
  chmod +x <file_name>   # Add executable permission
  ```

- **chown** (Change file ownership):
  ```bash
  sudo chown <user>:<group> <file_name>
  ```

---

## **7. Process Management**
- **ps** (List processes):
  ```bash
  ps aux  # Detailed list of all processes
  ```

- **kill** (Terminate a process):
  ```bash
  kill <process_id>
  ```

- **top** (View running processes dynamically):
  ```bash
  top
  ```

---

## **8. System Monitoring**
- **df** (Check disk usage):
  ```bash
  df -h
  ```

- **du** (Check directory size):
  ```bash
  du -sh <directory_name>
  ```

---

## **9. Networking**
- **ping** (Check connectivity):
  ```bash
  ping <hostname_or_ip>
  ```

- **curl** (Fetch data from a URL):
  ```bash
  curl <url>
  ```

---

## **10. Using sudo for Admin Tasks**
- Prepend `sudo` to run commands as an administrator:
  ```bash
  sudo apt update
  sudo apt install <package_name>
  ```

---

## **11. Helpful Shortcuts**
- **Ctrl + C:** Cancel a running command.
- **Ctrl + Z:** Suspend a running command.
- **Ctrl + D:** Exit the terminal.
- **Tab:** Auto-complete file or directory names.

---

## **12. Getting Help**
- **man** (Manual for a command):
  ```bash
  man <command>
  ```

- **--help** (Quick help for a command):
  ```bash
  <command> --help
  ```
