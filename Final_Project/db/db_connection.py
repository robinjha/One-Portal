def database_connection():
	import MySQLdb
	db = MySQLdb.connect("127.0.0.1","root","brandeis","OnePortal" )
	#db = MySQLdb.connect("127.0.0.1","root","brandeis","dvd_rental" )
	return db