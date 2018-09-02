# import needed packages
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# create a method to send the email
def send_email(email_address):
    my_email = os.getenv("EMAIL_ADDRESS")
    my_password = os.getenv("EMAIL_PASSWORD")

    # creates a message object instance
    msg = MIMEMultipart()

    message = """
            Hello,
            THis is a notification to remind you to post an entry.
            Follow this link below to sign in and add an entry to your diary
            http://www.google.com
            """

    # includes the object parameters
    msg['From'] = my_email
    msg['To'] = email_address
    msg['Subject'] = 'Daily Entry Notification'

    # encode character set     
    msg.set_charset('utf-8')

    # adds a message body 
    msg.attach(MIMEText(message, 'plain', 'utf-8'))

    # creates email server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    # starts the server
    server.starttls()

    # enters email credentials
    server.login(msg['From'], my_password)

    # send the message via the server.  
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    # quits the server
    server.quit()

    print('Email sent')
