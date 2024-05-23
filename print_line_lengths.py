import sys

def print_line_lengths(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Calculate the length of the line and print it
                line_length = len(line)
                print(line_length)
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py filename")
        return

    file_path = sys.argv[1]
    print_line_lengths(file_path)

if __name__ == "__main__":
    main()
