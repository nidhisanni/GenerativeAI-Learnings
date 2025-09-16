import nltk
from sklearn.preprocessing import LabelBinarizer
from nltk.tokenize import word_tokenize

sentences = ["I love NLP", "I love Python"]
tokens = []
for sent in sentences:
    tokens.extend(word_tokenize(sent.lower()))

print("Tokens:", tokens)
vocab = sorted(set(tokens))
print("Vocabulary:", vocab)

encoder = LabelBinarizer()
encoder.fit(vocab)

one_hot_vectors = encoder.transform(vocab)

for word, vec in zip(vocab, one_hot_vectors):
    print(f"{word}: {vec}")

sentence = "I love NLP"
tokens = word_tokenize(sentence.lower())

encoded_sentence = [encoder.transform([word])[0] for word in tokens]
print(encoded_sentence)
