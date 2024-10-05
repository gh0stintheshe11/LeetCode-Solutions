import os

def remove_empty_file(file_path):
    # Check if the file exists
    if os.path.exists(file_path):
        # Check if the file is empty
        if os.path.getsize(file_path) == 0:
            os.remove(file_path)  # Remove the empty file
            print(f"Removed empty file: {file_path}")
            
# remove all folder if there is only one question.json
for folder in os.listdir("solutions"):
    if len(os.listdir(f"solutions/{folder}")) == 1 and "question.json" in os.listdir(f"solutions/{folder}"):
        os.rmdir(f"solutions/{folder}")
        print(f"Removed folder: {folder}")

for folder in os.listdir("solutions"):
    for file in os.listdir(f"solutions/{folder}"):
        remove_empty_file(f"solutions/{folder}/{file}")