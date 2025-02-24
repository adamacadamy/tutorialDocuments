import subprocess
import sys

# Specify the Jupyter Notebook port
JUPYTER_PORT = "8888"  # Change this to any available port

def is_installed(command):
    """Check if a command is installed by attempting to run it."""
    try:
        subprocess.run([command, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except FileNotFoundError:
        return False
    except subprocess.CalledProcessError:
        return False

def install_dependencies():
    """Install Jupyter and ijavascript only if not installed."""
    if not is_installed("jupyter"):
        print("Installing Jupyter...")
        subprocess.run([sys.executable, "-m", "pip", "install", "jupyter", "--break-system-packages"], check=True)
    else:
        print("Jupyter is already installed.")

    if not is_installed("ijs"):
        print("Installing ijavascript...")
        subprocess.run(["npm", "install", "-g", "ijavascript"], check=True)
        subprocess.run(["ijsinstall"], check=True)
    else:
        print("ijavascript is already installed.")

def start_jupyter():
    """Launch Jupyter Notebook on a specified port without authentication."""
    print(f"Starting Jupyter Notebook on port {JUPYTER_PORT}...")
    subprocess.run([
        "jupyter", "notebook", 
        "--no-browser", 
        f"--port={JUPYTER_PORT}", 
        "--NotebookApp.token=''", 
        "--NotebookApp.password=''"
    ], check=True)

if __name__ == "__main__":
    install_dependencies()
    start_jupyter()
