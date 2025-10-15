from stats import get_num_words, get_num_chars, get_report_values
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_filepath = sys.argv[1]

    book_text = get_book_text(book_filepath)
    num_words = get_num_words(book_text)
    chars_dict = get_num_chars(book_text)
    result_list = get_report_values(chars_dict)
    print(result_list)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char in result_list:
        print(f"{char["char"]}: {char["num"]}")

    print("============= END ===============")

main()