#!c:/Python26/python.exe
import cgi
import header
import cgitb
import utility 
cgitb.enable()
from db import database_connection
print "Content-type: text/html; charset=iso-8859-1\n\n"
customer_id = utility.getUserId(utility.getUserName())

db = database_connection()
cursor = db.cursor()

sql_role = "select a.role_id,a.role_name from roles a, mapping b where a.role_id = b.role_id and b.user_id = '%s'"%customer_id
cursor.execute(sql_role)
results=cursor.fetchall()
#print header.printHeader()
#print leftNav.printLeftNav()
print header.printHeader()
print '''<div class="left-side" style="width:745px;" >'''
print '''<div  class="formbox" align="center">'''
 
print '''<table border='0' class="formboxcontent" align="center">
<tr><td colspan="5"><p><b>Click on the respective Roles to update fields</b></td></tr>
<tr><td><b><u>Role Name</u></b></td></tr>'''
for row in results:
	role_id = row[0]
	role_name = row[1]
	 
	print '''<tr><td><li>'''
	print '<a href ="update_roles.py?role_id=%s">%s</a>'%(role_id,role_name)
	print'''</li></td>'''
print '''<tr><td align='right'><INPUT TYPE=button VALUE = " Cancel " ONCLICK = 'window.history.back()'/></tr></td>'''	 	
print '''</table>'''	
#print footer.printFooter()



	