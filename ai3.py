sentence = "python is great and python is easy"
words = sentence.split()
word_count = {}
for word in words:
	word_count[word] = word_count.get(word, 0) + 1
print("Word occurrences:", word_count)
    