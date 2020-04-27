import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("""
     _   _ _ _       _       _   _ _      _
    | | | (_) |_ ___| |__   | | | (_) ___| | _____ _ __
    | |_| | | __/ __| '_ \  | |_| | |/ __| |/ / _ \ '__|
    |  _  | | || (__| | | | |  _  | | (__|   <  __/ |
    |_| |_|_|\__\___|_| |_| |_| |_|_|\___|_|\_\___|_|   """)

print("""
  ===================Emails Sender Python tool===================""")

print("""   Author : Parth Panchal""")

print("""  =============================================================""")


from_add = 'Paste Your email address here...'            #paste your email address here
mails = open('emails.txt','r')

print("\n\tPlease Wait...")
j = 1
for i in mails:
    to_add = str(i)

    msg = MIMEMultipart()
    msg['from'] = from_add
    msg['to'] = to_add
    msg['subject'] = 'testing'

    body = "hello this is for test..."

    msg.attach(MIMEText(body,'plain'))

    email = str("paste your email address here")                   #paste your email address here
    password = str("paste your email address password here")        #paste your email's password here

    try :
        #remove below line if you are using yahoo mail
        server = smtplib.SMTP("smtp.gmail.com", 587)

        #remove below line if you are using gmail
        server = smtplib.SMTP("smtp.mail.yahoo.com",587)

        server.ehlo()
        server.starttls()
        server.login(email,password)
        text = msg.as_string()
        server.sendmail(from_add, to_add, text)
        server.quit()
        print("\n\tEmail ",j," sent...")
        j = j+1
    except :
        print('\n\tEmail ',j,' is not send...')
        j = j+1

print("\n\tAll the mails sent successfully...")
