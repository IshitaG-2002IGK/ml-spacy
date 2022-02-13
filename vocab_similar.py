# Note: vocab: stores data shared across multiple documents. Strings are stored only once in the StringStore via nlp.vocab.strings

import spacy

def startpy():

   nlp = spacy.load('en_core_web_sm') 

   text = "I love maggi"

   doc = nlp(text)

   print("hash value: " , nlp.vocab.strings["maggi"])
   print("string value: ", nlp.vocab.strings[3197928453018144401])
   
if __name__ == '__main__':
    
    startpy()