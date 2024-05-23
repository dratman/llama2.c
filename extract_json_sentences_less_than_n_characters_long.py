import sys

def filter_sentences(max_length):
    try:
        for line in sys.stdin:
            if len(line.strip()) <= max_length:
                print(line, end='')  # Use end='' to avoid adding extra newlines
    except Exception as e:
        print(f"An error occurred: {str(e)}", file=sys.stderr)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py n")
        print("This script reads sentences from standard input and outputs only those sentences with length <= n.")
        return
    try:
        max_length = int(sys.argv[1])
        print("\nmax_length = ", max_length, "\n")
    except ValueError:
        print("Error: n must be an integer.")
        return

    filter_sentences(max_length)

if __name__ == "__main__":
    main()
