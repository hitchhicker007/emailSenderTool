import smtplib

gmail_user = ""   
gmail_pass = ""   

email_file = open('emails.txt','r')

emails = []
for i in email_file:
    emails.append(i.strip())

sent_from = gmail_user

subject = "Python webinar by ASME SOU"

body = "Hey there, my name is parth panchal. sending you this email using python programming on webinar session 4."


email_text = """
From: %s
To:%s
Subject: %s

%s
""" % (sent_from, emails,subject, body)

smtp_server = smtplib.SMTP_SSL('smtp.gmail.com',465)

smtp_server.ehlo()

smtp_server.login(gmail_user,gmail_pass)

for index,email in enumerate(emails):
    if index > 189:
        try:
            smtp_server.sendmail(sent_from, email, email_text)
            print("email ",index, " sent...")
        except Exception as e:
            print("error while sending email number ",index, " ",str(e))

print("----all emails are sent----")

smtp_server.close()
