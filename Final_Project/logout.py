#!c:/Python26/python.exe
import cgi

import utility
print "Content-type: text/html; charset=iso-8859-1\n\n"


print '''<HTML>'''
print '''<TITLE>Logout</TITLE><body>'''

print '''<script language=javascript>
		 var new_date = new Date()
    new_date = new_date.toGMTString()
    var thecookie = document.cookie.split(";")
    for (var i = 0;i < thecookie.length;i++) 
    {
        document.cookie = thecookie[i] + "; expires ="+ new_date
    }
    window.location="http://localhost/video/Final_Project/front_page.py";
    </script>
    '''


print '''
		<div class="left-side" style="width:745px;" >
	  '''
print '''You are logged out ... Now redirecting to Login page .... '''


print '''</div>'''

print '''</div>'''


