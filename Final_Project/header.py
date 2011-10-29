#!c:/Python26/python.exe
import cgi
import utility

def printHeader():
	print '''<img src = "/others/header.jpg" alt ="OnePortal" width = "100%" height ="100">
<body bgcolor="D8FOF8">
'''
	if utility.isLoggedIn()!='1':
		print ''' <a href="join_us.py">Join Now</a>  '''
		print '''| <a href="front_page.py">Home</a></li> '''
	if(utility.isLoggedIn()=='1'):
		print '''<a href="home.py">Home</a>'''
		print '''| <a href="insert_roles.py">Insert Roles</a> | <a href="display_roles.py">Update Roles</a> | <a href="delete_roles.py">Delete Roles</a>'''
		print '''| <a href="logout.py">  LogOut</a> | <a href="load_data.py">Load Data</a>'''
		print '''<br></br>'''
	return ""	
	 