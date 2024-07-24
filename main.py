def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(f"There are {word_count} words in this book")
    char_count, chars = count_char(text)
    print(f"There are {char_count} characters in this book")

def get_book_text(path):
    with open(path) as f:
        return f.read()
def count_char(text):
    l_text = text.lower()
    chars = {}
    char_count = 0
    for char in l_text:
        char_count += 1
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 0
    return char_count,chars
def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count
main()