import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = ('MY NAME IS NIDHI. I AM 23 YEARS OLD')

#sentence tokenize
sentences = sent_tokenize(text)
print('sentence tokenization:', sentences)

#word tokenize
words = word_tokenize(text)
print('word tokenization:', words)