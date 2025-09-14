import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

# Download resources (only first time)
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")  # for newer versions
nltk.download("maxent_ne_chunker")
nltk.download("maxent_ne_chunker_tab")  # NEW fix
nltk.download("words")

# Example sentence
text = "Apple was founded by Steve Jobs in California in 1976"

# Tokenize & POS tag
words = word_tokenize(text)
pos_tags = pos_tag(words)

# Named Entity Recognition
ner_tree = ne_chunk(pos_tags)

print(ner_tree)
ner_tree.draw()
