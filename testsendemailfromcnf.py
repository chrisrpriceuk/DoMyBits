#!/usr/bin/python

import ConfigParser
import subprocess

config = ConfigParser.ConfigParser()
config.read("config.cnf")
smtp_server = config.get('SMTP','server')
smtp_port = config.get('SMTP','server')
username = config.get('SMTP','server')
password = config.get('SMTP','server')
recipient = raw_input('Recipient: ')
subject = raw_input('Subject: ')
body = raw_input('Body: ')

child = subprocess.Popen(["python", "sendemail.py", smtp_server, smtp_port, username, password, recipient, subject, body])
