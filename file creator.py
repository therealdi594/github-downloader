from pathlib import Path

# 1. Automatically find the user's home directory (e.g., C:\Users\Name or /Users/Name)
home = Path.home()

# 2. Define the path to the Downloads folder
downloads_path = home / "Downloads"

# 3. Ask for your custom folder name
folder_name = "Therealdi594's Git Downloader Files"

# 4. Combine them to create the full path
new_folder_path = downloads_path / folder_name

# 5. Create the folder
# exist_ok=True prevents an error if the folder already exists
try:
    new_folder_path.mkdir(parents=True, exist_ok=True)
    print(f"Success! Folder created at: {new_folder_path}")
except Exception as e:
    print(f"An error occurred: {e}")
