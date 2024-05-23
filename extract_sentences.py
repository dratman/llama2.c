import json
import nltk
import sys
from nltk.tokenize import sent_tokenize

def extract_sentences_from_json(file_path, max_length):
    """
    Extracts sentences from stories contained in a JSON file, discards sentences longer than `max_length` characters.

    This function opens a JSON file specified by `file_path`, reads stories contained within,
    tokenizes these stories into sentences, discards any sentence exceeding `max_length` characters in length,
    and finds the longest sentence among the remaining ones.

    Parameters:
        file_path (str): The path to the JSON file containing stories.
        max_length (int): Maximum allowed length of sentences to keep.

    Returns:
        tuple: A tuple containing:
               - A list of all valid sentences (<= max_length characters) formatted as {"story": sentence}
               - An integer representing the length of the longest valid sentence.
    """
    # Load data from the specified JSON file
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    all_sentences = []  # List to store all valid sentences extracted
    longest_valid_length = 0  # Variable to store the length of the longest valid sentence

    # Process each item in the data
    for item in data:
        if 'story' in item:
            story_text = item['story'].strip()  # Remove leading and trailing whitespace
            sentences = sent_tokenize(story_text)  # Tokenize the text into sentences

            # Filter and add sentences to the list if they are max_length characters or shorter
            for sentence in sentences:
                if len(sentence) <= max_length:
                    all_sentences.append({"story": sentence})
                    longest_valid_length = max(longest_valid_length, len(sentence))  # Update longest_valid_length

    return all_sentences, longest_valid_length

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <max_length> <input_file_path> <output_file_path>\nEx: python  extract_sentences.py  106  data/TS_all_data/data07.json  data/TS_all_data/sentences/data07.json")
        sys.exit(1)

    max_length = int(sys.argv[1])  # Convert the first argument to an integer
    input_file_path = sys.argv[2]  # Input file path
    output_file_path = sys.argv[3]  # Output file path

    # Extract sentences and the length of the longest valid sentence
    sentences, longest_valid_length = extract_sentences_from_json(input_file_path, max_length)

    # Saving the sentences to the specified output JSON file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(sentences, file, ensure_ascii=False, indent=4)  # Serialize and write the valid sentences as {"story": sentence}

    # Output the length of the longest valid sentence
    print("Length of the longest valid sentence:", longest_valid_length)
