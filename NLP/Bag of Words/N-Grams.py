import nltk
from nltk import word_tokenize
from nltk.util import ngrams

nltk.download('punkt')

sentence = "I love natural language processing"
tokens = word_tokenize(sentence)

# Unigrams
unigrams = list(ngrams(tokens, 1))
print("Unigrams:", unigrams)

# Bigrams
bigrams = list(ngrams(tokens, 2))
print("Bigrams:", bigrams)

# Trigrams
trigrams = list(ngrams(tokens, 3))
print("Trigrams:", trigrams)
