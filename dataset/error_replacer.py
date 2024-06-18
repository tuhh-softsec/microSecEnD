from pathlib import Path
import re

def replace_in_file(file_path):
    try:
        if not file_path.exists():
            print(f"File does not exist: {file_path}")
            return

        content = file_path.read_text(encoding='utf-8')
        modified_content = re.sub(r'--\}', r'--\\n}', content)

        if content != modified_content:
            file_path.write_text(modified_content, encoding='utf-8')
            print(f"Updated file: {file_path}")
        else:
            print(f"No changes needed: {file_path}")

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

def process_all_subfolders(root_dir):
    root_path = Path(root_dir)
    # Using rglob to recursively find all .txt files
    for file_path in root_path.rglob('*.txt'):
        replace_in_file(file_path)

# Example usage:
root_dir = Path(r'put\your\root\dir\here') #set root dir
process_all_subfolders(root_dir)
