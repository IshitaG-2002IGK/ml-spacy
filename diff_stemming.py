# pip install -U spacy
# python -m spacy download en_core_web_sm
'''
Created on 
Course work: 
@author: Ishita
Source:
https://medium.com/@tusharsri/nlp-a-quick-guide-to-stemming-60f1ca5db49e
    
'''

# Import necessary modules
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
def startpy():

    porter = PorterStemmer()
    lancaster=LancasterStemmer()
    word_list = ["friend", "friendship", "friends", "friendships","stabil","destabilize","misunderstanding","railroad","moonlight","football"]
    print("{0:20}{1:20}{2:20}".format("Word","Porter Stemmer","lancaster Stemmer"))
    for word in word_list:
        print("{0:20}{1:20}{2:20}".format(word,porter.stem(word),lancaster.stem(word)))

if __name__ == '__main__':
    startpy()