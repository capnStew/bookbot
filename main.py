def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    character_list = sort_character_count(character_count)
    print(f"--- Begin report of {book_path} ---\n"
    f"{word_count} words found in document\n")
    for c in character_list:
        print(f"The '{c[0]}' character was found {c[1]} times")
    print("--- End report ---")  

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    character_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in character_dict:
            character_dict[lowered] += 1
        else:
            character_dict[lowered] = 1
    return character_dict

def sort_character_count(char_dict):
    char_list = list(char_dict.items())
    char_alpha = []
    for char in char_list:
        if char[0].isalpha():
            char_alpha.append(char)
    char_sorted = sorted(char_alpha, key = lambda char: char[1], reverse = True)
    return char_sorted

main()