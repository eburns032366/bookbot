from stats import get_word_count

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = list(get_word_count(text))
    print(f"Found {len(words)} total words")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
