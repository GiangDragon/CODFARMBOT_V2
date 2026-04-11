import subprocess
import sys
import os

VENV_DIR = ".venv"

def create_venv():
    if not os.path.exists(VENV_DIR):
        subprocess.check_call([sys.executable, "-m", "venv", VENV_DIR])

def install_packages():
    pip_path = os.path.join(VENV_DIR, "Scripts", "pip.exe")  # Windows

    subprocess.check_call([pip_path, "install", "--upgrade", "pip"])
    subprocess.check_call([pip_path, "install", "-r", "requirements.txt"])

if __name__ == "__main__":
    create_venv()
    install_packages()
    if not os.path.exists("media"):
        os.makedirs("media")