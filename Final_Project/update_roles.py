#!c:/Python26/python.exe
import cgi
import cgitb
cgitb.enable()
import header
import utility  
 
from db import database_connection
print "Content-type: text/html; charset=iso-8859-1\n\n" 

db = database_connection()
cursor = db.cursor()
print '''<script language=javascript>function form_validation(){
		var form_error=false;
		var error_message = "";
	 
		if(document.dvd_form.dvd_name.value == "")
		{
		error_message+='Please Enter DVD Name.\\n';
		form_error = true;
		}
		 	
		if(document.dvd_form.release_date.value == "")
		{
		error_message+='Please Enter Release Date.\\n';
		form_error = true;
		}
		var stripped = document.dvd_form.imdb_rating.value.replace(/[\(\)\.\-\ ]/g, '');  
		if(document.dvd_form.imdb_rating.value == "" || isNaN(parseInt(stripped)))
		{
		error_message+='Please Enter Valid IMDB Rating.\\n';
		form_error = true;
		}
		var stripped = document.dvd_form.no_dvd.value.replace(/[\(\)\.\-\ ]/g, '');  
		if(document.dvd_form.no_dvd.value == "" || isNaN(parseInt(stripped)) )
		{
		error_message+='Please Enter Number Of DVD.\\n';
		form_error = true;
		}
		if(document.dvd_form.director.value == "")
		{
		error_message+='Please Enter Director of Movie.\\n';
		form_error = true;
		}
		
		if (form_error){
		alert(error_message);
		return false;
		}}
	</script>'''

def generate_roleform():
	form = cgi.FieldStorage()
	role_id=form["role_id"].value
	 
	sql_role = 'SELECT m.keywords,m.emails,m.names,r.role_name,r.role_id FROM mapping AS m,roles AS r WHERE m.role_id = r.role_id AND m.role_id=%s'%(role_id)
	#print sql_role
 
	cursor.execute(sql_role)
	results=cursor.fetchall()
	for row in results:
		keywords = row[0]
		emails = row[1]
		names = row[2]
		role_name = row[3]
		role_id = row[4]
		 
	print '''<HTML><HEAD>'''
	print header.printHeader()
	print '''<TITLE>
			SwiftMail :: Update Roles 
			</TITLE></HEAD>
			<body>'''
	#print header.printHeader()
	#print leftNav.printLeftNav()
	print '''<div class="left-side" style="width:745px;" >'''
	print '''<div  class="formbox">'''
	 
	print '''<form name='role_form' action='update_roles.py' onsubmit="return form_validation();">
			<table width="745" border="0" class="formboxcontent">
			  <tr>
				<td colspan="2"><div align="left" class="formboxheader"><b>Update Fields</b></div></td>
			  </tr>
			  <tr>
				<td>Enter Role Name : </td>
				<td><input name="role_name" type="text" size="60" value='%s'/></td>
			  </tr>
			  <tr>
				<td>Enter Keyword for the role:(keywords seperated by semicolon)</td>
				<td><textarea name="keyword" cols="50" rows="5">%s</textarea> </td>
			  </tr>
			  <tr>
				<td>Enter Email Address for the role:(Email Address seperated by semicolon)</td>
				<td><textarea name="email" cols="50" rows="5">%s</textarea></td>
			  </tr>
			  <tr>
				<td>Enter Name for the role:(Name seperated by semicolon) </td>
				<td><textarea name="name" cols="50" rows="5">%s</textarea></td>
			  </tr>
			   
			  <tr>
				<td><input name="submit" type="submit" value=" UPDATE " />
				<INPUT TYPE = hidden NAME = 'action' VALUE ='display'>
				<INPUT TYPE =hidden NAME ='role_id' value='%s'>
				<INPUT TYPE=button VALUE = "Go Back" ONCLICK = 'window.history.back()'/>
				</td>
				<td>&nbsp;</td>
			  </tr>
			  <tr>
				<td>&nbsp;</td>
				<td>&nbsp;</td>
			  </tr>
			</table></form>
			</div></div>
			'''%(role_name,keywords,emails,names,role_id)
	print '''</body></html>'''	
	#print footer.printFooter()

def display_roledata(role_id,role_name,keyword,email,name):
	 
	db = database_connection()
	cursor = db.cursor()
	
	sql_mappingupdate = 'UPDATE mapping SET keywords="%s",emails="%s",names="%s" WHERE role_id="%s"'%(keyword,email,name,role_id)
	
	sql_role = 'UPDATE roles SET role_name = "%s" where role_id = "%s"' %(role_name,role_id)
	#print sql_dvdupdate
	cursor.execute(sql_mappingupdate)
	db.commit()
	cursor.execute(sql_role)
	db.commit()
	#print header.printHeader()
	#print leftNav.printLeftNav()
	print header.printHeader()
	print '''<div class="left-side" style="width:745px;" >'''
	print '''<div  class="formbox" align="center">'''
	 
	print '<p>Roles Info has been updated Successfully<p>'
	print '<a href="display_roles.py">Go back to Display Roles</a>'
	print '''</div></div>'''
	#print footer.printFooter()

def main():
	form = cgi.FieldStorage()
	if(form.has_key("action")):
		if form["action"].value == "display":
			 display_roledata(form["role_id"].value,form["role_name"].value,form["keyword"].value,form["email"].value,form["name"].value)
			
	else:
		generate_roleform()

main()