#!/usr/bin/python

import subprocess

username = raw_input('Username: ')
password = raw_input('Password: ')
recipient = raw_input('Recipient: ')
subject = raw_input('Subject: ')
body = raw_input('Body: ')

child = subprocess.Popen(["python", "sendemail.py", username, password, recipient, subject, body])
