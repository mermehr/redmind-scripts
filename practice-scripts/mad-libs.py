"""
Simple practice script made more complicated than it needed to be
Loads a .txt file containing placeholders like ADJECTIVE, NOUN, VERB, or ADVERB
Prompts the user for inputs and tracks them in a list
Uses a function to both display and save the result
Includes a basic ASCII banner for fun
"""

import re
import os

# Banner
def print_banner():
    banner = r"""
 __  __           _     _ _       
|  \/  | __ _ ___| |__ (_) |_ ___ 
| |\/| |/ _` / __| '_ \| | __/ __|
| |  | | (_| \__ \ | | | | |_\__ \
|_|  |_|\__,_|___/_| |_|_|\__|___/

    Mad Libs Generator - Python Ops Edition
    """
    print(banner)

# Prompt replacements
def get_replacements(text):
    word_regex = re.compile(r'\b(ADJECTIVE|NOUN|VERB|ADVERB)\b')
    word_list = word_regex.findall(text)
    user_words = []

    for word_type in word_list:
        article = 'an' if word_type[0] in 'AEIOU' else 'a'
        user_input = input(f"Enter {article} {word_type.lower()}: ")
        user_words.append(user_input)

    return word_list, user_words

# Replace and output
def fill_mad_lib(text, word_list, user_words):
    result = text
    for placeholder, user_words in zip(word_list, user_words):
        result = result.replace(placeholder, user_words, 1)

    return result

# Save and show result
def output_result(final_text, output_filename="mad_results.txt"):
    print("\n--- Your Mad Lib ---\n")
    print(final_text)

    with open(output_filename, 'w') as file:
        file.write(final_text)

    print(f"\nMad Lib saved to: {os.path.abspath(output_filename)}")

# Main program flow
def main():
    print_banner()
    input_file = input("Enter the path to your Mad Libs template file: ").strip()

    if not os.path.exists(input_file):
        print(f"File not found: {input_file}")
        return

    with open(input_file, 'r') as file:
        original_text = file.read()
    word_list, user_inputs = get_replacements(original_text)
    completed_text = fill_mad_lib(original_text, word_list, user_inputs)
    output_result(completed_text)

if __name__ == "__main__":
    main()