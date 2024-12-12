#!/usr/bin/env python
import sys
import os
import subprocess
import ensurepip

def ensure_pip_installed():
    """Ensure pip and distutils are installed."""
    try:
        ensurepip.bootstrap()
    except Exception as e:
        print(f"Error bootstrapping pip: {e}")
        sys.exit(1)

def install_requirements():
    """Install required packages from requirements.txt."""
    requirements_file = os.path.join(os.path.dirname(__file__), "requirements.txt")
    if os.path.exists(requirements_file):
        print("Installing dependencies...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
            print("Dependencies installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing dependencies: {e}")
            sys.exit(1)
    else:
        print("requirements.txt not found. Please ensure it is in the same directory as main.py.")
        sys.exit(1)

def main():
    ensure_pip_installed()

    try:
        with open('requirements.txt', 'r') as f:
            packages_to_check = [line.strip().split('>=')[0] for line in f if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        print("requirements.txt not found. Please ensure the file exists.")
        return

    installed_packages = subprocess.check_output([sys.executable, '-m', 'pip', 'list']).decode('utf-8')

    for package in packages_to_check:
        if package in installed_packages:
            print(f"{package} is installed")
        else:
            print(f'{package} is NOT installed')
            install_requirements()
            break

    # Start the application
    import tkinter as tk
    from src.frontend.main_window import MainWindow
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
