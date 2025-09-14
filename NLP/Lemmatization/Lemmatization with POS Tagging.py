import nltk
from nltk import pos_tag, word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# Download required resources (only first time)
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")  # NEW fix
nltk.download("wordnet")
nltk.download("omw-1.4")

# Function to map POS tags
def get_wordnet_pos(word):
    tag = pos_tag([word])[0][1][0].upper()
    tag_dict = {
        "J": wordnet.ADJ,
        "N": wordnet.NOUN,
        "V": wordnet.VERB,
        "R": wordnet.ADV
    }
    return tag_dict.get(tag, wordnet.NOUN)  # default is noun

# Lemmatizer
lemmatizer = WordNetLemmatizer()

# Example sentence
sentence = "The studies were better when he was running"
words = word_tokenize(sentence)

# Lemmatize each word with correct POS
lemmatized = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in words]

print("Original   :", words)
print("Lemmatized :", lemmatized)
