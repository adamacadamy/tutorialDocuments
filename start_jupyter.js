const { execSync } = require("child_process");

// Specify the Jupyter Notebook port
const JUPYTER_PORT = "8888"; // Change this to any available port

function isInstalled(command) {
    try {
        execSync(`${command} --version`, { stdio: "ignore" });
        return true;
    } catch (error) {
        return false;
    }
}

function installDependencies() {
    if (!isInstalled("jupyter")) {
        console.log("Installing Jupyter...");
        execSync("pip install jupyter --break-system-packages", { stdio: "inherit" });
    } else {
        console.log("Jupyter is already installed.");
    }

    if (!isInstalled("ijs")) {
        console.log("Installing ijavascript...");
        execSync("npm install -g ijavascript", { stdio: "inherit" });
        execSync("ijsinstall", { stdio: "inherit" });
    } else {
        console.log("iJavascript is already installed.");
    }
}

function startJupyter() {
    console.log(`Starting Jupyter Notebook on port ${JUPYTER_PORT}...`);
    execSync(`jupyter notebook --no-browser --port=${JUPYTER_PORT} --NotebookApp.token='' --NotebookApp.password=''`, { stdio: "inherit" });
}

// Run installation and start Jupyter
installDependencies();
startJupyter();
