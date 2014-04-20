#!/usr/bin/python

import ConfigParser
import base64
import subprocess

config = ConfigParser.ConfigParser()
config.read("config.cnf")
smtp_server = config.get('smtp','server')
smtp_port = config.get('smtp','port')
username = config.get('smtp','user')
password = base64.b64decode(config.get('smtp','pass'))
recipient = raw_input('Recipient: ')
subject = raw_input('Subject: ')
body = raw_input('Body: ')

child = subprocess.Popen(["python", "sendemail.py", smtp_server, smtp_port, username, password, recipient, subject, body])
