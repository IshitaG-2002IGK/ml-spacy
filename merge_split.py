'''
Created on 
Course work: 
@author: Ishita
Source:
    
'''

# Import necessary modules
# Merging and Splitting Tokens with retokenize

import spacy
def startpy():
    pass

# Printing tokens of a text
    nlp = spacy.load("en_core_web_sm")

    text="John Wick is a 2014 American action thriller film directed by Chad Stahelski"
    doc=nlp(text)
    for token in doc:
        print(token.text)

    with doc.retokenize() as retokenizer:
        attrs = {"POS": "PROPN"}
        retokenizer.merge(doc[0:2], attrs=attrs)

    for token in doc:
        print(token.text)

    for token in doc:
        print(token.text,token.pos_)

if __name__ == '__main__':
    startpy()