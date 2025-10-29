from os.path import abspath, join, isfile
from os import sep 
from config import MAX_FILE_READ_SIZE

def get_file_content(working_directory, file_path):
    """
    Return the contents of a file inside the working directory.
    Always return a string (either file contents or an error message).
    """

    try:
        # Normalize workding_directory and requested file path 
        wd_abs = abspath(working_directory)
        full_path = abspath(join(wd_abs, file_path))

        # Security check: ensure full_path stays witin working directory boundaries
        if not (full_path == wd_abs or full_path.startswith(wd_abs + sep)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Check if file_path is a file 
        if not isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        # Read and return file contents
        try:
            with open(full_path, "r") as f:
                contents = f.read()
        except Exception as e:
            return f'Error: ({e})'
        
        # Truncate if necessary
        if len(contents) > MAX_FILE_READ_SIZE:
            truncated = (contents[:MAX_FILE_READ_SIZE] 
            + f' [...File "{file_path}" truncated at 10000 characters]'
            ) 
            return truncated
        
        return contents
            
    except Exception as e:
        # Agent-safe error reporting
        return f"Error: {e}"