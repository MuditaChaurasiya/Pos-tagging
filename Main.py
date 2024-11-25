import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Ensure you have the necessary NLTK data
nltk.download('punkt')  # For tokenizing words
nltk.download('averaged_perceptron_tagger')  # For POS tagging

# Input text
text = "Natural Language Processing is fascinating."

# Tokenize the text into words
tokens = word_tokenize(text)

# Perform POS tagging
pos_tags = pos_tag(tokens)

# Output the POS tags
print("Word and POS Tags:")
for word, tag in pos_tags:
    print(f"{word}: {tag}")
