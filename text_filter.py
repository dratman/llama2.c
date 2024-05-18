# # Open the input file for reading and the output file for writing
# with open('/home/ralph/rdLLMScape/llama2.c/data/TinyStories_all_data/data49.json', 'r', encoding='utf-8') as infile, \
#      open('/home/ralph/rdLLMScape/llama2.c/data/TinyStories_all_data/data49_modified.json', 'w', encoding='utf-8') as outfile:
#     for line in infile:
#         # Replace undecoded newlines with real newlnes.
#         modifiedB_line = line.replace('\\n','\n')
#         # Replace each '}' with '}\n' in the current line
#         modifiedA_line = modifiedB_line.replace('}', '}\n')
#         # Replace each '{' with '\n{' in the current line
#         modified_line = modifiedA_line.replace('{', '\n{')
#         # Write the modified line to the output file
#         outfile.write(modified_line)

import sys

# usage: python text_filter.py  input_filename output_filename

# Check if command line argument is provided
if len(sys.argv) < 2:
    print("Usage: sys.srgv[0] input_file output_file")
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]

# Open the input file for reading and the output file for writing
with open(input_filename, 'r', encoding='utf-8') as infile, \
     open(output_filename, 'w', encoding='utf-8') as outfile:
    for line in infile:
        # Replace "text" with "story"
        modified_line = line.replace('}','},')

        # Write the modified line to the output file
        outfile.write(modified_line)

