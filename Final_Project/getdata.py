#!c:/Python26/python.exe
import cgi
import header
import utility 
import header
import datetime

#import cgitb
#cgitb.enable()
from db import database_connection
#print "Content-type: text/html; charset=iso-8859-1\n\n"

def getGmailAcct():
	user_id = utility.getUserId(utility.getUserName())
	
	db = database_connection()
	cursor = db.cursor()
	sql = "select gmail_login,gmail_pwd,login_id from user where user_id='%s'" %user_id
	#%(getUserName()) 
	#print sql
	cursor.execute(sql)
	results = cursor.fetchall()
	for row in results:
		username= row[0]
		password = row[1]
		local = row[2]
		#print username
	return (username,password,local)

def getLocal():
	user_id = utility.getUserId(utility.getUserName())
	db = database_connection()
	cursor = db.cursor()
	sql = "select gmail_login,gmail_pwd,login_id from user where user_id='%s'" %user_id
	
	cursor.execute(sql)
	results = cursor.fetchall()
	for row in results:
		local = row[2]
	return local
		