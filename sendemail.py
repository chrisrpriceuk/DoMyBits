#!/usr/bin/python

import sys
import smtplib

SMTP_SERVER = sys.argv[1]
SMTP_PORT = sys.argv[2]
SMTP_USERNAME = sys.argv[3]
SMTP_PASSWORD = sys.argv[4]
recipient = sys.argv[5]
email_subject = sys.argv[6]
body_of_email = sys.argv[7]


# The below code never changes, though obviously those variables need values.
session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
session.ehlo()
session.starttls()
session.login(SMTP_USERNAME, SMTP_PASSWORD)

headers = "\r\n".join(["from: " + SMTP_USERNAME,
                       "subject: " + email_subject,
                       "to: " + recipient,
                       "mime-version: 1.0",
                       "content-type: text/html"])

# body_of_email can be plaintext or html!                    
content = headers + "\r\n\r\n" + body_of_email
session.sendmail(SMTP_USERNAME, recipient, content)
