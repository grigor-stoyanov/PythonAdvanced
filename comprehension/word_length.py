text = input().split(', ')
word_length = {word: len(word) for word in text}
print(*[f'{key} -> {value}' for key, value in word_length.items()], sep=', ')
