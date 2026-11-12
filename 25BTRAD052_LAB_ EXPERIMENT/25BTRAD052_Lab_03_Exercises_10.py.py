sentence = input("Enter a sentence: ")

frequency = {}

for word in sentence.lower().split():
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)