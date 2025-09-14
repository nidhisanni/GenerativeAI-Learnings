from nltk.tokenize import word_tokenize

from nltk.stem import PorterStemmer

ps = PorterStemmer()

sentence = "Python programmers were playing, studied, and running towards challenges."

words = word_tokenize(sentence)

stemmed_words = [ps.stem(w) for w in words]

print('original:', words)
print('stemmed:', stemmed_words)