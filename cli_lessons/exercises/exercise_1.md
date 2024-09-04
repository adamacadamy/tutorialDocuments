# **CLI Exercise: File & Directory Operations with Home Directory Focus**

## **Explanation: What is the Home Directory?**

The **home directory** is a personal directory assigned to each user on the system, where they have full permissions to create, delete, and manage files and directories. It's a space for personal data, configurations, and documents. The location of the home directory varies by operating system.

**N.B**
* `~` is a shortcut signifying the home directory/location
* `.` is a shortcut signifying the current directory/location
* `-` is a shortcut to the previous path directory/location

### **1. Windows**
In Windows, the home directory is located under `C:\Users\`, followed by the username. For example, if the username is `john`, the home directory would be `C:\Users\john`.

- **Example**: `C:\Users\username\`

### **2. macOS**
In macOS, the home directory is located under `/Users/`. If the username is `john`, the home directory would be `/Users/john`.

- **Example**: `/Users/username/`
### **13. Linux**
In Linux, the home directory for a user is located under the `/home` directory. For example, if the username is `john`, the home directory would be `/home/john`.

- **Example**: `/home/username/`


## **Revised Exercise: File & Directory Operations with Home Directory Focus**

### **Challenge Description:**
Enhance the CLI program to work specifically with operations related to the user's **home directory**. The tasks should include:
 
1. **Create a Directory in Home Directory**: Create a new directory within the user's home directory called `myDir`.
2. **Create a File in `~\myDir\myFile.txt`**: Create a new file in the user's home directory in the sub directory  `myDir`  
3. **Delete the File from `~\myDir\myFile.txt`**: Delete the file `myFile.txt` 
4. **Delete the Directory `~\myDir`**: Delete the directory `~\myDir`, with the option for recursive deletion if it contains files.
5. **List Files and Directories in Home Directory**: List all files and directories within the home directory or a subdirectory.
6. **Navigate to the Subdirectory `Documents`**: Change the current working directory to the subdirectory the `Documents`.
7. **Show Current Path**: Display the current working directory.
 