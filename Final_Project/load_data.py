#!c:/Python26/python.exe
import cgi
import header
import utility 
import header
import datetime
import getdata
import runner
import insert_email
#import cgitb
#cgitb.enable()
print "Content-type: text/html; charset=iso-8859-1\n\n"
from db import database_connection
 

username,password,local = getdata.getGmailAcct()
runner.dumpData(username,password,local)

insert_email.insert_data()
print header.printHeader()	
print "Loading Your Data......" 
print '''<script language=javascript>
	window.location="http://localhost/video/Final_Project/home.py";</script>
	'''
