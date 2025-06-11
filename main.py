#!/usr/bin/python3

from stats import number_of_words

def get_book_text(filepath):
	return filepath.read()

def main():
	with open("books/frankenstein.txt") as filepath:
		num_words = number_of_words(get_book_text(filepath))
		print(f"{num_words} words found in the document")

main()
