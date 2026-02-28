import os
import platform
import importlib.util
import sys
from pathlib import Path

# --- 1. SETUP PATHS ---
# Automatically find home, downloads, and your specific custom folder
home = Path.home()
custom_folder = home / "Downloads" / "Therealdi594's Git Downloader Files"
file_to_open = custom_folder / "Better-CMD.py"

# Ensure the custom folder exists before doing anything else
try:
    custom_folder.mkdir(parents=True, exist_ok=True)
    print(f"Directory ready: {custom_folder}")
except Exception as e:
    print(f"Error creating folder: {e}")
    sys.exit(1)

# --- 2. CHECK IF FILE ALREADY EXISTS ---
if file_to_open.exists():
    print(f"'{file_to_open.name}' already exists. Skipping download.")
else:
    print(f"File not found in {custom_folder.name}. Starting setup...")

    # A. Check if 'requests' is installed
    package_name = 'requests'
    if importlib.util.find_spec(package_name) is None:
        print(f"Installing {package_name}...")
        os.system(f'"{sys.executable}" -m pip install --user {package_name}')
    
    # B. Run your download script
    # Note: Git-Downloader.py must be in your current working directory
    print("Running Git-Downloader.py...")
    python_cmd = "python" if platform.system() == "Windows" else "python3"
    os.system(f"{python_cmd} Git-Downloader.py")

# --- 3. OPEN THE FILE ---
if file_to_open.exists():
    print(f"Opening {file_to_open}...")
    if platform.system() == "Windows":
        # Start command handles paths with spaces using the empty quote trick
        os.system(f'start "" "{file_to_open}"')
    elif platform.system() == "Darwin":  # macOS
        os.system(f'open "{file_to_open}"')
    else:  # Linux
        os.system(f'xdg-open "{file_to_open}"')
else:
    print(f"Error: Could not find '{file_to_open.name}' at {file_to_open}")
