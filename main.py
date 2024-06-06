def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = get_char_counts(text)
    print_report(book_path, num_words, char_counts)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    return len(text.split())

def get_char_counts(text):
    counts = {}
    for c in text:
        lowered = c.lower()
        if lowered not in counts:
            counts[lowered] = 0
        counts[lowered] += 1
    
    return counts

def sort_on(dic):
    return dic["count"]


def print_report(path, words, chars):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document", end="\n\n")

    list_of_dicts = []
    for key, val in chars.items():
        if key.isalpha():
            list_of_dicts.append({"char": key, "count": val})

    list_of_dicts.sort(reverse=True, key=sort_on)
    
    for dic in list_of_dicts:
        print(f"The '{dic['char']}' character was found {dic['count']} times")

    
    print("--- End report ---")


if __name__ == '__main__':
    main()
