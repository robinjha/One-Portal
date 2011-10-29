from xml.etree.ElementTree import ElementTree
from xml.dom.minidom import Document
import getpass
import gdata
import gdata.calendar.service
import gdata.service
import atom.service
import gdata.calendar
import atom
import getopt
import sys
import string
import time
import os

def activate(username,password,local):
   
    
    #username = raw_input("Enter your username: ")
    #password = getpass.getpass("Enter your password: ")

    calendar_service = gdata.calendar.service.CalendarService(username,password , "Python-Calendar_Example-1.0")
    try:
        calendar_service.ProgrammaticLogin()
    except gdata.service.BadAuthentication, e:
        print "Authentication error logging in: %s" % e
        #f.write("Authentication error logging in: %s" % e)
        return
    except Exception, e:
        print "Error Logging in: %s" % e
        #f.write("Error Logging in: %s" % e)
        return

    
   
    try:
        #Get the CalendarListFeed
        all_calendars_feed = calendar_service.GetOwnCalendarsFeed()
    except Exception, e:
        print "Error getting all calendar feed: %s" % (e)
        #f.write("Error getting all calendar feed: %s" % (e))
        return

    

    #Now loop through all of the CalendarListEntry items.
    for cal in list(all_calendars_feed.entry):
        a_link = cal.GetAlternateLink()
        
        if (a_link is not None):
            event_feed = calendar_service.GetCalendarEventFeed(a_link.href)
            
            feedentry = list(event_feed.entry)
            
            
            i=0
            j=0

            if os.path.exists(os.curdir+"\\users\\"+local)==False:
                os.mkdir(os.curdir+"\\users\\"+local)
                os.mkdir(os.curdir+"\\users\\"+local+"\\xml")
                os.mkdir(os.curdir+"\\users\\"+local+"\\attachments")


            
            for event in feedentry:
                doc = Document()
                datasource = doc.createElement("dataSource")
                doc.appendChild(datasource)

                datasource.appendChild(doc.createTextNode("googlecalendar"))
        
                

                
            
                authorinfo = doc.createElement("from")
                for person in event.who:
                    
                    authorinfo.appendChild(doc.createTextNode("\t\t\tName: %s\n\t\t\temail: %s" % (person.name, person.email)))
                    datasource.appendChild(authorinfo)
                    
                    date = doc.createElement("date")
                for e_time in list(event.when):
                    da_te = e_time.start_time.split('T')[0]
                    date.appendChild(doc.createTextNode("\t\t\t%s\n" % da_te))
                    rawtime = e_time.start_time.split('T')[1]
                    time=rawtime.split('.')[0]
                    date.appendChild(doc.createTextNode("\t\t\t%s\n" % time))
                    datasource.appendChild(date)

                subject = doc.createElement("subject")
                subject.appendChild(doc.createTextNode("\t%s\r\n" % (event.title.text)))
                datasource.appendChild(subject)

                message = doc.createElement("message")
                message.appendChild(doc.createTextNode("\t%s" % event.content.text))
                datasource.appendChild(message)

                attach = doc.createElement("attachment")
                attach.appendChild(doc.createTextNode("NULL"))
                datasource.appendChild(attach)

                
                num=len(os.listdir(os.curdir+"\\users\\"+local+"\\xml"))
                
                f=open(os.curdir+"\\users\\"+local+"\\xml\\"+'%s.xml'%(num+1),'w')
                doc.writexml(f)
                f.close()               
                i+=1    
                
        
    

