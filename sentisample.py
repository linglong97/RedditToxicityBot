import nltk
from ntlk.corpus import sentiwordnet as swn
import re
import math

#testing file for using some common lexicon based sentiment analysis methods

text = raw_input()

def parse(text):
    output = []
    sentences = nltk.sent_tokenize(text)
    stokens = [nltk.word_tokenize(sent) for el in sentences]
    for el in stokens:
        output.append(nltk.pos_tag(el))
    return output

def sentiment_scores(text):
    scores = []
    lemmatizer = nltk.WordNetLemmatizer()
    for i, el in enumerate(text):
        new = ''
        lemma = lemmatizer.lemmatize(el[0])
        
    
