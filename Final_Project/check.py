#!c:/Python26/python.exe
import cgi
import cgitb

import sys
import random
import time
import datetime
#import header
#import leftNav
#import footer
import utility
print "Content-type: text/html; charset=iso-8859-1\n\n"
cgitb.enable()
form = cgi.FieldStorage()

if(form.has_key("user_name")):
	user_name = (form["user_name"].value)
	db = utility.database_connection()
	cursor = db.cursor()
	sql_select = 'select * from user where login_id = "%s"' %user_name
	cursor.execute(sql_select)
	results=cursor.fetchall()
	if(results!=None and len(results)>0):
		print '''<html><body><font color="red">This data already exists please change user name</font></body></html>'''
		