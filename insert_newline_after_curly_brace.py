# Open the input file for reading and the output file for writing
with open('/home/ralph/rdLLMScape/llama2.c/data/TinyStories_all_data/data49.json', 'r', encoding='utf-8') as infile, \
     open('/home/ralph/rdLLMScape/llama2.c/data/TinyStories_all_data/data49_modified.json', 'w', encoding='utf-8') as outfile:
    for line in infile:
        # Replace each '}' with '}\n' in the current line
        modified_line = line.replace('}', '}\n')
        # Write the modified line to the output file
        outfile.write(modified_line)
