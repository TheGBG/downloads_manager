import os
from utils import *

# Get the home dir like this so it works
# in any computer
home_directory = os.path.expanduser('~')

# This is the only hardcoded part
downloads_folder = 'Downloads'

root_path = os.path.join(home_directory, downloads_folder)
filenames = os.listdir(root_path)

for dirty_name in filenames:

    # 1. Generate the clean name
    clean_name = clean_filename(dirty_name)

    # 2. Build the clean path and the dirty path
    clean_path = os.path.join(root_path, clean_name)
    dirty_path = os.path.join(root_path, dirty_name)

    # 3. Handle names already clean and possible duplicates
    if clean_name == dirty_name:
        print(f'Filename "{dirty_name}" is already clean, skipping this file.')
        continue

    if os.path.exists(clean_path):
        clean_path = create_unique_file_path(root_path, clean_name)
        clean_name = os.path.basename(clean_path)

    # 4.Rename and print feedback
    os.rename(dirty_path, clean_path)
    
    message = f'Renamed {dirty_name} to {clean_name}'
    print(message)

print('All files renamed.')
