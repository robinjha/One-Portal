#!c:/Python26/python.exe
import cgi
import sys
import random
import time
import datetime
import urllib
import utility
import header
import leftNav
import footer
import insert_email
import runner
import con_str
#import getdata
print "Content-type: text/html; charset=iso-8859-1\n\n"



def getUserId():
	form = cgi.FieldStorage()
	return form["txtEmailAddress"].value
	
	
def database_connection():
	import MySQLdb
	db = MySQLdb.connect("127.0.0.1","root","brandeis","oneportal" )
	return db


def check_login():
	db = database_connection()
	cursor = db.cursor()
	form = cgi.FieldStorage()
	success='0'
	
	if (form.has_key("txtEmailAddress") and form.has_key("txtPassword")):
		userName = form["txtEmailAddress"].value
		password = form["txtPassword"].value
		sql="select login_id from user where login_id='%s' and password='%s'" %(userName,password)
		#print sql
		cursor.execute(sql)
		results=cursor.fetchall()
		
		if(results!=None and len(results)>0):
			#import home
			#for row in results:
			#	setUserId(row[0])
			success='1'
			
			#print 'Location: 127.0.0.1/cgi-bin/home.py'
			#home.generate_homepage("","","","")
			#home.main()
	#print '''<script language=javascript>document.cookie = "isloggedin=1"</script>'''
	
	key = "isloggedin"
	
	#utility.setCookie(key,success)
	return success

print '''<script language=javascript>
		function check(){'''
if utility.isLoggedIn()=='1':
	
	print '''
	window.location="http://localhost/video/Final_Project/home.py";
	'''
if check_login()=='1':
	print '''
	document.cookie = "isloggedin=1";
	'''

	print "document.cookie='user_id=%s';" %(getUserId())
	
	
	#username,password,local = getdata.getGmailAcct()
	
	#wordlist,local = con_str.con_str()
	#print username
	#print password
	#runner.dumpData(username,password,local)

	
	
	#insert_email.insert_data()
	print '''
	window.location="http://localhost/video/Final_Project/home.py";
	'''
	
print '''
		}'''
print '''function loginform_validation(){
		var form_error=false;
		var error_message = "";
		var login;
		var password;
		
		if(document.login_form.email.value == "")
		{
		error_message+='Please Enter Email Address.\\n';
		form_error = true;
		}
		if (document.login_form.email.value.indexOf ('@',0) == -1 || document.login_form.email.value.indexOf ('.',0) == -1)
		{
		error_message+='Please Enter Valid E-mail address.\\n';
		login=document.login_form.email.value;
		form_error = true;
		}	
		if(document.login_form.password.value == "")
		{
		error_message+='Please Enter Password.\\n';
		password=document.login_form.password;
		form_error = true;
		}
		 
		if (form_error){
		alert(error_message);
		return false;
		}}

</script>'''	
print '''<HTML>'''
print header.printHeader()
print '''<TITLE>Login Form </TITLE>'''
print '''<BODY onLoad="check();"> '''

#print header.printHeader()
	
	
#print leftNav.printLeftNav()
	
print '''
		
		<div class="left-side" style="width:745px;" >
		
		'''
print '''
	<form name="login_form" action="login.py">
	<div align="center">
	<div  class="formbox">
			<div align="left" class="formboxheader" align="center"><p>LOGIN HERE......</p></div>
			 
			<div class="formboxcontent" align="center">'''
if(check_login()=='0'):
	print '''<div id="login-error">
			<font color="red">Either User Name/Password is not correct. Please try again ......</font>
			</div>'''
print '''
				<div class="formbox-left" style="width:49%" align="center">
					<SPAN class="formfieldtext" >User Name:</SPAN>
					<SPAN>*&nbsp;</SPAN>
				</div>
				<div class="formbox-right">
					<SPAN><input name="txtEmailAddress" type="text" id="txtEmailAddress"   value="user@user.com"></SPAN>
				</div>
				
				<div class="formbox-left" style="width:49%">

					<SPAN class="formfieldtext" >Password:</SPAN>
					<SPAN>*&nbsp;</SPAN>
				 </div>
				<div class="formbox-right">
					<SPAN><input name="txtPassword" type="password" id="txtPassword"></SPAN>
				</div>
				
			</div>
			<br clear="all">

		<div align="center"><input type="submit" src="127.0.0.1/images/user/login.png" alt="Login" value="login" />&nbsp;
		<input type="button" value="reset" onClick="javascript:this.form.reset()"></div>	
	</div>
	<div class="formboxcontent">
		<div align="left"> 
		<ul>
		
			

		</ul>
		</div>
	</div>
	</div>
	</form> '''
print '''</div>'''
#print footer.printFooter()
print '''</div>'''


def main():
	check_login()
main()

