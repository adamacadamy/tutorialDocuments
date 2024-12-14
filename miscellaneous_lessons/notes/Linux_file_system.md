# Linux File System Tutorial (Debian-Based Systems)

This lesson provides a comprehensive guide to understanding and working with the Linux file system, focusing on Debian-based distributions like Ubuntu.

---

## **1. Overview of the Linux File System**

The Linux file system follows a hierarchical structure starting with the root directory (`/`). Each directory serves a specific purpose:

1. **`/` (Root):** The base of the Linux file system hierarchy. All other directories stem from this.
2. **`/boot`:** Contains files needed to boot the system, including the Linux kernel and GRUB bootloader configuration files.
3. **`/dev`:** Stores device files representing hardware devices (e.g., `/dev/sda` for a hard drive).
4. **`/etc`:** Configuration files for the system and installed services.
5. **`/home`:** Contains personal directories for users (e.g., `/home/username`).
6. **`/init`:** Used during the system's initialization phase (rarely seen in modern systems; often replaced by `/sbin/init`).
7. **`/lib`:** Essential shared libraries needed by binaries in `/bin` and `/sbin`.
8. **`/lib64`:** Shared libraries for 64-bit binaries.
9. **`/lost+found`:** Reserved for file recovery purposes, especially in ext-based file systems. Used when files are found during a disk check.
10. **`/media`:** Temporary mount points for removable media like USB drives or CDs.
11. **`/mnt`:** Mount point for temporarily mounting file systems.
12. **`/opt`:** Contains optional software installed manually or from third-party sources.
13. **`/proc`:** Virtual file system representing system and process information (e.g., CPU and memory stats).
14. **`/root`:** Home directory for the root user (administrator).
15. **`/run`:** Temporary runtime files for the system and services (e.g., PID files, sockets).
16. **`/sbin`:** System binaries (programs for system administrators, like `ifconfig`).
17. **`/srv`:** Data served by the system (e.g., web server files for HTTP).
18. **`/sys`:** Virtual file system with kernel and hardware information.
19. **`/tmp`:** Temporary files. Files here are typically deleted on reboot.
20. **`/usr`:** Contains user programs, libraries, documentation, and more. Key subdirectories include `/usr/bin`, `/usr/lib`, and `/usr/share`.
21. **`/var`:** Variable data like logs (`/var/log`), caches, and spool files (e.g., print queues).

---

## **2. Navigating the File System**

### **a. Common Commands**

- **Change Directory:**
  ```bash
  cd /path/to/directory
  ```

- **List Directory Contents:**
  ```bash
  ls
  ```

- **View Hidden Files:**
  ```bash
  ls -a
  ```

- **Show Detailed Information:**
  ```bash
  ls -l
  ```

- **Go to Home Directory:**
  ```bash
  cd ~
  ```

- **Return to Previous Directory:**
  ```bash
  cd -
  ```

---

## **3. File and Directory Management**

### **a. Create a New Directory**
```bash
mkdir new_directory
```

### **b. Create an Empty File**
```bash
touch new_file
```

### **c. Copy Files and Directories**
```bash
cp source_file destination
```
To copy directories:
```bash
cp -r source_directory destination
```

### **d. Move/Rename Files**
```bash
mv old_name new_name
```

### **e. Delete Files and Directories**
```bash
rm file_name
```
To delete directories:
```bash
rm -r directory_name
```

---

## **4. File Permissions**

Linux uses a permission system with three levels:
- **User**: Owner of the file.
- **Group**: Group members.
- **Others**: Everyone else.

### **View Permissions**
```bash
ls -l
```
Example output:
```bash
-rw-r--r-- 1 user group 1234 Jan 1 12:00 file.txt
```
- `r` : Read
- `w` : Write
- `x` : Execute

### **Change Permissions**
```bash
chmod 755 file_name
```

### **Change Ownership**
```bash
chown new_user:new_group file_name
```

---

## **5. Disk Usage and Space**

### **a. Check Disk Space**
```bash
df -h
```

### **b. Check Directory Size**
```bash
du -sh /path/to/directory
```

### **c. Find Large Files**
```bash
find / -type f -size +100M
```

---

## **6. File Search and Manipulation**

### **a. Search for Files**
```bash
find /path -name "file_name"
```

### **b. Search Inside Files**
```bash
grep "search_term" file_name
```
To search recursively:
```bash
grep -r "search_term" /path
```

### **c. Display File Contents**
- **View Entire File:**
  ```bash
  cat file_name
  ```
- **View File Page by Page:**
  ```bash
  less file_name
  ```
- **View First 10 Lines:**
  ```bash
  head file_name
  ```
- **View Last 10 Lines:**
  ```bash
  tail file_name
  ```

---

## **7. Mounting and Unmounting Drives**

### **a. Mount a Drive**
```bash
sudo mount /dev/sdX /mnt
```
Replace `sdX` with your device name.

### **b. Unmount a Drive**
```bash
sudo umount /mnt
```

### **c. View Mounted File Systems**
```bash
mount | column -t
```

---

## **8. Links: Hard vs Soft Links**

### **a. Create a Hard Link**
```bash
ln original_file hard_link
```

### **b. Create a Soft Link (Symbolic Link)**
```bash
ln -s original_file symbolic_link
```

---

## **9. Backups and Archives**

### **a. Create a Tar Archive**
```bash
tar -cvf archive_name.tar /path/to/files
```

### **b. Extract a Tar Archive**
```bash
tar -xvf archive_name.tar
```

### **c. Compress a File with gzip**
```bash
gzip file_name
```

### **d. Decompress a File**
```bash
gunzip file_name.gz
```

---

## **10. Practice Exercises**

1. Navigate to the `/etc` directory and list all files.
   ```bash
   cd /etc
   ls
   ```

2. Create a new directory called `practice` in your home folder.
   ```bash
   mkdir ~/practice
   ```

3. Copy a configuration file from `/etc` to your `practice` directory.
   ```bash
   cp /etc/hosts ~/practice
   ```

4. Search for the term "root" in the `/etc/passwd` file.
   ```bash
   grep "root" /etc/passwd
   ```

5. Find files larger than 10MB in the `/var` directory.
   ```bash
   find /var -type f -size +10M
   ```

6. Create a tar archive of the `practice` directory and compress it with gzip.
   ```bash
   tar -czvf practice.tar.gz ~/practice
   ```

7. Mount a USB drive to `/mnt` and unmount it after use.
   ```bash
   sudo mount /dev/sdX /mnt
   sudo umount /mnt
   ```
 