import re
from nltk.util import ngrams
 
s = "Natural-language processing (NLP) is an area of computer science " \
    "and artificial intelligence concerned with the interactions " \
    "between computers and human (natural) languages."
print('original',s)
 
s = s.lower()
s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
print('process',s)

tokens = [token for token in s.split(" ") if token != ""]
output = list(ngrams(tokens, 5))
print('output',output)

'''
('original', 'Natural-language processing (NLP) is an area of computer science and artificial intelligence concerned with the interactions between computers and human (natural) languages.')


('process', 'natural language processing  nlp  is an area of computer science and artificial intelligence concerned with the interactions between computers and human  natural  languages ')


('output', [('natural', 'language', 'processing', 'nlp', 'is'), ('language', 'processing', 'nlp', 'is', 'an'), ('processing', 'nlp', 'is', 'an', 'area'), ('nlp', 'is', 'an', 'area', 'of'), ('is', 'an', 'area', 'of', 'computer'), ('an', 'area', 'of', 'computer', 'science'), ('area', 'of', 'computer', 'science', 'and'), ('of', 'computer', 'science', 'and', 'artificial'), ('computer', 'science', 'and', 'artificial', 'intelligence'), ('science', 'and', 'artificial', 'intelligence', 'concerned'), ('and', 'artificial', 'intelligence', 'concerned', 'with'), ('artificial', 'intelligence', 'concerned', 'with', 'the'), ('intelligence', 'concerned', 'with', 'the', 'interactions'), ('concerned', 'with', 'the', 'interactions', 'between'), ('with', 'the', 'interactions', 'between', 'computers'), ('the', 'interactions', 'between', 'computers', 'and'), ('interactions', 'between', 'computers', 'and', 'human'), ('between', 'computers', 'and', 'human', 'natural'), ('computers', 'and', 'human', 'natural', 'languages')])

'''

