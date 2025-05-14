from stats import word_count

def get_book_text(file_path):
    with open(file_path) as file:
        book = file.read()
    return book

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    frankenstein_word_count = word_count(frankenstein)
    return print(f"{frankenstein_word_count} words found in the document")

main()