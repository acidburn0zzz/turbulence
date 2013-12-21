#!/usr/bin/env python2

import os
import subprocess
from sys import exit
from time import sleep

from tools_ import logger

#Stops users from running this manually
if __name__ == "__main__":
    print "This script should not be ran manually. It's apart of a package for the turbulence utility."
    exit()
  

#Kills the no good freaking plasma ;)
def killPlasma():
    try:
        KQuitPlasma = subprocess.Popen(["kquitapp", "plasma-desktop"], stdout=subprocess.PIPE)
        out, err = KQuitPlasma.communicate()
        logger.writeLog('killedPlasma')
    except OSError, e:
        print 'WARNING: failed os.kill: %s' % e
        print "Trying SIGKILL"
        plasmaPid = subprocess.Popen(["pidof", "-s", "plasma-desktop"], stdout=subprocess.PIPE)
        out, err = plasmaPid.communicate()
        pidOfPlasma = int(out)
        logger.writeLog('failedKillingPlasma')
        os.kill(pidOfPlasma, 9)
        logger.writeLog('killedPlasmaSIGKILL')
        
#Revives plasma from the dead!
def startPlasma():
    subprocess.Popen(["plasma-desktop"], stdout=subprocess.PIPE)
    logger.writeLog('startPlasma')
    
#Kills kwin
def killKwin():
    kwinPid = subprocess.Popen(["pidof", "-s", "kwin"], stdout=subprocess.PIPE)
    out, err = kwinPid.communicate()
    pidOfKwin = int(out)

    try:
        os.kill(pidOfKwin, 15)
        logger.writeLog('killedKwin')
    except OSError, e:
        print 'WARNING: failed os.kill: %s' % e
        print "Trying SIGKILL"
        logger.writeLog('failedKillingKwin')
        os.kill(pidOfKwin, 9)
        logger.writeLog('killedPlasmaSIGKILL')
        
#Revives kwin from the dead
def startKwin():
    subprocess.Popen(["dbus-send", "--dest=org.kde.kwin", "/KWin", "org.kde.KWin.reloadConfig"], stdout=subprocess.PIPE)
    logger.writeLog('startKwin')