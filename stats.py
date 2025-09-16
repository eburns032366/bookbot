def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def word_count():
    book_text = get_book_text("books/frankenstein.txt")
    words = book_text.split()
    word_count = len(words)
    return word_count

def count_chars():
    book_text = get_book_text("books/frankenstein.txt")
    char_count = {}
    for char in book_text:
        char = char.lower()
        if char in char_count.keys():
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

