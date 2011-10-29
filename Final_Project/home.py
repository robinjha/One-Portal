#!c:/Python26/python.exe
import cgi
import header
import utility 
import header
import datetime
import getdata
import runner
import insert_email
#import cgitb
#cgitb.enable()

from db import database_connection
customer_id = utility.getUserId(utility.getUserName())
#print 'id:%s'%customer_id


db = database_connection()
cursor = db.cursor()
sql_root = "select role_id,role_name from roles where role_id in (select role_id from mapping where user_id = %s)"%customer_id
#print sql_root
cursor.execute(sql_root)
results_root=cursor.fetchall()

def run():
		http_headers()
 
		customer_id = utility.getUserId(utility.getUserName())
		
		#print 'id:%s'%customer_id
		print '''
			<html>'''
		print header.printHeader()	
		todo = datetime.date.today()
		
		print '''<head>
			<script type="text/javascript" src="/others/simpletreemenu.js"></script>
			<link rel="stylesheet" type="text/css" href="/others/jquery-ui-1.8.6.custom.css" /></link>
			<script type="text/javascript" src="/others/jquery-1.4.2.min.js"></script>
			<script type="text/javascript" src="/others/jquery-ui-1.8.6.custom.min.js"></script>
			<link rel="stylesheet" type="text/css" href="/others/simpletree.css" /></link>
			<link rel="stylesheet" type="text/css" href="/others/styles.css" /></link>
 
			</head>
			
			<title>SwiftMail</title>
			<body>
			
			
			<table align='center' width='800' height='500' border='1' class='pagecontent'> 
			 
			<tr><td colspan="2">
			<div style="height: 135px;width: 1000px;;overflow:auto;">
			<table  class='pagecontent' border='0' width='800' align='center'>
			<tr width = "100%"><td colspan='2' width = "100%">'''
		print '''<h3 class="ui-widget-header">This is the to-do list for '%s'</h3>'''%todo
		 
		print '''</td></tr>'''
		print '''<tr><td><b>From</b></td> 
			 <td><b>Subject</b></td></tr>''' 
		sql_todo = "select message_id,message,date_email,from_email,datasource,subject,attachment from email where user_id = %s and date_email >= current_date()"%customer_id
		 
		cursor.execute(sql_todo)
		results_todo=cursor.fetchall()
		for row in results_todo:
			message_id = row[0]	
			message = row[1]
			date_email = row[2]
			from_email = row[3]
			datasource = row[4]
			subject =row[5]
			attachment = row[6]
			print '<tr><td>%s</td> '%from_email
			print '<td><a href=home.py?message_id=%s>%s</a></td></tr>'%(message_id,subject)
			
		print '''</table>
			
			
			
			</div></td>
			</tr>'''
		print '''<tr valign="top">
			<td rowspan='2'>
	 
				<script>
				$(function() {
					$( "#resizable2" ).resizable();
				});
				</script>
				
				<div id="resizable2" class="ui-widget-content">
			
			<a href="javascript:ddtreemenu.flatten('treemenu1', 'expand')">Expand All</a> | <a href="javascript:ddtreemenu.flatten('treemenu1', 'contact')">Contract All</a>	
				<div style="height:500px;width:206px;" style='table-layout:fixed'>
				<ul id="treemenu1" class="treeview">'''
		for row_root in results_root:
			print '<li>'
			role_id = row_root[0]
			role_id1 = row_root[0]
			role_name= row_root[1]
			print '<a href="home.py?role_id=%d">%s</a>'%(role_id,role_name)
			print '<ul>'
			
			sql_subroot = "select message_id,subject,from_email,date_email,datasource,attachment,role_id from email where user_id =%s and role_id = %s"%(customer_id,role_id)
			cursor.execute(sql_subroot)
			results_subroot=cursor.fetchall()
			if results_subroot:
				
				for row in results_subroot:
					message_id = row[0]
					message_id1 = row[0]
					subject = row[1]
					print '<li>'
					print '<a href="home.py?message_id=%d&role_id=%s">%s</a>'%(message_id,role_id,subject)
					print '</li>'
			else:
				message_id1 = 0
	
			print '</ul>'
			print '<li>'
		
		print '''</ul></div>
				<script type="text/javascript">
				 
				ddtreemenu.createTree("treemenu1", false)
				</script>
				'''
		print '''
 				<script>
				$(function() {
					$( "#resizable" ).resizable();
				});
				</script>'''
		
		print '''</div>
			</td>

			<td>
			
				<div id="resizable" class="ui-widget-content"; style="overflow:auto;">
				<h3 class="ui-widget-header">Inbox</h3>
				<table align="left" border='1' style='table-layout:fixed' class='pagecontent' width='100%'>
				<tr><td><b>From</b></td><td><b>Subject</b></td><td><b>Date</b></td><td><b>DataSource</b></td><td><b>Attachment</b></td></tr>
				'''
		form = cgi.FieldStorage()
		 
		
		try:	
			role_id=form["role_id"].value	
			
		except:
			#print "Select a appropriate folder"
			role_id = role_id1
		#print "role_id:%s"%role_id	
		sql_subroot = "select message_id,subject,from_email,date_email,datasource,attachment,role_id from email where user_id ='%s' and role_id = '%s'"%(customer_id,role_id)
		#print sql_subroot
		cursor.execute(sql_subroot)
		results_subroot=cursor.fetchall()		
		for row in results_subroot:
				message_id = row[0]
				
				subject = row[1]
				from_email = row[2]
				date_email = row[3]
				datasource = row[4]
				attachment = row[5]
				role_id = row[6]
				print '<tr><td>%s</td>'%from_email
				print ' <td>'
				print '<a href="home.py?message_id=%d&role_id=%s">%s</a>'%(message_id,role_id,subject)
				print '</td>'	
				print '<td>%s</td>'%date_email
				print '<td>%s</td>'%datasource
				print '<td>%s</td></tr>'%attachment
				print '<form><input type="hidden" name="role_id" value="%s"></form>'%role_id	
		 
		print'''</table>
				 </div>
			 
			</td>
			
			</tr>
			 <tr>
                <td valign='top'>
 				<script>
				$(function() {
					$( "#resizable1" ).resizable();
				});
				</script>
				
				<div id="resizable1" class="ui-widget-content">
				<h3 class="ui-widget-header">Full Email</h3>'''
		print '''<table border='0'  style='table-layout:fixed' class='pagecontent' width='100%'>'''
		form = cgi.FieldStorage()
		try:	
			message_id=form["message_id"].value	
		except:
			message_id = message_id1		
		sql_message = 'select message,from_email,subject from email where message_id = %s'%(message_id)	
		cursor.execute(sql_message)
		results_message=cursor.fetchall()	
		for row in results_message:
				print '''<tr><td>'''
				from_email = row[1]
 				print 'From : %s'%from_email	
				print '''</td></tr>'''	
				print '''<tr><td>'''
				subject = row[2]
 				print 'Subject : %s'%subject	
				print '''</td></tr>'''	
				print '''<tr><td>'''
				 
 				print '&nbsp;'
				print '''</td></tr>'''	
				print '''<tr><td>'''
				message = row[0]
 				print '%s'%message	
				print '''</td></tr>'''	
				
		print '''</table></div>
				</td>
              </tr>
			</table>
			</body>
			</html>'''
 
 
def http_headers():
	print "Content-type: text/html; charset=iso-8859-1\n\n"
   
run()



