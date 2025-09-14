import nltk
from nltk import pos_tag, word_tokenize

# Download punkt + tagger (only once)
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")  # for newer versions

# Example sentence
text = "The quick brown fox jumps over the lazy dog"

# Tokenize
words = word_tokenize(text)

# POS Tagging
pos_tags = pos_tag(words)

print("Words      :", words)
print("POS Tags   :", pos_tags)
