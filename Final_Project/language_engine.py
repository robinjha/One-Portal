import nltk
from sets import Set
from nltk.corpus import wordnet
import re


def setKeywords(words):

    global keys
    keys=words


def findWords():

    global vocabs

    vocabs=Set()

    for i in keys:

		dictionary_subset=wordnet.synsets(i)
		#print dictionary_subset
		for j in dictionary_subset:
			 
			for k in j.lemma_names:
				vocabs.add(k)

def checksubString(String):

    for i in vocabs:
        if i.find(String)!=-1:
            return True

    return False


def findContext():

    f=open('j.txt')
    lines=f.readlines()
    stats=0
    freq=0
    line_number=0
    k=0
    x_re=re.compile(r'[<> > < >= <= != = ) , .]')
    for i in lines:

        t=x_re.split(i)
        freq=0
        
        
        for j in t:
            
        
            
            if j in vocabs:
                freq+=1
                    
            

        if freq>stats:
            stats=freq
            line_number=k
              
        print line_number   
        k+=1
    
    print "Subject of the E-mail is:\n "+lines[line_number]




setKeywords(['monday','urgent','meeting','emergency','party','Director','conference','tuesday','wednesday','thursday','friday','saturday','sunday','days','years','months','January','February','March','April','May','June','July','August','September','October','November','December'])
findWords()
findContext()
