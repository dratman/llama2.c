import statistics
import math

def file_statistics(file_path):
    try:
        # Initialize variables to hold counts, longest line, and line lengths
        total_chars = 0
        total_words = 0
        total_lines = 0
        max_length_line = ""
        line_lengths = []  # List to hold the length of each line for statistical analysis

        # Open file in read mode
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line_length = len(line)

                # Update counts and lists
                total_lines += 1
                total_chars += len(line.encode('utf-8'))
                total_words += len(line.split())
                line_lengths.append(line_length)

                # Check if this line is the longest found so far
                if line_length > len(max_length_line):
                    max_length_line = line

        # Calculate statistics
        if total_lines > 0:
            average_line_length = sum(line_lengths) / total_lines
            std_deviation = statistics.stdev(line_lengths)
            # Calculate 95% confidence interval (assuming normal distribution)
            margin_error = 1.96 * (std_deviation / math.sqrt(total_lines))
            confidence_interval = (average_line_length - margin_error, average_line_length + margin_error)
        else:
            average_line_length = 0
            std_deviation = 0
            confidence_interval = (0, 0)

        # Print results
        print("File statistics:")
        print(f"Total number of characters (bytes): {total_chars}")
        print(f"Total number of words: {total_words}")
        print(f"Total number of lines: {total_lines}")
        print(f"Longest line: {max_length_line.strip()}")
        print(f"Average line length: {average_line_length:.2f}")
        print(f"Standard deviation of line lengths: {std_deviation:.2f}")
        print(f"95% confidence interval for line lengths: {confidence_interval}")

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
