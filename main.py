def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    
    print(get_count_characters(text))


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)
    
def get_count_characters(text):
    dictionary_words = {}
    for c in text:
        lowered = c.lower()
        if lowered in dictionary_words:
            dictionary_words[lowered] += 1
        else:
            dictionary_words[lowered] = 1

    return dictionary_words

main()