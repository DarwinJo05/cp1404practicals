"""
Word Occurrences
Estimated: 30 minutes
Actual: 1 hour 30 minutes
"""
text = input("Text: ")
words = text.split()

word_to_count = {}
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

max_length = max(len(word) for word in word_to_count)

for word in sorted(word_to_count):
    print(f"{word:{max_length}} : {word_to_count[word]}")