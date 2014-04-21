#!/usr/bin/python

import ConfigParser
import sys
import base64

config = ConfigParser.ConfigParser()
# Get the users setup details

SMTP_SERVER = raw_input('Enter your SMTP server: ')
SMTP_PORT = raw_input('Enter your SMTP port: ')
SMTP_USER = raw_input('Enter your SMTP username: ')
SMTP_PASSWORD = raw_input('Enter your SMTP password: ')
DAEMON_WAKEUP_INT = int(raw_input('How often in mins should I wakeup? ')) * 60
MYSQL_HOST = raw_input('Enter your MYSQL hostname: ')
MYSQL_ROOTU = raw_input('Enter the MYSQL root user: ')
MYSQL_ROOTP = raw_input('Enter the MYSQL password for ' + MYSQL_ROOTU + ': ')
MYSQL_DATABASE_NAME = raw_input('Enter a name for the MYSQL database we will create: ')
MYSQL_TABLE_NAME = raw_input('Enter a name for the MYSQL table we will create: ')
MYSQL_USER = raw_input('Enter the MYSQL user to be created: ')
MYSQL_PASS = raw_input('Enter the MYSQL password for ' + MYSQL_USER + ': ')

# set a number of parameters
config.add_section("smtp")
config.set("smtp", "server", SMTP_SERVER)
config.set("smtp", "port", SMTP_PORT)
config.set("smtp", "user", SMTP_USER)
config.set("smtp", "pass", base64.b64encode(SMTP_PASSWORD))
config.add_section("daemon")
config.set("daemon", "wakeup", DAEMON_WAKEUP_INT)
config.set("daemon", "debug", "no")
config.add_section("mysql")
config.set("mysql", "host", MYSQL_HOST)
config.set("mysql", "db", MYSQL_DATABASE_NAME)
config.set("mysql", "table", MYSQL_TABLE_NAME)
config.set("mysql", "user", MYSQL_USER)
config.set("mysql", "pass", base64.b64encode(MYSQL_PASS))
config.add_section("modules")
config.set("modules", "available_modules", "email_checker")
config.add_section("email_checker")
config.set("email_checker", "enabled", "yes")
config.set("email_checker", "script", "emailchecker.py")
# write to file
config_file = open('config.cnf', 'w')
config.write(config_file)
config_file.close

