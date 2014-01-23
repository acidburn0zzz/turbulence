#!/usr/bin/env python2 

import os
from sys import exit
from subprocess import check_output

from tools_ import logger

if __name__ == "__main__":
    print "This script should not be ran manually. It's apart of a package for the turbulence utility."
    exit()
    

#sets needed variables and lists
homeDir = os.path.expanduser("~")
homeFolders = []
keyDirectories = ['DOWNLOAD', 'DESKTOP', 'DOCUMENTS', 'MUSIC', 'PICTURES', 'PUBLICSHARE', 'TEMPLATES', 'VIDEOS']


#remove all hidden directories, hidden files, and normal files
def findKeyDir(needOrActive):
    x = 0
    for folderName in keyDirectories:
        folderCheck = check_output(['xdg-user-dir', folderName]).replace("\n", "").replace("\r", "")
        if folderCheck != homeDir and folderCheck != homeDir + "/":
            homeFolders.append(folderName)
            
    keyDirectoriesActive = set(homeFolders)
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
    return False
  
#creates directory
def createDir(directory, directoryXDG):
    ###########
    #IMPORTANT#
    ###########
    
    ####################################################
    #Due to the nature of the thus graphical installer
    #Already creating all of the users home directories
    #Already localized, I've disabled this feature 
    #Temporarily due to some complications with xdg
    #It will be re-enabled when the proper code is found 
    #To perform these actions. Otherwise, the below code
    #Will not work as is.
    ####################################################
    #TODO enable this functionality again, and fix code.
    
    #if os.path.exists(xdgDummyConf):
        #try:
           #with open(fullPath) as xdgConfig:
              #homeDirsNames = [line.rstrip('\n') for line in xdgConfig if not line.startswith("#")]
              #homeDirDic = {}
              #for dirName in homeDirsNames:
                  #homeDirDic[dirName.split('=')[0]] = ''.join(dirName.split('=')[1:])
        #except IOError:
           #print "Couldn't parse the " + fullPath + " Configuration file."
           
    #for xdgVar, homeDirValue in homeDirDic.items():
        #if xdgVar == directory:
            #if homeDirValue != "\"$HOME/\"":
                #print "Assume created..."
            #else:
                #print "Assume creation..."           
                
    
    fullPath = homeDir + "/" + directory
    if not os.path.exists(fullPath):
        os.makedirs(fullPath)
        os.system('xdg-user-dirs-update --set ' + directoryXDG.partition('XDG_')[-1].rpartition('_DIR')[0] + ' $HOME/' + directory)
        logger.writeLog('createdDir', fullPath)
    else:
        os.system('xdg-user-dirs-update --set ' + directoryXDG.partition('XDG_')[-1].rpartition('_DIR')[0] + ' $HOME/' + directory)
        logger.writeLog('dirAlreadyExists', fullPath)
        return False
    return True
        
  
#removes directory
def deleteDir(directory):
    fullPathXdg = homeDir + "/.config/user-dirs.dirs"
    if os.path.exists(fullPathXdg):
        try:
           with open(fullPathXdg) as xdgConfig:
              homeDirsNames = [line.rstrip('\n') for line in xdgConfig if not line.startswith("#")]
              homeDirDic = {}
              for dirName in homeDirsNames:
                  homeDirDic[dirName.split('=')[0]] = ''.join(dirName.split('=')[1:])
        except IOError:
           print "Couldn't parse the " + fullPathXdg + " Configuration file."
           logger.writeLog('couldntParseXDG', fullPathXDG)
           
    for xdgVar, homeDirValue in homeDirDic.items():
        if xdgVar == directory:
            if homeDirValue != "\"$HOME/\"":
                fullPath = ''.join(homeDirValue.replace("$HOME", homeDir).split("\"")[1:])
                if os.path.exists(fullPath):
                    os.rmdir(fullPath)
                else:
                    logger.writeLog('dirNotExists', fullPath)
                os.system('xdg-user-dirs-update --set ' + directory.partition('XDG_')[-1].rpartition('_DIR')[0] + ' $HOME/')
            else:
                fullPath = homeDirValue.replace("$HOME", homeDir)
                if not os.path.exists(fullPath):
                    os.rmdir(fullPath)
                else:
                    logger.writeLog('dirNotExists', fullPath)
    logger.writeLog("removedDir", fullPath)                
    
            
    
    
    
    
    