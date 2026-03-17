import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
        valid_file_path = os.path.commonpath([abs_working_dir, target_file_path]) == abs_working_dir        
        if not valid_file_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_file_path]
        result = subprocess.run(command, cwd=abs_working_dir, capture_output=True, text=True, timeout=30)
        if args:
            command.extend(args)
            if result.returncode != 0:
                return f'Error: Process exited with code {result.returncode}'
            if result.stdout is None or result.stderr is None:
                return 'No output produced'
            output_string = f'STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}'
            return output_string
    except Exception as e:
        return f"Error: executing Python file: {e}"