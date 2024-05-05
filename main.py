from string import ascii_lowercase
from typing import Counter

with open("books/frankenstein.txt") as f:
    file_contents = f.read()

word_count = len(file_contents.split())


letters = []

contents = file_contents.strip().replace(" ", "").lower()

for ch in contents:
    if ch not in ascii_lowercase:
        continue

    letters.append(ch)

counter = Counter(letters)
sorted_items = sorted(counter.items(), key=lambda x: x[1], reverse=True)
print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count} words found in the document")
for item in sorted_items:
    print(f"The '{item[0]}' character was found {item[1]} times")

print("--- End report ---")
