import os
from utils import clean_filename

# Get the home dir like this so it works
# in any computer
home_directory = os.path.expanduser('~')

# This is the only hardcoded part
downloads_folder = 'Downloads'

root_path = os.path.join(home_directory, downloads_folder)
filenames = os.listdir(root_path)

# TODO: create a function to check for duplicated items
# looking at the hash

# TODO: classify documents in the downloads folder by 
# its extension, and place them into folders

for dirty_name in filenames:

    # 1. Generate the clean name
    clean_name = clean_filename(dirty_name)

    # 2. Build the clean path and the dirty path
    clean_path = os.path.join(root_path, clean_name)
    dirty_path = os.path.join(root_path, dirty_name)

    if clean_name == dirty_name:
        print(f'Filename "{dirty_name}" is already clean, skipping this file.')
        continue

    # 3.Rename and print feedback
    os.rename(dirty_path, clean_path)
    
    message = f'Renamed {dirty_name} to {clean_name}'
    print(message)

print('All files renamed.')
