import cgi
import sys
import time
import datetime
import session
import Cookie
import random
import MySQLdb

import cgitb; cgitb.enable()

# Some hosts will need to have document_root appended
# to sys.path to be able to find user modules
import os

def database_connection():
	db = MySQLdb.connect("127.0.0.1","root","brandeis","oneportal" )
	return db

def getCookie(key):
	try:
		cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
		return cookie[key].value
	except:
		return ""
	
def isLoggedIn():
	#sess=init()
	isloggedin = getCookie('isloggedin')
	return isloggedin

def getUserId(userName):
	db = database_connection()
	cursor = db.cursor()
	sql = "select user_id from user where login_id='%s'" %(userName) 
	#print sql
	cursor.execute(sql)
	actor_result = cursor.fetchall()
	for row in actor_result:
		return row[0]

def getUserName():
	user_id = getCookie("user_id")
	#print "user_id is %s" %(user_id)
	return user_id
	
def getGmailAcct():
	db = database_connection()
	cursor = db.cursor()
	sql = "select gmail_login,gmail_pwd,login_id from user where user_id='%s'" %(getUserId(getUserName()) )
	#%(getUserName()) 
	print sql
	cursor.execute(sql)
	results = cursor.fetchall()
	for row in results:
		username= row[0]
		password = row[1]
		local = row[2]
	return (username,password,local)

def getLocal():
	db = database_connection()
	cursor = db.cursor()
	sql = "select gmail_login,gmail_pwd,login_id from user where user_id='%s'" %(getUserId(getUserName()))
	
	cursor.execute(sql)
	results = cursor.fetchall()
	for row in results:
		local = row[2]
	return local
	
def isAdmin():
	db = database_connection()
	cursor = db.cursor()
	sql = "select type from login where login_name='%s'" %(getUserName()) 
	#print sql
	cursor.execute(sql)
	results = cursor.fetchall()
	for row in results:
		return str(row[0])
	return '0'
	
def userExists(custId):
	db = database_connection()
	cursor = db.cursor()
	sql = "select * from customer where Customer_ID='%s'" %(custId) 
	#print sql
	cursor.execute(sql)
	results = cursor.fetchall()
	if(len(results)==0):
		return '0'
	else:
		return '1'
		
		

def cardLuhnChecksumIsValid(card_number):
    """ checks to make sure that the card passes a luhn mod-10 checksum """

    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1
	

    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return ( (sum % 10) == 0 )		
