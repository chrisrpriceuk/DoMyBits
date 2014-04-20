#!/usr/bin/python

import ConfigParser
import sys
import base64

config = ConfigParser.ConfigParser()
# Get the users setup details

SMTP_SERVER = raw_input('Enter Your SMTP Server: ')
SMTP_PORT = raw_input('Enter Your SMTP Port: ')
SMTP_USER = raw_input('Enter Your SMTP Username: ')
SMTP_PASSWORD = raw_input('Enter Your SMTP Password: ')

# set a number of parameters
config.add_section("SMTP")
config.set("SMTP", "server", SMTP_SERVER)
config.set("SMTP", "port", SMTP_PORT)
config.set("SMTP", "user", SMTP_USER)
config.set("SMTP", "pass", base64.b64encode(SMTP_PASSWORD))

# write to file
config_file = open('config.cnf', 'w')
config.write(config_file)
config_file.close

