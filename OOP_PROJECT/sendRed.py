#!/usr/bin/python
import os, re
import sys
import smtplib

#from email.mime.image import MIMEImage
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.MIMEText import MIMEText


SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587


sender = 'jrsraspberrypi@gmail.com'
password = "RaspPi3.14"
recipient = sys.argv[1]
subject = ''
message = sys.argv[3]
BODY_HTML = '<!DOCTYPE html><html><head><title>TEST</title></head><body><h1><b>Water Level Has Risen!</b></h1><br/></body></html>'

def main():
    print("I am running the py script!")
    msg = MIMEMultipart()
    msg['Subject'] = sys.argv[2]
    msg['To'] = recipient
    msg['From'] = sender

    part = MIMEText('text', "plain")
    part.set_payload(message)
    msg.attach(part)
    msg.attach(MIMEText(BODY_HTML, 'html'))

    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

    session.ehlo()
    session.starttls()
    session.ehlo

    session.login(sender, password)

    # Now send or store the message
    qwertyuiop = msg.as_string()



    session.sendmail(sender, recipient, qwertyuiop)

    session.quit()
    #os.system('notify-send "Email sent"')

if __name__ == '__main__':
    main()
