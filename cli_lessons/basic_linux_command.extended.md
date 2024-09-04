
# Basic Linux Commands and Path Shortcuts

## 1. Introduction
Linux is a powerful and flexible operating system that allows users to interact with their system through the command line interface (CLI). This document covers basic Linux commands and shortcuts for path navigation, such as `.` (current directory), `~` (home directory), and `..` (parent directory).

## 2. Path Shortcuts

### `.` - Current Directory
The `.` represents the current directory. It's commonly used in commands when you want to execute a file or script in the current working directory.

**Example:**
```bash
cd ~
touch ./myfile.txt
ls ./myfile.txt
```
This command runs the `script.sh` file in the current directory.

### `..` - Parent Directory
The `..` represents the parent directory of the current directory. You can use this shortcut to move up one directory level.

**Example:**
```bash
cd ..
```
This command changes your current working directory to its parent directory.

### `~` - Home Directory
The `~` symbol refers to the home directory of the current user. It's a convenient way to quickly navigate to your home directory without typing the full path.

**Example:**
```bash
cd ~
```
This command takes you to your home directory.

### `-` - Previous Directory
The `-` symbol is used to navigate to the previous directory you were in.

**Example:**
```bash
cd -
```
This command switches you to the last directory you visited.

## 3. Basic Linux Commands

### `pwd` - Print Working Directory
Displays the full path of the current working directory.

**Usage:**
```bash
pwd
```

### `ls` - List Directory Contents
Lists files and directories in the current directory. Common options include:
- `ls -l` for detailed listing (permissions, owner, size, etc.)
- `ls -a` to show hidden files

**Usage:**
```bash
ls
ls -l
```

### `cd` - Change Directory
Changes the current directory. You can use absolute or relative paths.

**Usage:**
```bash
cd /path/to/directory
cd ..
```

### `cp` - Copy Files and Directories
Copies files or directories from one location to another.

**Usage:**
```bash
cp source_file destination
cp -r source_directory destination_directory
```

### `mv` - Move (or Rename) Files and Directories
Moves or renames files and directories.

**Usage:**
```bash
mv old_name new_name
mv file.txt /path/to/new/location
```

### `rm` - Remove Files and Directories
Deletes files or directories. Use `-r` to remove directories and their contents recursively.

**Usage:**
```bash
rm file.txt
rm -r directory
```

### `mkdir` - Make Directory
Creates a new directory.

**Usage:**
```bash
mkdir new_directory
```

### `rmdir` - Remove Empty Directories
Deletes empty directories.

**Usage:**
```bash
rmdir empty_directory
```

### `touch` - Create Empty File
Creates a new, empty file, or updates the timestamp of an existing file.

**Usage:**
```bash
touch newfile.txt
```

### `cat` - Concatenate and Display File Content
Displays the content of a file in the terminal.

**Usage:**
```bash
cat file.txt
```

### `nano` / `vim` / `vi` - Text Editors
Open files for editing in different text editors. `nano` is user-friendly for beginners, while `vim` and `vi` are more advanced.

**Usage:**
```bash
nano file.txt
vim file.txt
```

### `chmod` - Change File Permissions
Changes the file permissions for the owner, group, and others.

**Usage:**
```bash
chmod 755 file.sh
```

### `chown` - Change File Owner and Group
Changes the ownership of a file or directory.

**Usage:**
```bash
chown user:group file.txt
```

### `df` - Disk Space Usage
Shows the available and used disk space on all mounted filesystems.

**Usage:**
```bash
df -h
```

### `du` - Directory Space Usage
Estimates file and directory space usage.

**Usage:**
```bash
du -sh /path/to/directory
```

### `ps` - Process Status
Lists currently running processes.

**Usage:**
```bash
ps aux
```

### `kill` - Terminate Processes
Kills a process by its process ID (PID).

**Usage:**
```bash
kill 1234
```

### `man` - Manual Pages
Displays the manual page for a command, which includes detailed information about how to use it.

**Usage:**
```bash
man ls
```

## 4. Conclusion
This guide covers some of the most essential Linux commands and path shortcuts. Mastering these will allow you to navigate the file system, manage files, and control processes more effectively. For more advanced operations, consult the manual pages with the `man` command.
