import nltk
from nltk.tokenize import sent_tokenize

text =  "Mr. John works at Google. He lives in the U.S.A. Do you know him?"

sentences = sent_tokenize(text)
print(sentences)
print('number of sentences:', len(sentences))