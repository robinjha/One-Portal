import os
import sys
from xml.dom.minidom import parse, parseString
from nltk.corpus import wordnet
import datetime

def readFile(filename):
    global doc1
    global datasource1
    datasource1=open(filename)
    doc1=parse(datasource1)

def closeFile():
    datasource1.close()

def getDataSource():
    return doc1.childNodes[0].firstChild.data

def getFrom():
    return doc1.childNodes[0].childNodes[1].firstChild.data

def getDate():
    return doc1.childNodes[0].childNodes[2].firstChild.data

def getSubject():
    return doc1.childNodes[0].childNodes[3].firstChild.data

def getMessage():
    return doc1.childNodes[0].childNodes[4].firstChild.data

def getAttachments():
    return doc1.childNodes[0].childNodes[5].firstChild.data.split()

def getPluginList():

    filteredList=[]
    
    l=os.listdir(os.curdir+"\\plugins\\")

    

    for i in l:
        if i.endswith('.py'):
            filteredList.append(i.split('.')[0])

    return filteredList

def dumpData(username,password,local):
 

    lis=getPluginList()
    
    for i in lis:

        sys.path.append(os.curdir+"\\plugins\\")
        
        module=__import__(i)

        module.activate(username,password,local)

def findWords(keys):

    global vocabs

    vocabs=[]

    for i in keys:

        dictionary_subset=wordnet.synsets(i)

        for j in dictionary_subset:


            for k in j.lemma_names:

                
                vocabs.append(k)


def xmlReadandAnalyze(wordList,local):

    words=[]

    syn=[]

    finals=[]

    wordList=wordList.split(';')    

    #findWords(wordList)    
      
    files=os.listdir(os.curdir+"\\Users\\"+local+"\\xml")

    for f in files:

        #print f

        readFile(os.curdir+"\\Users\\"+local+"\\xml\\"+f)

        total=str(getDataSource())+' '+str(getFrom())+' '+str(getDate())+' '+str(getSubject())+' '+str(getMessage())+' '+str(getAttachments())

        
        #print total
        
        for j in total.split():

            if j in wordList:

                words.append(j)

            #if j in vocabs:
                 #syn.append(j)       

        
        finals.append((str(getDataSource().encode('ascii','replace')),str(getFrom().encode('ascii','replace')),str(getDate().encode('ascii','replace')),str(getSubject()),str(getMessage()),str(getAttachments()),words))
        
        closeFile()
    return finals

#dumpData()
#xmlReadandAnalyze('urgent;meeting;deepali')

