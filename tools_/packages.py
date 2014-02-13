#!/usr/bin/env python2

import urllib2
import subprocess
from sys import exit
from os import system

from tools_ import logger

#Stops people from running this program directly.
if __name__ == "__main__":
    print "This script should not be ran manually. It's apart of a package for the turbulence utility."
    exit()
    

def checkInternet():
    return False #Debug
    try:
        response=urllib2.urlopen('http://74.125.228.100',timeout=20)
        return True
    except urllib2.URLError as err: pass
    return False
    
    
def getCurrentPackages():
        packagesText = subprocess.check_output("pacman -Qq", shell=True)
        packagesList = packagesText.split("\n")
        return packagesList

def handlePackages(packagesTBI, packagesTBR): #packagesTBI = packages to be installed #packagesTBR = packages to br removed
    currentPackages = getCurrentPackages()
    packagesTBIList = list(set(packagesTBI) - set(currentPackages)) #Packages to be installed
    packagesTBIStr = ' '.join(packagesTBIList)
    logger.writeLog("packagesToBeInstalled", packagesTBIStr)
    packagesTBNList = list(set(currentPackages) - set(packagesTBR)) #Packages that don't need to be removed or installed (neutral).
    packagesTBRList = list(set(currentPackages) - set(packagesTBNList)) #Packages to be removed
    packagesTBRStr = ' '.join(packagesTBRList)
    logger.writeLog("packagesToBeRemoved", packagesTBRStr)
    
    installPackages = subprocess.Popen(["lxterminal", "-e", "bash",  "/usr/share/turbulence/scripts/install-packages.sh", "\"" + ' '.join(packagesTBIList) + "\"", "-r", "\"" + ' '.join(packagesTBRList) + "\""])
    installPackages.wait()
    system("wmctrl -a LXTerminal")
