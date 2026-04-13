import subprocess
import sys
import os

VENV_DIR = ".venv"

def create_venv():
    if not os.path.exists(VENV_DIR):
        subprocess.check_call([sys.executable, "-m", "venv", VENV_DIR])

def install_packages():
    python_path = os.path.join(VENV_DIR, "Scripts", "python.exe")
    subprocess.check_call([python_path, "-m", "pip", "install", "--upgrade", "pip"])
    subprocess.check_call([python_path, "-m", "pip", "install", "-r", "requirements.txt"])

if __name__ == "__main__":
    create_venv()
    install_packages()
    if not os.path.exists("media"):
        os.makedirs("media")
