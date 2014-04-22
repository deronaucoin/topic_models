import sqlite3
import csv
conn = sqlite3.connect('contacts.db')
from DAO import DAO
dao = DAO("DB")
sql = "select top 10000 Message, noteid from Note where whenposted > '4/20/2012' and NoteFKTypeID = 102 and NoteDetailTypeID = 24404 and NoteTypeID  = 24352 and Message like 'How is your placement going?%' /*and noteid = 2883737*/ order by NoteID desc"
messages = dao.read(sql)
questions = []
questions.append("How is your placement going?")  
questions.append("Does au pair receive weekly stipend?")
questions.append("Any concerns with the 10 hr/day and 45 hr/week schedule?")
questions.append("Any concerns with childcare and any non-childcare related duties?")
questions.append("Any concerns with time-off/vacation scheduling?")
questions.append("Is au pair scheduled or planning to take educational courses?")
       
innerQuestions = questions       
       
contacts = []
for messageRow in messages:
    contact = {}
    message = messageRow.Message    
    contact['noteid'] = messageRow.noteid        
    i = 1
    response = {}        
    for question in questions:
        quesStart = message.rfind(question)        
        if i < len(questions):
            quesEnd = message.rfind(questions[i])
        else:
            quesEnd = len(message)   
        questionString = message[quesStart:quesEnd]
        response[question] = questionString.replace(question,"").strip()
        response[question] = response[question].replace("\r\n"," ")  
        i += 1
        contact['responses'] = response
    contacts.append(contact)

c = csv.writer(open("contacts.csv", "wb"))
c.writerow(["noteid","comment"])
for contact in contacts:
    #print st
    c.writerow([contact['noteid'],contact['responses']["How is your placement going?"]])
    #print str(contact['noteid']) + " " + contact['responses']["How is your placement going?"]