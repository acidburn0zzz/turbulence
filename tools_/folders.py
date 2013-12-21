#!/usr/bin/env python2 

import os
from sys import exit

from tools_ import logger

if __name__ == "__main__":
    print "This script should not be ran manually. It's apart of a package for the turbulence utility."
    exit()
    

#sets needed variables and lists
homeDir = os.path.expanduser("~")
#homeDir = "/home/dcell/testhome" #developers uncomment this line 
homeDirCont = os.listdir(homeDir)
homeFolders = []
keyDirectories = ['Downloads', 'Desktop', 'Documents', 'Music', 'Pictures', 'Public', 'Templates', 'Videos']

#remove all hidden directories, hidden files, and normal files
def findKeyDir(needOrActive):
    x = 0
    while x != len(homeDirCont):
        if homeDirCont != []:
            if homeDirCont[x].startswith('.') or os.path.isfile(os.path.join(homeDir, homeDirCont[x])):
                homeDirCont.remove(homeDirCont[x])
                #x = x - 1
            else:
                x = x + 1
        else:
	     x = len(homeDirCont)
    
    #finds the directories being used, and the directories needed
    keyDirectoriesActive = set(homeDirCont).difference(set(homeDirCont).difference(keyDirectories))
    keyDirectoriesNeeded = set(keyDirectories).difference(keyDirectoriesActive)
    
    #returns type of output that was specified
    if needOrActive == "active":
        return keyDirectoriesActive
    elif needOrActive == "need":
        return keyDirectoriesNeeded
    return True
      
#gets object name from set in bool value or name
def getObject(setname, objectname, nameorbool):
    x = 0
    for x in setname:
        if objectname == x:
            if nameorbool == "bool":
                return True
            elif nameorbool == "name":
                return x
    return True
  
#creates directory
def createDir(directory):
    fullPath = homeDir + "/" + directory
    if not os.path.exists(fullPath):
        os.makedirs(fullPath)
        logger.writeLog('createdDir', fullPath)
    else:
        logger.writeLog('dirAlreadyExists', fullPath)
        return False
    return True
  
#removes directory
def deleteDir(directory):
    fullPath = homeDir + "/" + directory
    if os.path.exists(fullPath):
        if os.listdir(fullPath) == []:
            os.rmdir(fullPath)
            logger.writeLog('removedDir', fullPath)
        else:
	    logger.writeLog('dirNotEmpty', fullPath)
    else:
        logger.writeLog('dirNotExists', fullPath)
        return False
    return True
    
    
    
    
    