def number_of_words(contents):
    return len(contents.split())

def letter_count(contents):
    letter_dict = {}
    for letter in contents.lower():
        letter_dict[letter] = letter_dict.get(letter,0) + 1
    return letter_dict

def sort_dict(letter_dict):
    return dict(sorted(letter_dict.items()))
