#!c:/Python26/python.exe
 
from xml.dom.minidom import parse
import xml.dom.minidom
 

def readFile(filename):
	datasource=open(filename)
	global doc
	doc=parse(datasource)

	return doc

def getNews():
	i=0

	newslist=[]
	
	while i<len(doc.firstChild.childNodes[0].childNodes):
			
			newslist.append("Title:" + doc.firstChild.childNodes[0].childNodes[i].firstChild.data+"\nLink:" + doc.firstChild.childNodes[0].childNodes[i+1].firstChild.data+"\nDescription" + doc.firstChild.childNodes[0].childNodes[i+2].firstChild.data+"\nPublished Date" + doc.firstChild.childNodes[0].childNodes[i+3].firstChild.data)	
			
			i+=4    
	return newslist
 

 
readFile('BrandeisNow.xml')
print getNews()    
