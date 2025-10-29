from os.path import abspath, join, isdir, getsize, isfile
from os import listdir, sep 

def get_files_info(working_directory, directory="."):
    """
    Return a textual listing of a directory's contents constrained to a working directory.

    - working_directory: The sandbox root (absolute or relative).
    - directory: A RELATIVE path inside working_directory (defaults to ".").

    Returns:
        str
          On success: lines like
            - README.md: file_size=1032 bytes, is_dir=False
            - src: file_size=128 bytes, is_dir=True
          On failure: an error string starting with "Error: ..."
    """

    try:
        # Normalize paths 
        wd_abs = abspath(working_directory)
        full_path = abspath(join(wd_abs, directory))

        # Security check: ensure full_path stays witin working directory boundaries
        # Accept exact match (same dir) or a proper descendant (wd_abs + os.sep prefix)
        if not (full_path == wd_abs or full_path.startswith(wd_abs + sep)):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        # Check that the target is a directory
        if not isdir(full_path):
            return f'Error: "{directory}" is not a directory'
        
        # List contents; order doesn't matter but sorting for stability
        try:
            entries = sorted(listdir(full_path))
        except Exception as e:
            return f"Error: could not list directory contents ({e})"
        
        lines = []
        for name in entries:
            entry_path = join(full_path, name)

            try:
                size = getsize(entry_path)
                is_dir = isdir(entry_path)
            except Exception as e:
                # If we can't stat the file, report error for that entry
                return f"Error: failed to stat '{name}' ({e})"
            
            lines.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")
        
        return "\n".join(lines)
        
    except Exception as e:
        # Catch-all: tool functions should return strings so the LLM can reason about failures
        return f"Error: {e}"

