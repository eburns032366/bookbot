import sys

from stats import word_count 
from stats import char_counts
from stats import make_char_report

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return
    
    book = sys.argv[1]
    wc = word_count(book)
    cc = char_counts(book)
    mr = make_char_report(char_counts(book))

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print(f"----------- Word Count ---------")
    print(f"Found {wc} total words")
    print(f"--------- Character Count ------")
    
    for i in mr:
        ch = i["char"]
        if ch.isalpha():
            print(f"{ch}: {i['num']}")
    return

if __name__ == "__main__":
    main()

