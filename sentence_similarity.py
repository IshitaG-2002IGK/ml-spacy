import spacy
def startpy():
# this loads the wrapper
    nlp = spacy.load('en_core_web_sm')

    # your sentences
    search_doc = nlp("This was very strange argument between american and british person")

    main_doc = nlp("He was from Japan, but a true English gentleman in my eyes, and another one of the reasons as to why I liked going to school.")

    print(main_doc.similarity(search_doc))
    # this will print 0.310783598221594
    
if __name__ == '__main__':
    startpy()