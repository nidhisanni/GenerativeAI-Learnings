from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "played", "plays", "player", "studies", "studying"]

for w in words:
    print(w, '->', ps.stem(w))