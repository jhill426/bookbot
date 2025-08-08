from stats import get_book_text, get_letter_counts, get_word_count
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    relative_path_to_book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {relative_path_to_book}...")
    text = get_book_text(relative_path_to_book)
    print("----------- Word Count ----------")
    word_count = get_word_count(text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    letter_counts = get_letter_counts(text)
    for letter, count in letter_counts:
        print(f"{letter}: {count}")
    print("============= END ===============")

if __name__ == "__main__":
    main()