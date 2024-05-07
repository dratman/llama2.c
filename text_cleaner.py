import re

def clean_enwik9(input_file_path, output_file_path):
    # Regular expression to match text enclosed in <...>
    tag_pattern = re.compile(r'<[^>]+>')
    # Regular expression to match text enclosed in [[...]]
    brackets_pattern = re.compile(r'\[\[([^]]+)\]\]')

    with open(input_file_path, 'r', encoding='utf-8') as infile, \
         open(output_file_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # Remove all tags
            cleaned_line = re.sub(tag_pattern, '', line)
            # Replace [[...]] with the content inside the brackets
            cleaned_line = re.sub(brackets_pattern, r'\1', cleaned_line)
            outfile.write(cleaned_line)

# Usage example:
input_path = 'data/enwik9.txt'
output_path = 'data/cleaned_enwik9.txt'
clean_enwik9(input_path, output_path)
