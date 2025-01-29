# How to Install Node.js on Windows and Debian

Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine. It allows you to build scalable network applications. Below are step-by-step instructions for installing Node.js on Windows and Debian.

---

## **Installing Node.js on Windows**

1. **Download the Node.js Installer**
   - Go to the [official Node.js website](https://nodejs.org/).
   - Choose either the **LTS (Long-Term Support)** version or the **Current** version based on your needs.

2. **Run the Installer**
   - Double-click the downloaded `.msi` file to start the installation.
   - Follow the on-screen instructions.
     - Accept the license agreement.
     - Choose the installation directory.
     - Select optional tools (e.g., automatically install Chocolatey for package management).

3. **Verify Installation**
   - Open a Command Prompt or PowerShell and type:
     ```bash
     node -v
     ```
     This command displays the installed Node.js version.

4. **Install npm (Node Package Manager)**
   - npm is included with Node.js. To verify, run:
     ```bash
     npm -v
     ```
     This displays the npm version.

5. **Optional: Update npm**
   - If needed, update npm to the latest version:
     ```bash
     npm install -g npm
     ```

---

## **Installing Node.js on Debian**

1. **Update System Package Index**
   - Run the following command:
     ```bash
     sudo apt update
     sudo apt upgrade -y
     ```

2. **Install Node.js from NodeSource**
   - Install the required dependencies:
     ```bash
     sudo apt install -y curl
     ```
   - Download the NodeSource setup script:
     ```bash
     curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
     ```
     Replace `18.x` with the desired Node.js version (e.g., `20.x` for Node.js 20).

3. **Install Node.js**
   - Run:
     ```bash
     sudo apt install -y nodejs
     ```

4. **Verify Installation**
   - Check the installed Node.js version:
     ```bash
     node -v
     ```
   - Check the installed npm version:
     ```bash
     npm -v
     ```

5. **Optional: Install Build Tools**
   - Some npm packages require build tools. Install them with:
     ```bash
     sudo apt install -y build-essential
     ```

---

## **Testing Node.js Installation**

To ensure Node.js is working correctly:
1. Create a file named `app.js`:
   ```javascript
   console.log("Node.js is installed!");
   ```

2. Run the file:
   ```bash
   node app.js
   ```

You should see the message `Node.js is installed!` printed in the terminal.

---

## Additional Resources
- [Node.js Official Website](https://nodejs.org/)
- [NodeSource Node.js Binary Distributions](https://github.com/nodesource/distributions)

