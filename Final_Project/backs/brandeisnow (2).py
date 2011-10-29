#!c:/Python26/python.exe
import cgi
import cgitb
cgitb.enable()
print "Content-type: text/html; charset=iso-8859-1\n\n"
import urllib2
from xml.dom import minidom
import urllib
from xml.dom.minidom import Document
from xml.dom.ext.reader import Sax2 
from xml.dom.ext import PrettyPrint 
import os

# Create the minidom document
doc = Document()


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
  
def xmlSplit(xml_filename):
	reader = Sax2.Reader() 
	my_dom = reader.fromUri(xml_filename) 
	steps = my_dom.getElementsByTagName('datasource') 
	i=1 
	for step in steps: 
			num=len(os.listdir(os.curdir+"\\users\\"+username+"\\xml"))
			tmp = file(os.curdir+"\\users\\"+username+"\\xml\\"+'%s.xml'%(num+1),'w')
			#tmp.write('<?xml version="1.0" encoding="ISO-8859-1" ?>\n') 
			PrettyPrint(step , tmp , encoding='ISO-8859-1') 
			tmp.close() 
			i+=1 
	
def activate(username,password):

  import sys
  rssDocument = load('http://www.brandeis.edu/now/rss.xml')
 
  maincard = doc.createElement("OnePortal")
 
  doc.appendChild(maincard)
  
  for item in getElementsByTagName(rssDocument, 'item'):
	titleval = textOf(first(item, 'title')).encode('ascii','replace')
	linkval= textOf(first(item, 'link')).encode('ascii','replace')
	descriptionval= textOf(first(item, 'description')).encode('ascii','replace')
	pubDateval = textOf(first(item, 'pubDate')).encode('ascii','replace')
	creatorval = textOf(first(item, 'creator', DUBLIN_CORE)).encode('ascii','replace')
	fromval = 'Brandeis Now'
    
	news = doc.createElement("datasource")
	news.appendChild(doc.createTextNode('Brandeis Now'))
	maincard.appendChild(news)
	
	# Create a <from> element
	from1 = doc.createElement("from")
	news.appendChild(from1)
	# Give the <title> element value
	fromtext = doc.createTextNode(" "+fromval)
	from1.appendChild(fromtext)
	
	# Create a <PubDate> element
	PubDate1 = doc.createElement("date")
	news.appendChild(PubDate1)
	# Give the <PubDate> element value
	PubDatetext = doc.createTextNode(" "+pubDateval)
	PubDate1.appendChild(PubDatetext) 
		
	# Create a <title> element
	title1 = doc.createElement("subject")
	news.appendChild(title1)
	# Give the <title> element value
	titletext = doc.createTextNode(" "+titleval)
	title1.appendChild(titletext)
	
	
	# Create a <Description> element
	Description1 = doc.createElement("message")
	news.appendChild(Description1)
	# Give the <Description> element value
	Descriptiontext = doc.createTextNode(" "+descriptionval)
	Description1.appendChild(Descriptiontext)
	
	# Create a <link> element
	link1 = doc.createElement("attachment")
	news.appendChild(link1)
	# Give the <title> element value
	linktext = doc.createTextNode(" "+linkval)
	link1.appendChild(linktext)
	 

  #Print our newly created XML
 
  if os.path.exists(os.curdir+"\\users\\"+username)==False:
            os.mkdir(os.curdir+"\\users\\"+username)
            os.mkdir(os.curdir+"\\users\\"+username+"\\xml")
            os.mkdir(os.curdir+"\\users\\"+username+"\\attachments")



  
  xml_filename =os.curdir+"\\temp\\"+username+'BrandeisNow.xml'
  f=open(xml_filename,'w')
  doc.writexml(f)
  f.close()
  
 
  xmlSplit(xml_filename)
  os.remove(os.curdir+"\\temp\\"+username+"BrandeisNow.xml")
  	

    
