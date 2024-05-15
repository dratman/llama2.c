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

# Check if command line arguments are provided
if len(sys.argv) < 3:
    print("Usage: script_name input_file output_file")
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]

# Open the input file for reading and the output file for writing
with open(input_filename, 'r', encoding='utf-8') as infile, \
     open(output_filename, 'w', encoding='utf-8') as outfile:
    for line in infile:
        # Replace "text" with "story"
        modifiedC_line = line.replace('text','story')
        # Replace undecoded newlines with real newlnes.
        modifiedB_line = modifiedC_line.replace('\\n','\n')
        # Replace each '}' with '}\n' in the current line
        # modifiedA_line = modifiedB_line.replace('}', '}\n')
        modifiedA_line = modifiedB_line
        # Replace each '{' with '\n{' in the current line
        # modified_line = modifiedA_line.replace('{', '\n{')
        modified_line = modifiedA_line
        # Write the modified line to the output file
        outfile.write(modified_line)

