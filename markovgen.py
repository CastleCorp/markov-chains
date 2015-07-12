import sys
from pprint import pprint
import markovify

# Get corpus text as a string
with open("corpus.txt") as f:
    corpus = f.read()

# Build chain model
corpus_model = markovify.Text(corpus)

# Print five randomly generated sentences
for i in range(5):
    print(corpus_model.make_sentence())
