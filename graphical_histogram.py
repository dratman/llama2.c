import sys
import matplotlib.pyplot as plt

def read_line_lengths_from_stdin():
    line_lengths = []
    try:
        for line in sys.stdin:
            line_lengths.append(len(line.strip()))
    except Exception as e:
        print(f"An error occurred: {str(e)}", file=sys.stderr)
        return []
    return line_lengths

def create_graphical_histogram(line_lengths, bin_size):
    if not line_lengths:
        print("No data to plot.", file=sys.stderr)
        return

    # Plotting the histogram
    plt.figure(figsize=(10, 6))
    plt.hist(line_lengths, bins=range(min(line_lengths), max(line_lengths) + bin_size, bin_size), edgecolor='black')
    plt.title('Histogram of Line Lengths')
    plt.xlabel('Line Length')
    plt.ylabel('Frequency')
    plt.grid(True)
    #plt.show()
    plt.savefig('output.png')

def main():
    # Read bin size from command line or use a default
    bin_size = int(sys.argv[1]) if len(sys.argv) > 1 else 10  # Default bin size of 10 if not specified

    line_lengths = read_line_lengths_from_stdin()
    create_graphical_histogram(line_lengths, bin_size)

if __name__ == "__main__":
    main()