from os.path import abspath, join, exists, dirname 
from os import sep, makedirs

def write_file(working_directory, file_path, content):
    """
    Write content to a file inside the working directory.
    Always return a string indicating success or an error message
    """

    try:
        # Normalize working_directory and requested file path
        wd_abs = abspath(working_directory)
        full_path = abspath(join(wd_abs, file_path))

        # Security check: ensure full_path stays witin working directory boundaries
        # Accept exact match (same dir) or a proper descendant (wd_abs + os.sep prefix)
        if not (full_path == wd_abs or full_path.startswith(wd_abs + sep)):
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

    
        # Determine the parent directory 
        parent_dir = dirname(full_path)

        # If parent dir doesn't exist, create it
        if not exists(parent_dir):
            try:
                makedirs(parent_dir)
            except Exception as e:
                return f"Error: Unable to create directory '{parent_dir}'"
    
        # Write to/overwrite the file (creates the file if doesn't exist)
        try:
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception as e:
            return f"Error: {e}"
        

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        # Catch-all: tool functions should return strings so the LLM can reason about failures
        return f"Error: {e}"