import os
from subprocess import run, TimeoutExpired

def run_python_file(working_directory, file_path, args=[]):
    """
    Execute a Python file inside the working directory with optional arguments.
    Always return output as a string.
    """
    try:
        wd_abs = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(wd_abs, file_path))  # <-- fix

        # Ensure the path stays inside the working directory
        if not (full_path == wd_abs or full_path.startswith(wd_abs + os.sep)):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # Check if the file path exists
        if not os.path.exists(full_path):
            return f'Error: File "{file_path}" not found.'

        # Ensure file_path is a Python file
        if not full_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        # Build execution command
        cmd = ["python", full_path] + list(args)

        # Execute with timeout + output capture
        completed = run(
            cmd,
            cwd=wd_abs,
            capture_output=True,
            timeout=30,
            text=True,
        )

        stdout = completed.stdout.strip()
        stderr = completed.stderr.strip()

        # If both empty -> no output
        if not stdout and not stderr:
            return "No output produced."

        lines = []
        if stdout:
            lines.append("STDOUT:")
            lines.append(stdout)
        if stderr:
            lines.append("STDERR:")
            lines.append(stderr)

        if completed.returncode != 0:
            lines.append(f"Process exited with code {completed.returncode}")

        return "\n".join(lines)

    except TimeoutExpired:
        return 'Error: executing Python file: timed out after 30 seconds'
    except Exception as e:
        return f"Error: executing Python file: {e}"