from stats import num_words, num_chars_todict,num_chars_tolist
import sys

def get_book_text(filepath: str) -> str:
    data = ""
    with open(filepath) as f:
        data = f.read()

    return data

def main():
    p = sys.argv[1]
    text = get_book_text(p)
    word_count = num_words(text)
    char_count = num_chars_todict(text)
    result = num_chars_tolist(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {p}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for d in result:
        for k,v in d.items():
            if k.isalpha():
                print(f"{k}: {v}")
    print("============= END ===============")




if __name__ == "__main__":
    main()

