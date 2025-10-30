import sys
from stats import get_num_words, get_character_count, print_report

def get_book_text(path: str) -> str:
    data = ""
    with open(path) as f:
        data = f.read()

    return data


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    content = get_book_text(path)
    word_count = get_num_words(content)
    character_count = get_character_count(content)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print_report(character_count)


if __name__ == "__main__":
    main()
