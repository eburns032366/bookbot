#!/usr/bin/python3

from stats import number_of_words
from stats import letter_count
from stats import sort_dict
import sys

def get_book_text(filepath):
    return filepath.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("------------ Word Count ------------")

    with open(sys.argv[1]) as filepath:
        num_words = number_of_words(get_book_text(filepath))
        print(f"Found {num_words} total words")

    print("------------ Character Count ------------")

    with open(sys.argv[1]) as filepath:
        count = letter_count(get_book_text(filepath))
        sorted_count = sort_dict(count)
        for key, value  in sorted_count.items():
            if key.isalpha():
                print(f"{key}: {value}")
main()
