#!c:/Python26/python.exe
import cgi
import cgitb
cgitb.enable()
print "Content-type: text/html; charset=iso-8859-1\n\n"
import urllib2
from xml.dom import minidom
import urllib
#from xml.dom.minidom import Document
from xml.dom.ext.reader import Sax2 
from xml.dom.ext import PrettyPrint 
reader = Sax2.Reader() 
my_dom = reader.fromUri('BrandeisNow.xml') 
steps = my_dom.getElementsByTagName('datasource') 
i=1 
for step in steps: 
        tmp = file('News%s.xml' % i,'w') 
        #tmp.write('<?xml version="1.0" encoding="ISO-8859-1" ?>\n') 
        PrettyPrint(step , tmp , encoding='ISO-8859-1') 
        tmp.close() 
        i+=1 