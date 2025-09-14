#(more aggressive, shorter stems)
from nltk import LancasterStemmer

ls = LancasterStemmer()

words = ["playing", "played", "plays", "player", "studies", "studying"]

for w in words:
    print(w, '->', ls.stem(w))