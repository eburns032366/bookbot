from stats import word_count 
from stats import count_chars

def main():
    wc = word_count()
    cc = count_chars()
    print(f"{wc} words found in the document")
    for i in cc:
        print(f"'{i}': {cc[i]}")
    return

if __name__ == "__main__":
    main()

