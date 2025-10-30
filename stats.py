def get_num_words(content: str) -> int:

    return len(content.split())

def get_character_count(content: str):
    character_dict = {}
    for ch in content.lower():
        if not ch.isalpha():
            continue
        if ch not in character_dict:
            character_dict[ch] = 0
        character_dict[ch] += 1
    # dict(sorted(x.items(), key=lambda item: item[1]))
    return dict(sorted(character_dict.items(), key=lambda item: item[1], reverse=True))

def print_report(character_count):
    print("--------- Character Count -------")
    for ch in character_count:
        print(f"{ch}: {character_count[ch]}")
    print("============= END ===============")
