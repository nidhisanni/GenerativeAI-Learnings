from nltk.tokenize import BlanklineTokenizer

text = """This is sentence one.

This is sentence two.

And this is sentence three."""

tokens = BlanklineTokenizer().tokenize(text)
print(tokens)
