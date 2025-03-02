"""
Word Occurrences
Estimate: 20 minutes
Actual:    minutes
"""
text = input("Text: ").strip().lower()
words = text.split()
word_count = {}
for word in words:
    frequency = word_count.get(word, 0)
    word_count[word] = frequency + 1

for word in word_count:
    print(f"{word} : {word_count[word]}")
