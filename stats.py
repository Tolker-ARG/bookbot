import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents

def count_words(filepath):
    with open(filepath) as f:
        contents = f.read()
        words = contents.split()
        count = len(words)
        return f"Found {count} total words"

def character_count(filepath):
    text = get_book_text(filepath)
    lowercases = text.lower()
    dict_lower = {}
    for letter in lowercases:
        if letter not in dict_lower:
            dict_lower[letter] = 1
        else:
            dict_lower[letter] += 1
    return dict_lower

def sort_on(items):
    return items["num"]

def dict_sort(dict_lower):
    dict_list = []
    for key, value in dict_lower.items():
        if key.isalpha():
            char_dict = {"char": key, "num": value}
            dict_list.append(char_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
    


    



