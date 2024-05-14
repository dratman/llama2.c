import json
import os
from wikipedia import wikipedia
import re

def fetch_wikipedia_articles(article_names_file, output_folder, base_filename, file_size=10*1024*1024, num_files=50):
    wikipedia.set_lang('en')
    output_index = 0
    current_size = 0
    all_stories = []

    # Create output directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    with open(article_names_file, 'r', encoding='utf-8') as names_file:
        for line in names_file:
            article_name = line.strip()
            try:
            # Fetch the Wikipedia page
                 mypage = wikipedia.page(title=article_name, pageid=None, auto_suggest=False, redirect=True)

                 # Clean the content
                 content = mypage.content

                 # Remove non-printing characters like newline and carriage return
                 content = re.sub(r'[\r\n]+', ' ', content)

                 # Remove backslashes
                 content = content.replace('\\', '')

                 # Merge multiple spaces into one
                 content = re.sub(r'\s+', ' ', content)

                 # Strip leading and trailing spaces
                 content = content.strip()

                 # Prepare the story dictionary
                 story = {"story": content}

                 # Convert the dictionary to a JSON string
                 story_json = json.dumps(story, ensure_ascii=True)

                 # Append the JSON string to a list
                 all_stories.append(story_json)

                 # Update the current size
                 current_size += len(story_json.encode('utf-8'))

                 # Check if the current file size exceeds the threshold or the file count limit is reached
                 if current_size >= file_size or (output_index >= num_files - 1 and num_files > 0):
                    # Write to JSON file
                    filename = f"{output_folder}/{base_filename}{output_index:02d}.json"
                    with open(filename, 'w', encoding='utf-8') as file:
                        file.write(f"[{','.join(all_stories)}]")
                    print(f"Created file {filename} with size ~{current_size/1024/1024:.2f} MB.")

                    # Prepare for next file
                    all_stories = []
                    current_size = 0
                    output_index += 1

                    # Stop if maximum file number is reached
                    if output_index >= num_files:
                        break
            except wikipedia.exceptions.PageError:
                print(f"Page not found: {article_name}")
            except wikipedia.exceptions.DisambiguationError as e:
                print(f"Disambiguation error for {article_name}, options: {e.options}")

    # Final file write if any residual stories
    if all_stories and output_index < num_files:
        filename = f"{output_folder}/{base_filename}{output_index:02d}.json"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"[{','.join(all_stories)}]")
        print(f"Created final file {filename} with size ~{current_size/1024/1024:.2f} MB.")

# Configuration
article_names_file = "data/wikipedia_as_text/wikipedia_articles_list.txt"  # Path to your file with Wikipedia article names
output_folder = "data/wikipedia_as_text/output_json_files"
base_filename = "data"

# Run the function
fetch_wikipedia_articles(article_names_file, output_folder, base_filename)
