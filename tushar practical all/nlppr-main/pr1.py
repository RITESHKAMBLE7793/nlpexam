# Step 1: Import library
import re

# Step 2: Sample text
text = "Hello Buddy! This is AI & Machine Learning. Let's learn together :)"

# Step 3: Convert to lowercase (Normalization)
text = text.lower()

# Step 4: Remove punctuation
text = re.sub(r'[^a-z\s]', '', text)

# Step 5: Tokenization (split into words)
tokens = text.split()

# Step 6: Print results
print("Original Text:", text)
print("Tokens:", tokens)




#Advance here

import nltk
from nltk.tokenize import word_tokenize
import string

# Download once
nltk.download('punkt')

text = "Hello Buddy! This is AI & Machine Learning."

# Lowercase
text = text.lower()

# Tokenization
tokens = word_tokenize(text)

# Remove punctuation
tokens = [word for word in tokens if word not in string.punctuation]

print(tokens)