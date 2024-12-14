# cURL Tutorial for Linux

This document provides a comprehensive guide to using cURL, from installation to downloading files and making REST API requests.

---

## **1. Install cURL**

cURL is often pre-installed on Linux. If not, install it using your package manager:

### **On Debian/Ubuntu:**
```bash
sudo apt update
sudo apt install curl
```

### **On CentOS/RHEL:**
```bash
sudo yum install curl
```

### **On Fedora:**
```bash
sudo dnf install curl
```

### **Verify Installation:**
```bash
curl --version
```

---

## **2. Basic cURL Usage**

### **a. Fetch a Webpage**
```bash
curl https://www.google.com
```

### **b. Save Output to a File**
```bash
curl -o output.html https://www.google.com
```

### **c. Save with the Same Filename as on the Server**
```bash
curl -O https://www.google.com/index.html
```

---

## **3. Download Files**

### **a. Download a File**
Download an Ubuntu ISO:
```bash
curl -O https://releases.ubuntu.com/22.04/ubuntu-22.04.3-live-server-amd64.iso
```

### **b. Save with a Custom Name**
```bash
curl -o ubuntu-server.iso https://releases.ubuntu.com/22.04/ubuntu-22.04.3-live-server-amd64.iso
```

### **c. Resume Interrupted Download**
```bash
curl -C - -O https://releases.ubuntu.com/22.04/ubuntu-22.04.3-live-server-amd64.iso
```

### **d. Limit Download Speed**
Limit download speed to 1MB/s:
```bash
curl --limit-rate 1M -O https://releases.ubuntu.com/22.04/ubuntu-22.04.3-live-server-amd64.iso
```

---

## **4. Authentication Examples**

### **a. Basic Authentication**
Download a file from a protected server:
```bash
curl -u username:password https://example.com/protected/file.zip
```

### **b. Bearer Token Authentication**
```bash
curl -H "Authorization: Bearer <YOUR_TOKEN>" https://api.github.com/user
```

---

## **5. REST API Requests**

### **a. GET Request**
Fetch a list of users from a public API:
```bash
curl -X GET https://jsonplaceholder.typicode.com/users
```

### **b. POST Request**
Send a POST request with JSON data:
```bash
curl -X POST -d '{"title":"foo","body":"bar","userId":1}' -H "Content-Type: application/json" https://jsonplaceholder.typicode.com/posts
```

### **c. PUT Request**
Update a resource:
```bash
curl -X PUT -d '{"id":1,"title":"updated title","body":"updated body","userId":1}' -H "Content-Type: application/json" https://jsonplaceholder.typicode.com/posts/1
```

### **d. DELETE Request**
Delete a resource:
```bash
curl -X DELETE https://jsonplaceholder.typicode.com/posts/1
```

### **e. Custom Headers**
```bash
curl -H "Content-Type: application/json" -H "Accept: application/json" https://api.github.com
```

---

## **6. Download and Execute Software**

### **a. Download and Execute a Shell Script**
Install Docker using its installation script:
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
chmod +x get-docker.sh
sudo ./get-docker.sh
```

### **b. Download a .deb Package**
Download and install Google Chrome:
```bash
curl -O https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
```

---

## **7. Upload Files**

### **Example: Upload to an API**
Upload a file to Imgur:
```bash
curl -X POST -H "Authorization: Client-ID <YOUR_CLIENT_ID>" -F "image=@/path/to/your/image.jpg" https://api.imgur.com/3/image
```

---

## **8. Advanced Usage**

### **a. Check Your Public IP**
```bash
curl https://api.ipify.org
```

### **b. Test Website Response Time**
```bash
curl -w "Time to connect: %{time_connect}\nTime to transfer: %{time_starttransfer}\nTotal time: %{time_total}\n" -o /dev/null -s https://www.google.com
```

### **c. Follow Redirects**
```bash
curl -L https://bit.ly/3u9Qz3H
```

### **d. Debug a Request**
```bash
curl -v https://jsonplaceholder.typicode.com/posts
```

---
 