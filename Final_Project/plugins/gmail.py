import imaplib
from email.parser import HeaderParser
import email
import xml.dom.minidom
from xml.dom.minidom import Document
import os
import datetime

def connect(uname,passwd):
    try:
        global conn
        conn = imaplib.IMAP4_SSL('imap.gmail.com',993)
        #username=raw_input('Enter gmail username')
        
        conn.login(uname, passwd)
        conn.select()
        s=conn.search(None, 'UNSEEN') 
        d=s[1][0]
        global ids
        ids=d.split()
        return uname

    except:
        print 'Cant Log you into gmail service'
        return 0
    
def getAttachments(username,ids):

    files=[]

    

    

    resp,data=conn.fetch(ids,"RFC822")
    mail=email.message_from_string(data[0][1])
    


    if mail.get_content_maintype() != 'multipart':
        return []
    
    for p in mail.walk():

        if p.get_content_maintype()=='multipart':
            continue

        if p.get('Content-Disposition') is None:
            continue

        file_name=p.get_filename()

        

        path=os.curdir+"\\users\\"+local+"\\attachments\\" + file_name

        files.append(path)

        if not os.path.isfile(path):
            f=open(path,'wb')
            f.write(p.get_payload(decode=True))
            f.close()
    return files    

def writeXML(uname,passwd,local):

    username=connect(uname,passwd)

    if username==0:
        return

    if os.path.exists(os.curdir+"\\users\\"+local)==False:
            os.mkdir(os.curdir+"\\users\\"+local)
            os.mkdir(os.curdir+"\\users\\"+local+"\\xml")
            os.mkdir(os.curdir+"\\users\\"+local+"\\attachments")

    
    for i in ids:

        files=getAttachments(username,i)

        data = conn.fetch(int(i), '(BODY[HEADER])')
        data1 = conn.fetch(int(i), '(BODY[1])')

        header_data = data[1][0][1]
        message=data1[1][0][1]

        parser = HeaderParser()
        msg = parser.parsestr(header_data)
        msg1=email.message_from_string(message)

        text=" "

    
        
        for part in msg1.walk():
            
                text+=str(part.get_payload())


     


        doc = xml.dom.minidom.Document()

        datasource=doc.createElement('datasource')

        datasource.appendChild(doc.createTextNode('gmail'))

        
        doc.appendChild(datasource)


        body=doc.createElement('from')

        body.appendChild(doc.createTextNode(str(msg['from'])))

        datasource.appendChild(body)


        body=doc.createElement('date')

        month={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
        components=str(msg['date']).split()
        date=str(datetime.datetime(int(components[3]),month[components[2]],int(components[1]),int(components[4].split(':')[0]),int(components[4].split(':')[1]),int(components[4].split(':')[2])))


        body.appendChild(doc.createTextNode(date))

        datasource.appendChild(body)


        body=doc.createElement('subject')

        body.appendChild(doc.createTextNode(str(msg['subject'])))

        datasource.appendChild(body)

        body=doc.createElement('message')

        body.appendChild(doc.createTextNode(text))

        datasource.appendChild(body)


        body=doc.createElement('attachment')

        if len(files)!=0:
            body.appendChild(doc.createTextNode('\n'.join(files)))
        else:
            body.appendChild(doc.createTextNode("NULL"))

        datasource.appendChild(body)


        doc.toprettyxml(indent=" ")


        
        num=len(os.listdir(os.curdir+"\\users\\"+local+"\\xml"))
          
        f=open(os.curdir+"\\users\\"+local+"\\xml\\"+'%s.xml'%(num+1),'w')
        doc.writexml(f)
        f.close()

    conn.logout()

def activate(uname,passwd,local):
    writeXML(uname,passwd,local)
    #logout()

