#!c:/Python26/python.exe
import cgi
import cgitb

import sys
import random
import time
import datetime
import header
#import leftNav
#import footer
import utility
print "Content-type: text/html; charset=iso-8859-1\n\n"
cgitb.enable()
form = cgi.FieldStorage()
success=0

if(form.has_key("action")):
	try:
		user_name = (form["user_name"].value)
		password = (form["user_pwd"].value)
		gmail_login = (form["gmail_login"].value)
		gmail_pwd  = (form["gmail_pwd"].value)
		#calendar_login  = (form["calendar_login"].value)
		#calendar_pwd  = (form["calendar_pwd"].value)
		db = utility.database_connection()
		cursor = db.cursor()
		sql_insert = 'insert into user (login_id,password,gmail_login,gmail_pwd) values ("%s","%s","%s","%s")' %(user_name,password,gmail_login,gmail_pwd)
		#print sql_insert
		cursor.execute(sql_insert)
		user_id = cursor.lastrowid
		#print user_id
		sql_role1 = 'insert into mapping (role_id,user_id) values ("2","%s")' %(user_id)
		cursor.execute(sql_role1)
		sql_role2 = 'insert into mapping (role_id,user_id) values ("3","%s")' %(user_id)
		cursor.execute(sql_role2)
		db.commit()
		success=1
	except:
		success=2



print '''
<html>
<head>'''
print header.printHeader()
print '''<script type="text/javascript" src="/others/jquery-1.4.2.min.js"></script>
<script type="text/javascript" src="/others/validation.js"></script>
<script type="text/javascript">
$(document).ready(function(){
    $("#recordCreate").validate();
	
	$("#user_name").change(function() {
	
    $("#submit").removeAttr("disabled");
	$("#error").text('');
	$.get("check.py", 
  { user_name: $("#user_name").val()}, 
  function(data){ 
    $("#error").append(data);
	
	if(data.indexOf("This data already")!=-1){
	
	$("#submit").attr("disabled", "true");
	}
  } 
);
	
});
});

</script>

<style type="text/css">
* { font-family: Verdana; font-size: 96%; }
label { width: 10em; float: left; }
label.error { float: none; color: red; padding-left: .5em; vertical-align: top; }
p { clear: both; }
.submit { margin-left: 12em; }
em { font-weight: bold; padding-right: 1em; vertical-align: top; }
</style>
</head>
<body>

<h1 align = "center"><font = 2>Create an Account</font></h1><br />'''
if (success==1):
	print '''<p align="center"><font color="green">Record has been created</font><a href="login.py">Login Now</a></p>'''
if (success==2):
	print '''<p><font color="red">There was some error creating your account. Contact System Admin</font></p>'''

print '''
<br></br>
<form name="frm1" id="recordCreate" name="recordCreate" action="join_us.py" method = "post">
<table align ="center">
<tr>
<td>User Name</td>
<td><input type="text" name="user_name" id="user_name" class="required"/></td>
<td><font id="error" name="error"></font></td>
</tr>
<tr>
<td>Password</td>
<td><input type="password" name="user_pwd" id="user_pwd" class="required"/></td>
</tr>
<tr>
<td>Gmail Login</td>
<td><input type="text" name="gmail_login" id="gmail_login" class="required email"/></td>
</tr>
<tr>
<td>Gmail Password</td>
<td><input type="password" name="gmail_pwd" id="gmail_pwd" class="required"/></td>
</tr>
 
 
<tr>
</tr>
<input type="hidden" name="action" id="action" value="submit"/>
<td><input type="submit" id="submit" name="submit" value="Create Entry"></td>

</table>
</form>

</body>
</html>




'''

	