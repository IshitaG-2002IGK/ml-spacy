'''
Created on 
Course work: 
@author: Ishita
Source:https://www.machinelearningplus.com/spacy-tutorial-nlp/#namedentityrecognition
Note : Have a look at this text “John works at Google1″. In this, ” John ” and ” Google ” are names of a person and a company. These words are referred as named-entities. They are real-world objects like name of a company , place,etc..
    
'''
import spacy
def startpy():

# Preparing the spaCy document
    nlp = spacy.load("en_core_web_sm")
    text='Tony Stark owns the company StarkEnterprises . Emily Clark works at Microsoft and lives in Manchester. She loves to read the Bible and learn French'
    doc=nlp(text)


    # Printing the named entities
    print(doc.ents)
    for entity in doc.ents:
        print(entity.text,'--- ',entity.label_)
    # Using displacy for visualizing NER

# from spacy import displacy
# displacy.render(doc,style='ent',jupyter=True)

    
  
if __name__ == '__main__':
    startpy()