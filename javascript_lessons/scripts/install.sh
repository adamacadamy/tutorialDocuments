#!/bin/bash

# A script to install Jupyter, the JavaScript kernel, and fix common issues.

echo "=== Starting Installation Script for Jupyter and JavaScript Kernel ==="

# Step 1: Install Python and pip
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Installing Python3..."
    sudo apt update && sudo apt install -y python3 python3-pip 
else
    echo "Python3 is already installed."
fi

# Upgrade pip
echo "Upgrading pip..."
pip3 install --upgrade pip  --break-system-packages

# Step 2: Install Jupyter Notebook and JupyterLab
echo "Installing Jupyter Notebook and JupyterLab..."
sudo pip install jupyter ipython --break-system-packages
sudo pip3 install notebook jupyterlab  --break-system-packages

# Step 3: Install Node.js and npm (via nvm) 
if ! command -v nvm &> /dev/null; then
    echo "Installing nvm..."
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \ . "$NVM_DIR/nvm.sh"
    [ -s "$NVM_DIR/bash_completion" ] && \ . "$NVM_DIR/bash_completion"
fi

 


# Ensure Node.js is installed and switch to a stable version
echo "Installing Node.js via nvm..."
nvm install 18
nvm use 18

# Step 4: Install ijavascript Kernel
echo "Installing ijavascript kernel..."
sudo npm install -g ijavascript
ijsinstall

# Step 5: Rebuild zeromq Dependency
echo "Rebuilding zeromq dependency..."
sudo npm rebuild zeromq || sudo npm install zeromq --force

# Step 6: Verify Kernel Installation
echo "Verifying kernel installation..."
kernels=$(jupyter kernelspec list)
if echo "$kernels" | grep -q "ijavascript"; then
    echo "iJavascript kernel is installed."
else
    echo "iJavascript kernel not found. Attempting to reinstall..."
    ijsinstall
fi

# Step 7: Final Test
echo "Testing Jupyter Notebook..."
jupyter notebook --debug &

echo "=== Installation and Setup Completed ==="
echo "If issues persist, please review the debug logs from Jupyter Notebook."
