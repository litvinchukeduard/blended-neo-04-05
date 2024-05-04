word_list = [
    "Serendipity", # Sere...
    "Mellifluous",
    "Effervescent",
    "Luminous",
    "Quintessential",
    "Ephemeral",
    "Resplendent",
    "Euphoria",
    "Tranquility",
    "Cascade"
]

# map

# def shorten_word(word: str) -> str:
#     if len(word) > 4:
#         return word[:4] + '...'
#     else:
#         return word
def shorten_word(word: str) -> str:
    return word[:4] + ('...' if len(word) > 4 else '')

# print(shorten_word('Serendipity'))

# for word in word_list...
# print(list(map(shorten_word, word_list)))
# for word in map(shorten_word, word_list):
#     print(word)

for word in map(lambda word: word[:4] + ('...' if len(word) > 4 else ''), word_list):
    print(word)
