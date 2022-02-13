# pip install -U spacy
# python -m spacy download en_core_web_sm


# import nltk
# # nltk.download('punkt')
# from nltk.stem.porter import *

# porterStemmer = PorterStemmer()

# sentence = "compute computer computed computing"
# wordList = nltk.word_tokenize(sentence)

# stemWords = [porterStemmer.stem(word) for word in wordList]

# print(' '.join(stemWords))

# Import necessary modules

from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
def startpy():


    porter = PorterStemmer()
    lancaster=LancasterStemmer()
    #proide a word to be stemmed
    print("Porter Stemmer")
    print(porter.stem("cats"))
    print(porter.stem("trouble"))
    print(porter.stem("troubling"))
    print(porter.stem("troubled"))
    print("Lancaster Stemmer")
    print(lancaster.stem("cats"))
    print(lancaster.stem("trouble"))
    print(lancaster.stem("troubling"))
    print(lancaster.stem("troubled"))


if __name__ == '__main__':
    startpy()