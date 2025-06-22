"""
Word Occurences
Estimated: 30 minutes
Actual:
"""
text = input("Text: ")
words = text.split()

word_to_count = {}
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

