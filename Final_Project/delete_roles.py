#!c:/Python26/python.exe
import cgi
import header
import cgitb
import utility 
cgitb.enable()
from db import database_connection
print "Content-type: text/html; charset=iso-8859-1\n\n"
customer_id = utility.getUserId(utility.getUserName())


def generate_deleteform():
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
	 
	print '''<form name="form_delete" action="delete_roles.py"><table border='1' class="formboxcontent">
	<tr><td colspan="5"><b>Click on the respective Roles to Delete</b></td></tr>
	<tr><td colspan='1'>&nbsp;</td><td><b>Role Name</b></td></tr>'''
	for row in results:
		role_id = row[0]
		role_name = row[1]
		 
		print '''<tr><td><input name="role_id" type="radio" value="%d" /></td><td>'''%role_id
		print role_name
		print'''</td>'''
	print '''<tr><td>&nbsp;</td><td align='right'> <input name="btn_delete" type="submit" value="Delete" />
			<INPUT TYPE = hidden NAME = 'action' VALUE ='display'>
			
	</tr></td>'''	 	
	print '''</table></form>'''	
	#print footer.printFooter()

def delete_roledata(role_id):
		 
	db = database_connection()
	cursor = db.cursor()
	sql_delete2 = 'DELETE FROM mapping WHERE role_id=%s'%(role_id) 
	cursor.execute(sql_delete2)
	db.commit()
	sql_delete = 'DELETE FROM roles WHERE role_id=%s'%(role_id)
	cursor.execute(sql_delete)
	db.commit()
	
	print header.printHeader()
 
	#print leftNav.printLeftNav()
	print '''<div class="left-side" style="width:745px;" >'''
	print '''<div  class="formbox" align="center">'''
	 
	print '<p>Roles has been deleted Successfully<p>'
	print '<a href="display_roles.py">Go back to Display Roles</a>'
	print '''</div></div>'''
	#print footer.printFooter()	
	
def main():
	form = cgi.FieldStorage()
	if(form.has_key("action")):
		if form["action"].value == "display":
			 delete_roledata(form["role_id"].value)
			
	else:
		generate_deleteform()

main()



	