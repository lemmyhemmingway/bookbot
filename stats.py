from collections import Counter

def num_words(text: str) -> int:
    return len(text.split())

def num_chars_todict(text: str) -> int:
    return dict(Counter(text.lower()))

def num_chars_tolist(d):
    result = []
    for k, v in d.items():
        result.append({k: v})

    return sorted(result, key=lambda x: x[next(iter(x))], reverse=True)

