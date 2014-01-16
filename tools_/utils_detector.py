#!/usr/bin/env python2

import subprocess
import signal
import os

from sys import exit
from tools_ import logger

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
    if detectProcess('tint2'):
        return True
    else:
        return False

#Detect if plasma is present
def detectPlasma():
    if detectProcess('plasma-desktop'):
        return True
    else:
        return False

#Detect is KWin is present
def detectKwin():
    if detectProcess('kwin'):
        return True
    else:
        return False

#This is a tricky one, since nitrogen doesn't have
#A process to detect it by. I'm going to be looking
#For a better way to detect the presence of nitrogen.
def detectNitrogen():
    if detectPlasma():
        return False
    else:
        if os.path.isfile('/usr/bin/nitrogen'):
            print "Assuming that you are running nitrogen..."
            return True
        else:
            return False

            
            