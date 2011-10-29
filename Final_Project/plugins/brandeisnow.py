#!c:/Python26/python.exe
import os
import cgi
import cgitb
cgitb.enable()
import urllib2
from xml.dom import minidom
import urllib
from xml.dom.minidom import Document
from xml.dom.ext.reader import Sax2 
from xml.dom.ext import PrettyPrint 
import datetime

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
  
def activate(username,password,local):

  if os.path.exists(os.curdir+"\\users\\"+local)==False:
            os.mkdir(os.curdir+"\\users\\"+local)
            os.mkdir(os.curdir+"\\users\\"+local+"\\xml")
            os.mkdir(os.curdir+"\\users\\"+local+"\\attachments")

  import sys
  rssDocument = load('http://www.brandeis.edu/now/rss.xml')
 
  j = 0
  for item in getElementsByTagName(rssDocument, 'item'):

        if j==10:
          break


	titleval = textOf(first(item, 'title')).encode('ascii','replace')
	linkval= textOf(first(item, 'link')).encode('ascii','replace')
	descriptionval= textOf(first(item, 'description')).encode('ascii','replace')
	pubDateval = textOf(first(item, 'pubDate')).encode('ascii','replace')
	creatorval = textOf(first(item, 'creator', DUBLIN_CORE)).encode('ascii','replace')
	fromval = 'Brandeis Now'
	doc = Document()
    
	datasource = doc.createElement("datasource")
	datasource.appendChild(doc.createTextNode('Brandeis Now'))
	doc.appendChild(datasource)
	
	# Create a <from> element
	from1 = doc.createElement("from")
	from1.appendChild(doc.createTextNode(" "+fromval))
	# Give the <title> element value 
	datasource.appendChild(from1)
	
	# Create a <PubDate> element
	PubDate1 = doc.createElement("date")

        month={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
        components=pubDateval.split()
        date=str(datetime.datetime(int(components[3]),month[components[2]],int(components[1]),int(components[4].split(':')[0]),int(components[4].split(':')[1]),int(components[4].split(':')[2])))

	PubDate1.appendChild(doc.createTextNode(" "+date))
	# Give the <PubDate> element value
	datasource.appendChild(PubDate1) 
		
	# Create a <title> element
	title1 = doc.createElement("subject")
	title1.appendChild(doc.createTextNode(" "+titleval))
	# Give the <title> element value
	datasource.appendChild(title1)
	
	
	# Create a <Description> element
	Description1 = doc.createElement("message")
	Description1.appendChild(doc.createTextNode(" "+descriptionval))
	# Give the <Description> element value
	datasource.appendChild(Description1)
	
	# Create a <link> element
	link1 = doc.createElement("attachment")
	link1.appendChild(doc.createTextNode(" "+linkval))
	# Give the <title> element value
	datasource.appendChild(link1)

	num=len(os.listdir(os.curdir+"\\users\\"+local+"\\xml"))
        			 
	f=open(os.curdir+"\\users\\"+local+"\\xml\\"+str(num+1)+".xml","w")
	doc.writexml(f)
	f.close()
	j+=1
  
		
    
