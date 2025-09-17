def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def word_count(book):
    book_text = get_book_text(book)
    words = book_text.split()
    word_count = len(words)
    return word_count

def char_counts(book):
    book_text = get_book_text(book)
    char_count = {}
    for char in book_text:
        char = char.lower()
        if char in char_count.keys():
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def make_char_report(char_counts):
    items = []
    for ch, n in char_counts.items():
        items.append({"char": ch, "num": n})
    items.sort(reverse=True, key=sort_helper)
    return items

def sort_helper(item):
    return item["num"]

