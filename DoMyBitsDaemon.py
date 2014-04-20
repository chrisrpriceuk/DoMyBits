#!/usr/bin/python

from datetime import datetime
import ConfigParser
import time


def main():
    config = ConfigParser.ConfigParser()
    config.read("config.cnf")
    wait_int = int(config.get('DAEMON','wakeup'))
    if config.getboolean('DAEMON','debug') == True:
        debug("Daemon started in full debug mode")
    lastnow = datetime.now()
    while True:
        now = datetime.now()
        dif = (now-lastnow).total_seconds()
        if dif < wait_int:
            time.sleep(1)
        else:
            checkevents(config)
            lastnow = datetime.now()

def debug(message):
    logfile = open('logfile.log', 'a')
    message = message + " - " + str(datetime.now()) + "\n"
    logfile.write(message)
    logfile.close()
    return

def checkevents(config):
    if config.getboolean('DAEMON','debug') == True:
        debug("Checking Events")
    return

main()
