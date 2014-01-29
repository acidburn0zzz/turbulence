#!/usr/bin/env python2

import subprocess
import signal

from sys import exit
from tools_ import logger
from os.path import isfile

if __name__ == "__main__":
    print "This script should not be ran manually. It's apart of a package for the turbulence utility."
    exit()

#Detect the existence of a running process
def detectProcess(processName):
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()

    for line in out.splitlines():
        if processName in line:
            active = True
            break
        else:
            active = False
            
    if active:
        return True
    else:
        return False

#Detect if tint is present
def detectTint():
    tint = detectProcess('tint2')
    return tint

#Detect if plasma is present
def detectPlasma():
    plasma =  detectProcess('plasma-desktop')
    return plasma

#Detect is KWin is present
def detectKwin():
    kwin = detectProcess('kwin')
    return kwin
  
def detectOpenBox():
    openbox = detectProcess('openbox')
    return openbox

#This is a tricky one, since nitrogen doesn't have
#A process to detect it by. I'm going to be looking
#For a better way to detect the presence of nitrogen.
def detectNitrogen():
    if detectPlasma():
        return False
    else:
        if isfile('/usr/bin/nitrogen'):
            return True
        else:
            return False
            
            