#!c:/Python26/python.exe
import cgi
def printLeftNav():
	db = database_connection()
	cursor = db.cursor()
	
	print '''
		<div class="clearfix"></div>
		<div class="underliner"></div>
		<div  class="left-side"  style="float:left;width:200px">
					<div class="title-menu">Browse By Genres</div>
						<ul id="MenuBar2" class="MenuBarVertical">'''
	
	sql = "select Category_Name from category"
	cursor.execute(sql)
	categories = cursor.fetchall()
	for category in categories:
		print '''<li><a href="home.py?genere='''
		print category[0]
		print '''">'''
		print category[0]
		print '''</a></li>'''
	
						
	print '''</ul>
		<div style="height:2px;">&nbsp;</div>
		<div class="title-menu">Hot lists</div>
		 <ul id="MenuBar2" class="MenuBarVertical">
								
								<li ><a   href='home.py?action=popular' >Most Popular Movie</a></li>
								<li ><a   href='home.py?action=new'>New In Store</a></li>
								<li ><a href='home.py?action=recent'>Recent Movie</a></li>
								

							</ul>
					<div style="height:2px;">&nbsp;</div>
						
		</div>'''
		
	return ""
	
def database_connection():
	import MySQLdb
	db = MySQLdb.connect("127.0.0.1","root","brandeis","dvd_rental" )
	return db
