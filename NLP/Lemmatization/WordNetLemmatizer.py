from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize('studies'))
print(lemmatizer.lemmatize('studying'))
print(lemmatizer.lemmatize('better'))


#By default, NLTK’s WordNetLemmatizer assumes every word is a noun.