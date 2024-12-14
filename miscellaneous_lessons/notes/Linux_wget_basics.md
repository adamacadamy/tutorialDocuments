# wget Tutorial for Linux

This document provides a comprehensive guide to using `wget`, from installation to downloading files and making advanced requests.

---

## **1. Install wget**

`wget` is often pre-installed on Linux. If not, install it using your package manager:

### **On Debian/Ubuntu:**
```bash
sudo apt update
sudo apt install wget
```

### **On CentOS/RHEL:**
```bash
sudo yum install wget
```

### **On Fedora:**
```bash
sudo dnf install wget
```

### **Verify Installation:**
```bash
wget --version
```

---

## **2. Basic wget Usage**

### **a. Download a Single File**
Download the Google homepage:
```bash
wget https://www.google.com
```

### **b. Save Output with a Custom Name**
```bash
wget -O custom_name.html https://www.google.com
```

### **c. Download in the Background**
```bash
wget -b https://www.google.com
```
Check the progress in the `wget-log` file:
```bash
tail -f wget-log
```

---

## **3. Download Files**

### **a. Download a Large File**
Download an Ubuntu ISO:
```bash
wget https://releases.ubuntu.com/22.04/ubuntu-22.04.3-live-server-amd64.iso
```

### **b. Resume an Interrupted Download**
```bash
wget -c https://releases.ubuntu.com/22.04/ubuntu-22.04.3-live-server-amd64.iso
```

### **c. Limit Download Speed**
Limit download speed to 1MB/s:
```bash
wget --limit-rate=1m https://releases.ubuntu.com/22.04/ubuntu-22.04.3-live-server-amd64.iso
```

### **d. Download Files in Sequential Order**
Download multiple files listed in a text file:
```bash
wget -i file_list.txt
```
Where `file_list.txt` contains URLs, one per line.

---

## **4. Authentication Examples**

### **a. Basic Authentication**
Download a file from a protected server:
```bash
wget --user=username --password=password https://example.com/protected/file.zip
```

### **b. Bearer Token Authentication**
Use a token for API access:
```bash
wget --header="Authorization: Bearer <YOUR_TOKEN>" https://api.example.com/resource
```

---

## **5. Recursive Downloads**

### **a. Download an Entire Website**
Download a website recursively:
```bash
wget --recursive --no-clobber --page-requisites --html-extension --convert-links --domains example.com --no-parent https://example.com
```

### **b. Mirror a Website**
Create a local copy of a website:
```bash
wget --mirror -p --convert-links -P ./local_dir https://example.com
```

---

## **6. Advanced Usage**

### **a. Check Your Public IP**
```bash
wget -qO- https://api.ipify.org
```

### **b. Test Website Response Time**
```bash
wget --spider -S https://www.google.com
```

### **c. Skip SSL Certificate Validation**
Useful for self-signed certificates:
```bash
wget --no-check-certificate https://example.com
```

### **d. Debug a Request**
```bash
wget --debug https://jsonplaceholder.typicode.com/posts
```

---

## **7. Download and Execute Software**

### **a. Download and Execute a Shell Script**
Install Docker using its installation script:
```bash
wget -O get-docker.sh https://get.docker.com
chmod +x get-docker.sh
sudo ./get-docker.sh
```

### **b. Download a .deb Package**
Download and install Google Chrome:
```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
```

---

## **8. Upload Files**

`wget` does not support file uploads natively. Use tools like `curl` for uploading files.

---

## **9. Automate Downloads**

### **a. Schedule Downloads with cron**
Add this to your `crontab` to schedule a download every day:
```bash
0 3 * * * wget -c -P /path/to/download_dir https://example.com/file.zip
```

### **b. Use a Script for Multiple Downloads**
Create a script `download_files.sh`:
```bash
#!/bin/bash
wget -O file1.zip https://example.com/file1.zip
wget -O file2.zip https://example.com/file2.zip
```
Make it executable:
```bash
chmod +x download_files.sh
./download_files.sh
```

 