def get_book_text(filepath):
	return filepath.read()

def number_of_words(contents):
	 return len(contents.split())
	
def main():
	with open("books/frankenstein.txt") as filepath:
		num_words = number_of_words(get_book_text(filepath))
		print(f"{num_words} words found in the document")

main()
