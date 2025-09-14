#(improved version of Porter, supports multiple languages)

from nltk.stem import SnowballStemmer

snow = SnowballStemmer('english')

words = ["connection", "connections", "connected", "connecting", "connectionist"]

for w in words:
    print(w, "->", snow.stem(w))