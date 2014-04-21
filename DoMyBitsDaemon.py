#!/usr/bin/python

from datetime import datetime
import ConfigParser
import time
import subprocess

def main():
    config = ConfigParser.ConfigParser()
    config.read("config.cnf")
    wait_int = int(config.get('daemon','wakeup'))
    if config.getboolean('daemon','debug') == True:
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
    logfile.write(message + " - " + str(datetime.now()) + "\n")
    logfile.close()
    return

def checkevents(config):
    available_modules = config.get('modules', 'available_modules').split(',')
    if config.getboolean('daemon','debug') == True:
        debug("Checking Events")
        debug("attempting to launch modules: " + ''.join(available_modules))
    for module in available_modules:
        if config.getboolean(module, 'enabled') == True:
            if config.getboolean('daemon','debug') == True:
                debug("Launching " + module)
                child = subprocess.Popen(["python", config.get(module, 'script')])
                debug(module + " Spawned")
            else:
                child = subprocess.Popen(["python", config.get(module, 'sctipt')])
    return

main()
