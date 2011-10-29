#!c:/Python26/python.exe
import cgi
import cgitb
cgitb.enable()
from db import database_connection
print "Content-type: text/html; charset=iso-8859-1\n\n"

db = database_connection()
cursor = db.cursor()

sql_roles = "SELECT role_id,user_id,role_name FROM roles WHERE user_id='1'"
cursor.execute(sql_roles)
results_roles=cursor.fetchall()

def insert_keywords(user_id,role_id,keyword):

	db = database_connection()
	cursor = db.cursor()
	sql_role = 'INSERT INTO roles(user_id,role_name) VALUES("%s","%s")'%(user_id,role_name)
	cursor.execute(sql_role)
	db.commit()
	role_id = cursor.lastrowid
	sql_mapping = 'INSERT INTO mapping(role_id,user_id,keyword,email,name) VALUES("%s","%s","%s","%s","%s")'%(role_id,user_id,keyword,email,name)
	print sql_mapping
	cursor.execute(sql_mapping)
	db.commit()
 	print '''<HTML>'''
	print '''<TITLE>SwiftMail::Insert Roles </TITLE><body>'''
	#print header.printHeader()
	
	
	#print leftNav.printLeftNav()
	
	print '''<div class="left-side" style="width:745px;" >'''
	print '''<table align="center" border='0'><tr><td>&nbsp;</td></tr></table>'''
	print 'Roles has been created successfully! '
	print "<A HREF='insert_roles.py?user_id=1'> Go Back To Add New Roles </A></div>"
	#print footer.printFooter()
	print '''</body></html>'''		
	

def generate_form():
	print '''
	<html>
	<head>
	<link rel="stylesheet" type="text/css" href="/others/styles.css" /></link>
	</head>
	
	<title>SwiftMail::Insert Keywords </title>
	<body>
	<table width="800" border="0" align="center" class='pagecontent'>
	<form name="frm_keyword" action="insert_keyword.py">
	  <tr>
		<td colspan="2"> Insert Keyword </td>
	  </tr>
	  <tr>
		<td>Please Select Roles</td>
		<td><select name="roles">'''
				
	for row in results_roles:
		role_id = row[0]
		role_name = row[2]
		
		print '<option value="%d">%d%s</option>'%(role_id,role_id,role_name)
	print '''</select></td>
	  </tr>
	  <tr>
		<td>Enter Keywords(keyword seperated by semicolon):</td>
		<td><input name="keyword" type="text" size="45" /></td>
	  </tr>
	  <tr>
		<td>&nbsp;</td>
		<td><input name="submit" type="submit" />
		  <INPUT TYPE=button VALUE = " Go Back " ONCLICK = 'window.history.back()'/>
		  <INPUT TYPE=button VALUE = " Cancel " ONCLICK = 'window.history.back()'/>
		  <INPUT TYPE = hidden NAME = 'action' VALUE ='display'>
		  <INPUT TYPE = hidden NAME = 'user_id' VALUE ='1'>
		</td>
	  </tr>
	  <tr>
		<td><div align="left"></div></td>
		<td>&nbsp;</td>
	  </tr>
	  </form>
	</table>
	</body>
	</html>'''


def main():
	form = cgi.FieldStorage()
	if(form.has_key("action")):
		if form["action"].value == "display":	
			insert_keywords(form["user_id"].value,form["roles"].value,form["keyword"].value)
			
	else:
		generate_form()

main() 