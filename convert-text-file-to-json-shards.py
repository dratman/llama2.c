import json
import os

def chunk_file_to_json(input_file, output_dir, chunk_size=6000):
    """
    Splits the input text file into smaller JSON files (shards).

    :param input_file: Path to the input text file.
    :param output_dir: Directory to save the JSON shards.
    :param chunk_size: Number of lines in each shard.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r', encoding='utf-8') as file:
        count = 0
        chunk = []
        for line_number, line in enumerate(file):
            chunk.append(line.strip())
            if (line_number + 1) % chunk_size == 0:
                with open(os.path.join(output_dir, f'shard_{count}.json'), 'w', encoding='utf-8') as out_file:
                    json.dump({"text": chunk}, out_file, ensure_ascii=False)
                count += 1
                chunk = []

        # Write any remaining lines as the last shard
        if chunk:
            with open(os.path.join(output_dir, f'data{count}.json'), 'w', encoding='utf-8') as out_file:
                json.dump({"text": chunk}, out_file, ensure_ascii=False)

# Example usage
input_file_path = '/Users/RalphDratman_1/Downloads/complete-works-of-Mark-Twain-gutenberg.txt'
output_directory = '/Users/RalphDratman_1/Downloads/complete-works-of-Mark-Twain-gutenberg/shards2'
chunk_file_to_json(input_file_path, output_directory)
