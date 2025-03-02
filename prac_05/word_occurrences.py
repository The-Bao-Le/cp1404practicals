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

max_length = max(len(word) for word in words)
for word in sorted(word_count):
    print(f"{word:{max_length}} : {word_count[word]}")