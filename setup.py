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
DAEMON_WAKEUP_INT = int(raw_input('How Often In Mins Should I Wakeup? ')) * 60

# set a number of parameters
config.add_section("smtp")
config.set("smtp", "server", SMTP_SERVER)
config.set("smtp", "port", SMTP_PORT)
config.set("smtp", "user", SMTP_USER)
config.set("smtp", "pass", base64.b64encode(SMTP_PASSWORD))
config.add_section("daemon")
config.set("daemon", "wakeup", DAEMON_WAKEUP_INT)
config.set("daemon", "debug", "no")
config.add_section("modules")
config.set("modules", "available_modules", "email_checker")
config.add_section("email_checker")
config.set("email_checker", "enabled", "yes")
config.set("email_checker", "script", "emailchecker.py")
# write to file
config_file = open('config.cnf', 'w')
config.write(config_file)
config_file.close

