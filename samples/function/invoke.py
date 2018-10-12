import fetch

words = fetch.fetch_words()
words.sort()
print('========================')
print(words)
print('========================')
print(set(words))
sortedWords = sorted(set(words))
print('========================')
print(sortedWords)
print('========================')
