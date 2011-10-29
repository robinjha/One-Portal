#!c:/Python26/python.exe
import cgi
import cgitb
cgitb.enable()
import os
import urllib2
from xml.dom import minidom
import urllib
from xml.dom.minidom import Document
from xml.dom.ext.reader import Sax2 
from xml.dom.ext import PrettyPrint 
import datetime
import xml.dom.minidom

# Create the minidom document



DEFAULT_NAMESPACES = \
  (None, # RSS 0.91, 0.92, 0.93, 0.94, 2.0
  'http://purl.org/rss/1.0/', # RSS 1.0
  'http://my.netscape.com/rdf/simple/0.9/' # RSS 0.90
  )
DUBLIN_CORE = ('http://purl.org/dc/elements/1.1/',)

def load(rssURL):
  return minidom.parse(urllib.urlopen(rssURL))

def getElementsByTagName(node, tagName, possibleNamespaces=DEFAULT_NAMESPACES):
  for namespace in possibleNamespaces:
    children = node.getElementsByTagNameNS(namespace, tagName)
    if len(children): return children
  return []

def first(node, tagName, possibleNamespaces=DEFAULT_NAMESPACES):
  children = getElementsByTagName(node, tagName, possibleNamespaces)
  return len(children) and children[0] or None

def textOf(node):
  return node and "".join([child.data for child in node.childNodes]) or ""
  
def xmlSplit(xml_filename,username,password):
	reader = Sax2.Reader() 
	my_dom = reader.fromUri(xml_filename) 
	steps = my_dom.getElementsByTagName('datasource') 
        print steps
	i=1 
	for step in steps: 
                        num=len(os.listdir(os.curdir+"\\users\\"+username+"\\xml"))
			tmp = file(os.curdir+"\\users\\"+username+"\\xml\\"+'%s.xml'%(num+1),'w') 
			#tmp.write('<?xml version="1.0" encoding="ISO-8859-1" ?>\n') 
			PrettyPrint(step , tmp , encoding='ISO-8859-1') 
                        print step
			tmp.close() 
			i+=1 
	
def activate(username,password):

  
  
  import sys
  rssDocument = load('http://www.brandeis.edu/now/rss.xml')
  
  #maincard = doc.createElement("OnePortal")

  

 
  #doc.appendChild(maincard)
  
  for item in getElementsByTagName(rssDocument, 'item'):
	titleval = textOf(first(item, 'title')).encode('ascii','replace')
	linkval= textOf(first(item, 'link')).encode('ascii','replace')
	descriptionval= textOf(first(item, 'description')).encode('ascii','replace')
	pubDateval = textOf(first(item, 'pubDate')).encode('ascii','replace')
	creatorval = textOf(first(item, 'creator', DUBLIN_CORE)).encode('ascii','replace')
	fromval = 'Brandeis Now'

        doc=Document()

        datasource=doc.createElement('datasource')

        datasource.appendChild(doc.createTextNode('Brandeis Now'))

        
        doc.appendChild(datasource)


        body=doc.createElement('from')

        body.appendChild(doc.createTextNode(fromval))

        datasource.appendChild(body)


        body=doc.createElement('date')

        month={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
        components=str(pubDateval).split()
        date=str(datetime.datetime(int(components[3]),month[components[2]],int(components[1]),int(components[4].split(':')[0]),int(components[4].split(':')[1]),int(components[4].split(':')[2])))


        body.appendChild(doc.createTextNode(date))

        datasource.appendChild(body)


        body=doc.createElement('subject')

        body.appendChild(doc.createTextNode(titleval))

        datasource.appendChild(body)

        body=doc.createElement('message')

        body.appendChild(doc.createTextNode(descriptionval))

        datasource.appendChild(body)


        body=doc.createElement('attachment')

        
        body.appendChild(doc.createTextNode(linkval))
        
        datasource.appendChild(body)


        doc.toprettyxml(indent=" ")

        num=len(os.listdir(os.curdir+"\\users\\"+username+"\\xml"))
          
        f=open(os.curdir+"\\users\\"+username+"\\xml\\"+'%s.xml'%(num+1),'w')
        doc.writexml(f)
        f.close()

	 

  #Print our newly created XML
 
  #print doc.toprettyxml(indent="  ")
  if os.path.exists(os.curdir+"\\users\\"+username)==False:
            os.mkdir(os.curdir+"\\users\\"+username)
            os.mkdir(os.curdir+"\\users\\"+username+"\\xml")
            os.mkdir(os.curdir+"\\users\\"+username+"\\attachments")


  xml_filename = os.curdir+"\\temp\\"+username+"BrandeisNow.xml"
  f=open(xml_filename,'w')
  doc.writexml(f)
  f.close()
  xmlSplit(xml_filename,username,password)
  os.remove(os.curdir+"\\temp\\"+username+"BrandeisNow.xml")
		

    
