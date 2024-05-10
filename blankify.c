#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

// Function to check if the word is a small word
bool is_small_word(const char *word) {
    const char *small_words[] = {"and", "the", "or", "a", "an", NULL};
    for (int i = 0; small_words[i] != NULL; i++) {
        if (strcmp(word, small_words[i]) == 0) return true;
    }
    return false;
}

// Function to check if the word is an abbreviation
bool is_abbreviation(const char *word) {
    int len = strlen(word);
    if (len > 0 && word[len - 1] == '.' && len <= 4) {
        for (int i = 0; i < len - 1; i++) {
            if (!isalpha(word[i])) return false;
        }
        return true;
    }
    return false;
}

// Main function to process the file
void process_file(const char *input_file, const char *output_file) {
    FILE *in = fopen(input_file, "r");
    FILE *out = fopen(output_file, "w");

    if (in == NULL || out == NULL) {
        perror("Error opening file");
        return;
    }

    char c;
    char word[100];
    int idx = 0;

    int wordlen = 0;
    while ((c = fgetc(in)) != EOF) {
        if (isalpha(c) || (c == '.' && idx > 0)) {
            word[idx++] = c;
            wordlen++;
        } else {
            if (idx != 0) {
                word[idx] = '\0';
                if (is_abbreviation(word)) {
                    word[strlen(word) - 1] = '\0';  // Remove the period
                    fprintf(out, "%s", word);
                } else if (is_small_word(word)) {
                    fprintf(out, "%s", word);
                } else {
                    // Print a string of underscores the same length as the removed word.
                    for (int j = 0; j < wordlen; j++)
                    fprintf(out, "_");
                }
                idx = 0;
            }
            fputc(c, out);
        }
    }

    fclose(in);
    fclose(out);
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <input file> <output file>\n", argv[0]);
        return 1;
    }

    process_file(argv[1], argv[2]);
    return 0;
}
