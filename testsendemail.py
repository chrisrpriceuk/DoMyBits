#!/usr/bin/python

import subprocess

smtp_server = raw_input('SMTP Server: ')
smtp_port = raw_input('SMTP Port: ')
username = raw_input('Username: ')
password = raw_input('Password: ')
recipient = raw_input('Recipient: ')
subject = raw_input('Subject: ')
body = raw_input('Body: ')

child = subprocess.Popen(["python", "sendemail.py", smtp_server, smtp_port, username, password, recipient, subject, body])
