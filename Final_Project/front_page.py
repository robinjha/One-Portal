#!c:/Python26/python.exe
import cgi
import cgitb

import sys
import random
import time
import datetime
 
import utility
print "Content-type: text/html; charset=iso-8859-1\n\n"
cgitb.enable()
form = cgi.FieldStorage()

print ''' <html>
		<img src = "/others/header.jpg" alt ="OnePortal" width = "100%" height ="100">
		<body bgcolor="D8FOF8">
		<h1 align = "center"> Welcome to OnePortal </h1>
		<table border = 0 align = "center">
		<tr>
		<td><li><a href="login.py">Login</a></li></td>
		</tr>
		<tr>
		<td><li><a href="join_us.py">Join Us</a></li></td>
		</tr>
		</table>
		</html>'''
