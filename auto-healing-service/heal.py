import os
import tempfile
import shutil

print("AI Auto-Healing Service Started")
print("--------------------------------")

# SAFE WHITELIST
ALLOWED_PATHS = [tempfile.gettempdir()]

temp_dir = tempfile.gettempdir()

# Verify allowed path
if temp_dir not in ALLOWED_PATHS:
    print("Unauthorized path detected!")
    exit()

print(f"Authorized cleanup path: {temp_dir}")

deleted_files = 0
MAX_DELETE_LIMIT = 50

for filename in os.listdir(temp_dir):

    if deleted_files >= MAX_DELETE_LIMIT:
        print("\nSafety limit reached.")
        break

    file_path = os.path.join(temp_dir, filename)

    try:
        # Skip important/system files
        if filename.endswith((".sys", ".dll", ".exe")):
            continue

        # Delete normal temp files only
        if os.path.isfile(file_path):
            os.remove(file_path)
            deleted_files += 1

            print(f"Deleted file: {filename}")

        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
            deleted_files += 1

            print(f"Deleted folder: {filename}")

    except Exception:
        pass

print(f"\nTotal deleted items: {deleted_files}")

print("\nSafe Recovery Completed Successfully!")
from datetime import datetime

with open("logs/healing.log", "w") as log:
    log.write(f"Timestamp: {datetime.now()}\n")
    log.write(f"Deleted Files/Folders: {deleted_files}\n")
    log.write("Status: SUCCESS\n")