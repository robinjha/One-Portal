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

def con_str():

	user_id = utility.getUserId(utility.getUserName())
	db = database_connection()
	cursor = db.cursor()
	string2=""
	sql_role = 'select role_id from mapping where user_id = %s' %user_id 
	
	cursor.execute(sql_role)
	results_role=cursor.fetchall()
	for row in results_role:
		role_id = row[0]
		sql_keyword = 'select keywords,emails,names from mapping where role_id = %s' %role_id
		
		cursor.execute(sql_keyword)
		results_keyword=cursor.fetchall()
		for row1 in results_keyword:
			keyword = row1[0]
			if keyword:
				string2 = keyword+";"+string2
			
			emails = row1[1]
			if emails:
				string2 =emails+";"+string2
			
			names = row1[2]
			if names:
				string2 =names+";"+string2
	sql_user = 'select login_id from user where user_id = %s' %user_id
	cursor.execute(sql_user)
	results_user=cursor.fetchall()
	for rows in results_user:
		user_name = rows[0]
	
	return (string2,user_name)


