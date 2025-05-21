from stats import word_count, character_count, sort_character_count
import sys

def get_book_text(file_path):
    try:
        with open(file_path) as file:
            book = file.read()
        return book
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("---------------------------------") 

    print("----------- Word Count ----------")
    book_word_count = word_count(book)
    print(f"Found {book_word_count} total words")
    print("---------------------------------")

    print("--------- Character Count -------")
    frankenstein_char_count = character_count(book)
    sorted_chars = sort_character_count(frankenstein_char_count)

    for item in sorted_chars:
        char = item['character']
        count = item['count']
        # Check if the character is an alphabetical character
        if char.isalpha():
            # Print the character and its count
            print(f"{char}: {count}")

    print("---------------------------------")
    print("=========== Analysis Complete ===========")

main()
