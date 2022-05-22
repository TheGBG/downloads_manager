import os

def clean_filename(filename):
    '''
    Cleans a given string by:

    - removing leading and trailing spaces

    - replacing spaces and dots with _

    - making the name lowercase
    '''
    
    # 1. Separate name and extension
    name, extension = os.path.splitext(filename)
    
    # 2. Remove leading and trailing spaces
    clean_name = name.strip()
    
    # 3. Replace spaces and dots with _
    clean_name = clean_name.replace(' ', '_').replace('.', '_')

    # 4. Make the name lowercase
    clean_name = clean_name.lower()

    # 5. Add the extension back
    clean_name += extension

    return clean_name

def create_unique_file_path(root_path, filename):
    '''
    Adds a number to a filepath till its unique.
        file_path(1)
        file_path(2)
        file_path(3)
        ...
    '''
    
    i = 1
    name, extension = os.path.splitext(filename)

    filename = f'{name}({i}){extension}'
    file_path = os.path.join(root_path, filename)
    
    while os.path.exists(file_path):
        i += 1
        
        # Update the path with the final number
        filename = f'{name}({i}){extension}'
        file_path = os.path.join(root_path, filename)
    
    return file_path