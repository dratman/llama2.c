import subprocess
import sys

def run_command_with_args(command, args_list):
    for args in args_list:
        # Build the full command with arguments
        full_command = command + args.split()
        # Execute the command
        try:
            result = subprocess.run(full_command, check=True, text=True, capture_output=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error executing {full_command}: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Example usage: python my_xargs.py 'python filter.py' < file_list.txt
    command = sys.argv[1]  # Command to run ---------------------------------------- COMMAND TO RUN
    file_list = sys.stdin.read().strip().split('\n')  # Read file list from stdin

    # Execute the command on each file
    run_command_with_args(command, file_list)
