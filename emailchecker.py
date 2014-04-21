#!/usr/bin/python

import ConfigParser
import base64
import subprocess
from datetime import datetime

def main():
    config = ConfigParser.ConfigParser()
    config.read("config.cnf")
    smtp_server = config.get('smtp','server')
    smtp_port = config.get('smtp','port')
    username = config.get('smtp','user')
    password = base64.b64decode(config.get('smtp','pass'))
    recipient = username
    subject = "test subject"
    body = "test body"
    if config.getboolean('daemon','debug') == True:
        debug("emailchecker launched")
        child = subprocess.Popen(["python", "sendemail.py", smtp_server, smtp_port, username, password, recipient, subject, body])
        debug("email sent to " + username)
    else:
        child = subprocess.Popen(["python", "sendemail.py", smtp_server, smtp_port, username, password, recipient, subject, body])

def debug(message):
    logfile = open('logfile.log', 'a')
    logfile.write(message + " - " + str(datetime.now()) + "\n")
    logfile.close()
    return

main()
