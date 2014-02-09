#!/usr/bin/env python2

from sys import exit
from subprocess import call
from webbrowser import open as open_

from tools_ import logger

#Stops people from running this program directly.
if __name__ == "__main__":
    print "This script should not be ran manually. It's apart of a package for the turbulence utility."
    exit()
    
    
def launchSystemSettings():
    logger.writeLog("launchSystemSettings")
    call(["systemsettings"])
    return True
    
def launchAppearance():
    logger.writeLog("launchCustomize")
    call(["lxappearance"])
    return True
    
def launchHelp():
    logger.writeLog("launchHelp")
    open_('http://manjaro.org')
    return True
    
