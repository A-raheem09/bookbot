def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print("==============Beginning of The Book Report of frankenstein.txt==============")
    print(f"There are {word_count} words in this book")
    char_count, chars = count_char(text)
    print(f"There are {char_count} characters in this book")
    char_list = [{"char": char, "count": count} for char, count in chars.items()]
    char_list.sort(key=lambda d: d["count"], reverse=True)
    for item in char_list:
        print(f"The item '{item['char']}' was found {item['count']}")
    print("==============The End of The Book Report==============")
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_char(text):
    l_text = text.lower()
    chars = {}
    char_count = 0
    for char in l_text:
        if char.isalpha():
            char_count += 1
            if char in chars:
                chars[char] += 1
            else :
                chars[char] = 1
    return char_count,chars

def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

main()