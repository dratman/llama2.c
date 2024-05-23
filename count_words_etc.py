def file_statistics(file_path):
    try:
        # Initialize variables to hold counts and the longest line
        total_chars = 0
        total_words = 0
        total_lines = 0
        max_length_line = ""
        total_line_lengths = 0

        # Open file in read mode
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Increment line count
                total_lines += 1

                # Update character and word counts
                total_chars += len(line.encode('utf-8'))
                total_words += len(line.split())

                # Check if this line is the longest found so far
                if len(line) > len(max_length_line):
                    max_length_line = line

                # Update total line lengths for average calculation
                total_line_lengths += len(line)

        # Calculate the average line length
        if total_lines > 0:
            average_line_length = total_line_lengths / total_lines
        else:
            average_line_length = 0

        # Print results
        print("File statistics:")
        print(f"Total number of characters (bytes): {total_chars}")
        print(f"Total number of words: {total_words}")
        print(f"Total number of lines: {total_lines}")
        print(f"Longest line: {max_length_line}")
        print(f"Average line length: {average_line_length:.2f}")

    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    # Get the file path from the user
    file_path = input("Enter the name of the text file: ")
    file_statistics(file_path)

if __name__ == "__main__":
    main()
