import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download needed data
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')   

# Sample text
text = "This is an example showing how to remove stopwords using NLTK in Python."

# Tokenize
words = word_tokenize(text)

# Stopwords
stop_words = set(stopwords.words('english'))

# Filter
filtered_words = [word for word in words if word.lower() not in stop_words]

print("Original Words:", words)
print("Filtered Words:", filtered_words)
