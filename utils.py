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
