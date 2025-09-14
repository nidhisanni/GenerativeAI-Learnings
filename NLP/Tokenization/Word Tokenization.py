import nltk
from nltk.tokenize import word_tokenize

text = "The quick brown fox jumps over the lazy dog."

words = word_tokenize(text)
print(words)
print('number of tokens:', len(words))