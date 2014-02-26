#!/usr/bin/env python

import os
import subprocess
from sys import exit

from tools_ import logger

#Stops users from running this manually
if __name__ == "__main__":
    print("This script should not be ran manually. It's apart of a package for the turbulence utility.")
    exit()
    
def killTintTwoPlus():
    tintTwoKill = subprocess.Popen(["killall", "tint2"], stdout=subprocess.PIPE)
    tintTwoKill.wait()
    tintTwoStart =subprocess.Popen(["tint2", "&"], stdout=subprocess.PIPE)
    conkyKill = subprocess.Popen(["killall", "conky"], stdout=subprocess.PIPE)
    conkyKill.wait()
    conkyStart = subprocess.Popen(["conky", "&"], stdout=subprocess.PIPE)