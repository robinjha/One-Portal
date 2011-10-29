#!c:/Python26/python.exe
import cgi
import re
import string
import utility 
import sys
import runner
import con_str
 
from db import database_connection
#print "Content-type: text/html; charset=iso-8859-1\n\n"
user_id = utility.getUserId(utility.getUserName())

db = database_connection()
cursor = db.cursor()


def insert_data():
	user_id = utility.getUserId(utility.getUserName())
	#print user_id
	#data = [('googlecalendar', '\t\t\tName: drrt2010@gmail.com\n\t\t\temail: drrt2010@gmail.com', '\t\t\t2010-12-05\n\t\t\t15:00:00\n', '\ttest attachment 1\n', '\tthis is a test1', "[u'NULL']", ['ritu', 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test']), ('googlecalendar', '\t\t\tName: drrt2010@gmail.com\n\t\t\temail: drrt2010@gmail.com', '\t\t\t2010-12-05\n\t\t\t15:00:00\n', '\ttest event 2\n', '\tthis is a test2', "[u'NULL']", ['deepali', 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test']), ('googlecalendar','\t\t\tName: drrt2010@gmail.com\n\t\t\temail: drrt2010@gmail.com', '\t\t\t2010-12-05\n\t\t\t15:00:00\n', '\ttest event\n', '\tthis is a test', "[u'NULL']", ['johann'])]
	wordList,local = con_str.con_str()
	data = runner.xmlReadandAnalyze(wordList,local)
	#print "Data:%s"%data
	#[('gmail', 'Deepali Agarwal <koolkhush@gmail.com>', '2010-12-05 17:45:09', 'urgent', ' Hi this is an urgent message.\n\n-- \nThanks and Regards!\nDeepali\n', "[u'NULL']", ['urgent'])]
	#data = [('Brandeis Now', ' Brandeis Now', ' 2010-12-03 17:06:00', ' Town hall on alcohol and drug policy', ' ', "[u'http://www.brandeis.edu/now/2010/december/townhall-dec6.html']", []), ('Brandeis Now', ' Brandeis Now', ' 2010-11-30 14:28:00', ' Schusterman Center unveils Israeli art collection', " At the entrance to the new home of the Schusterman Center for Israel Studies, on the top level of the Mandel Center for the Humanities, visitors encounter innovative video works by prominent Israeli artists. These works by Sigalit Landau, Yael Bartana, Doron Solomons and Guy Ben-Ner are on display here after having been screened at major museums, among them the Israel Museum in Jerusalem, the Museum of Modern Art in New York, Tate Modern in London, and the Massachusetts Museum of Contemporary Art. They are part of a new collection of contemporary Israeli photography, prints and video art unveiled Nov. 10 at the inauguration of the Schusterman Center's new space. Also on display in the center are several large and powerful photographs of the Israeli landscape, including a nostalgic vista of the Yarkon River by Yossi Breger and a nocturnal image of the ruins of a Palestinian home by Dor Guez.", "[u'http://www.brandeis.edu/now/2010/december/schustermanfeature.html']", []), ('Brandeis Now', ' Brandeis Now', ' 2010-11-29 21:07:00', ' Annual Messiah Sing', ' ', "[u'http://www.brandeis.edu/arts/concerts/concerts.html']", []), ('Brandeis Now', ' Brandeis Now', ' 2010-11-29 17:48:00', " 'Girldrive' author says her cross-country trip shaped her view of feminism", ' In 2007, journalist and cultural critic Nona Willis Aronowitz and photographer Emma Bee Bernstein, both then 22 years old, hit the road for a trip across the United States to discover how their generation of young women related to feminism and ideas about gender justice. Some who they met didn\'t know the word "feminist," but they were "living the legacy" of feminism, she says.', "[u'http://www.brandeis.edu/now/2010/november/girldrive.html']", []), ('Brandeis Now', ' Brandeis Now', ' 2010-11-29 17:33:00', ' Ambassador will speak on South Sudan referendum', ' The self-determination vote gives South Sudan the opportunity to vote for independence from the North. The vote was provided for in the Comprehensive Peace Agreement that ended the Sudanese civil war in 2005. Top officials on both sides have committed to holding the referendum on time and to respecting the outcome. But many in the South and the international community worry that the government in Khartoum, in North Sudan, will not go along if the South votes for independence. ', "[u'http://www.brandeis.edu/now/2010/november/sudanese.html']", []), ('Brandeis Now', ' Brandeis Now', ' 2010-11-29 16:28:00', ' Staff awards surprise recipients', ' ', "[u'http://www.brandeis.edu/now/2010/november/staffawards.html']", [])]
	keywords = []
	counter = 0
	for item in data:
		counter +=1
		#print "counter"
		#print counter
		source = item[0]
		email_from = item[1]
		email_date = item[2]
		subject = item[3]
		message = item[4]
		attachment = item[5] 
		keywords =item[6]
		temp = attachment.split("[")
		#print temp
		for temp1 in temp:
			temp2 = temp1.split("u")
			for temp3 in temp2:
				temp4 = temp3.split("]")
				att = temp4[0]
				
				#print temp4[0]
 
		if source == 'googlecalendar':
			parts = email_from.split("Name:")
			for value in parts:
				email_from1 = value.split("email:")
				for some in email_from1:
					email_from2= some.split("\t")
			email_final = email_from2[0]
		
		if source == 'gmail':
			email_final = email_from
			
		if source == 'Brandeis Now':
			email_final = "Brandeis Now"
			message = "Null"
			subject = "Null"
			att = "Null"
			email_date = '2010-12-06 11:29:00'
			
						
 
		keywords1 = list(set(keywords))
		count1 =0
		count2=0
		count3 =0
		for child in keywords1:
			temp = "%"
			child1 = temp+child+temp
			
			sql_role = "SELECT count(role_id) FROM oneportal.mydata where mydata like '%s' and user_id = '%s'" %(child1,user_id)
			
			#print sql_role
			cursor.execute(sql_role)
			results=cursor.fetchall()
			for row in results:
				count = row[0]
				
				if count > 1:
					count1 = 1
				if count == 1:
					count2 =1
					data = child1
					child2 = child1
		if ((count2!=1) and (count1==1)):
			sql_insert = 'insert into email (role_id,user_id,message,date_email,from_email,datasource,subject,attachment) values ("2","%s","%s","%s","%s","%s","%s","%s")' %(user_id,message ,email_date,email_final,source,subject,att)
			#print sql_insert
			cursor.execute(sql_insert)
			db.commit()
			
		if (count2==1):
			sql_fetch = "select role_id from oneportal.mydata where mydata like '%s' and user_id = '%s'" %(data,user_id)
			cursor.execute(sql_fetch)
			results1=cursor.fetchall()
			for row1 in results1:
				role_id = row1[0]
			sql_insert = 'insert into email (role_id,user_id,message,date_email,from_email,datasource,subject,attachment) values ("%s","%s","%s","%s","%s","%s","%s","%s")' %(role_id,user_id,message ,email_date,email_final,source,subject ,att )
			#print sql_insert
			cursor.execute(sql_insert)
			db.commit()
			
		if ((count2 ==0) and (count1 ==0)):
			sql_insert = 'insert into email (role_id,user_id,message,date_email,from_email,datasource,subject,attachment) values ("3","%s","%s","%s","%s","%s","%s","%s")'%(user_id,message,email_date,email_final,source,subject ,att )
			#print sql_insert
			cursor.execute(sql_insert)
			db.commit()

 