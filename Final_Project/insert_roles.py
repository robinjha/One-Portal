#!c:/Python26/python.exe
import cgi
import cgitb
cgitb.enable()
import header
import utility 
from db import database_connection
print "Content-type: text/html; charset=iso-8859-1\n\n"
form = cgi.FieldStorage()

print '''<script language=javascript>function form_validation(){
		var form_error=false;
		var error_message = "";
	 
		if(document.form_role.role_name.value == "")
		{
		error_message+='Please Enter Role Name.\\n';
		form_error = true;
		}
		if(document.form_role.keyword.value == "")
		{
		error_message+='Please Enter Keywords for the role.\\n';
		form_error = true;
		}
		if (document.form_role.email.value.indexOf ('@',0) == -1 || document.form_role.email.value.indexOf ('.',0) == -1)
		{
		error_message+='Please Enter Valid E-mail address for the role.\\n';
		form_error = true;
		}	

		if(document.form_role.name.value == "")
		{
		error_message+='Please Enter Name for the role.\\n';
		form_error = true;
		}
		 
		if (form_error){
		alert(error_message);
		return false;
		}}
	</script>'''
	
 
def generate_form(err):
	 
	print '''<html>'''
	print header.printHeader()		
	print '''<head>
			<link rel="stylesheet" type="text/css" href="/others/styles.css" /></link>
			</head>
			
			<title>SwiftMail::Insert Roles </title>
			<body>
			<table align='center' width='800' border='0' class='pagecontent'>'''
	if (err == 1):
		print "<tr><td>&nbsp;</td><td><font color='#FF0000'>Please Enter Role again,Roles already exists!</font></td></tr>"
	print '''<form name="form_role" action="insert_roles.py" onsubmit="return form_validation();">
			  <tr>
				<td colspan="2"><b>Insert Roles</b></td>
			  </tr>
			  <tr>
				<td colspan="2">&nbsp;</td>
			  </tr>
			  <tr>
				<td>Enter Role Name : </td>
				<td><input name="role_name" type="text" size="60"></td>
			  </tr>
			  <tr>
				<td>Enter Keyword for the role:(keywords seperated by semicolon)</td>
				<td>
				<textarea name="keyword" cols="50" rows="5">'''
	if(err == 1):
		try:
			print "%s"%(form["keyword"].value)
		except:
			print ""				
	print '''</textarea>
				</td>
			  </tr>
			  <tr>
				<td>Enter Email Address for the role:(Email Address seperated by semicolon)</td>
				<td><textarea name="email" cols="50" rows="5">'''
	if(err == 1):
		try:
			print "%s"%(form["email"].value)
		except:
			print ""			
	print '''</textarea></td>
			  </tr>
			  <tr>
				<td>Enter Name for the role:(Name seperated by semicolon)</td>
				<td><textarea name="name" cols="50" rows="5">'''
	if(err == 1):
		try:
			print "%s"%(form["name"].value)
		except:
			print ""			
	print'''</textarea></td>
			  </tr>
			  <tr>
			  <td>&nbsp;</td>
				<td><div align="left">
				  <input name=" Submit " type="submit" value=" Submit " />
				  <INPUT TYPE=button VALUE = " Go Back " ONCLICK = 'window.history.back()'/>
				  <INPUT TYPE = hidden NAME = 'action' VALUE ='display'>
				   
				</div></td>
			  </tr>
			  </form>
			</table>
			</body>
			</html>'''
			
def insert_roles(user_id,role_name,keyword,email,name):

	db = database_connection()
	cursor = db.cursor()
	 
	sql_validate = 'select role_name from roles where role_name = "%s"' %(role_name)
	
	cursor.execute(sql_validate)
	results1=cursor.fetchall()
	
	if results1:
		generate_form(1)
	else:
		sql_role = 'INSERT INTO roles(role_name) VALUES("%s")'%(role_name)
	 
		cursor.execute(sql_role)
		db.commit()
		role_id = cursor.lastrowid
		#keywords = keyword.strip().split(";")
		#print len(keywords) 
		#for keyword in keywords: 
		sql_mapping = 'INSERT INTO mapping(role_id,user_id,keywords,emails,names) VALUES("%s","%s","%s","%s","%s")'%(role_id,user_id,keyword,email,name)
		#print sql_mapping
		cursor.execute(sql_mapping)
		db.commit()
		print '''<HTML>'''
		print header.printHeader()
 
		print '''<TITLE>SwiftMail::Insert Roles </TITLE><body>'''
		 
		#print leftNav.printLeftNav()
		
		print '''<div class="left-side" style="width:745px;" >'''
		print '''<table align="center" border='0'><tr><td>&nbsp;</td></tr></table>'''
		print 'Roles has been created successfully! '
		print "<A HREF='home.py'> Go Back </A></div>"
		#print footer.printFooter()
		print '''</body></html>'''		
 
	
	
def main():
	form = cgi.FieldStorage()
	if(form.has_key("action")):
		customer_id = utility.getUserId(utility.getUserName())
		if form["action"].value == "display":
			if "keyword" not in form:
				keywords= ""
			else:
				keywords = form["keyword"].value
				
			if "email" not in form:
				emails= ""
			else:
				emails = form["email"].value	
				
			if "name" not in form:
				names= ""
			else:
				names = form["name"].value	
				
			insert_roles(customer_id,form["role_name"].value,keywords,emails,names)
			
	else:
		generate_form(0)

main()   

   



