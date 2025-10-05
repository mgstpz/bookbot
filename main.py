import sys
from stats import get_num_words, count_chars, sort_dict
def get_book_text(filepath):
    with open (filepath) as f:
        print(f"Analyzing book found at {filepath}")
        contents = f.read()
    return contents

def main():
    print("============ BOOKBOT ============")
    # ./books/frankenstein.txt
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    contents_book = get_book_text(sys.argv[1])
    print(f"Found {get_num_words(contents_book)} total words")
    letter_count = count_chars(contents_book)
    char_count = sort_dict(letter_count)
    for i in range(0, len(char_count)):
        print(f"{char_count[i]["char"]}: {char_count[i]["num"]}")

main()