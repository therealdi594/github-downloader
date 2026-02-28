import os
import platform
import importlib.util
import sys
from pathlib import Path

# --- 1. CONFIGURATION ---
# The folder where everything will be saved
FOLDER_NAME = "Therealdi594's Git Downloader Files"

# Format: "Key": ["Filename_to_save.py", "RAW_GitHub_URL"]
apps = {
    "1": ["Better-CMD.py", "https://raw.githubusercontent.com/therealdi594/better-cmd/refs/heads/main/Better%20CMD.py"],
    "2": ["Cmd (ai).py", "https://raw.githubusercontent.com/therealdi594/better-cmd/refs/heads/main/Cmd%20(ai).py"],
    "3": ["Example.py", "https://raw.githubusercontent.com"]
}

def setup_requests():
    """Checks for requests and installs if missing."""
    if importlib.util.find_spec("requests") is None:
        print("Installing required library: requests...")
        os.system(f'"{sys.executable}" -m pip install --user requests')
    import requests
    return requests


def main():
    # --- 2. PATH SETUP ---
    home = Path.home()
    # Path: Downloads/Therealdi594's Git Downloader Files
    save_dir = home / "Downloads" / FOLDER_NAME
    
    # Create the folder if it doesn't exist
    save_dir.mkdir(parents=True, exist_ok=True)

    print(f"--- GITHUB MULTI-LAUNCHER ---")
    print(f"Storage: {save_dir}\n")
    
    for key, value in apps.items():
        print(f"[{key}] {value[0]}")
    
    choice = input("\nSelect a number to launch: ").strip()

    if choice in apps:
        filename, url = apps[choice]
        if not url:
            print("Slot is empty/Coming soon!")
            return

        full_path = save_dir / filename

        # --- 3. CHECK, DOWNLOAD, & LAUNCH ---
        if full_path.exists():
            print(f"Found {filename} locally.")
            launch_file(full_path)
        else:
            print(f" {filename} not found. Downloading...")
            requests = setup_requests()
            try:
                r = requests.get(url, timeout=10)
                r.raise_for_status()
                with open(full_path, "wb") as f:
                    f.write(r.content)
                print("Download complete.")
                launch_file(full_path)
            except Exception as e:
                print(f"Download failed: {e}")
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()
