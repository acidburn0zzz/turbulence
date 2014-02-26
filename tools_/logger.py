#!/usr/bin/env python

import os
import time
from sys import exit

#Stops users from running this manually
if __name__ == "__main__":
    print("This script should not be ran manually. It's apart of a package for the turbulence utility.")
    exit()


#Sets needed variables
homeDir = os.path.expanduser("~")
fullPath = homeDir + "/.turbulence"
fullPathAndFile = fullPath + "/turbulence.log"

#Checks that the log exists
def logExists():
    if os.path.isdir(fullPath):
        if os.path.isfile(fullPathAndFile):
            try:
                with open(fullPathAndFile):
                    return True
            except IOError:
                return False
        else:
            return False
    else:
        return False

#Creates the log      
def makeLog():
    logOrNot = logExists()
    if not logOrNot:
        if not os.path.isdir(fullPath):
            os.makedirs(fullPath)
            createLog = open(fullPathAndFile, 'w')
            createLog.close()
            return True
        else:
            if not os.path.isfile(fullPathAndFile):
                createLog = open(fullPathAndFile, 'w')
                createLog.close()
                return True
            else:
                return False
    else:
        return False
      
#Writes events to the log
def writeLog(event, optionalArg=None):
    eventLogic = {
        "logHeader": ["Turbulence successfully launched at: " + time.strftime("%d/%m/%Y %H:%M:%S"), None],
        "rootWarning": ["\nWarning: This script should not be ran as root unless you wish to change the theming for your root account", None],
        "proceedToFolders": ["\nProceeded to folders", None],
        "folderChosen": ["\nThis folder was chosen to be used: ", optionalArg],
        "folderNotChosen": ["\nThis folder was chosen to not be used: ", optionalArg],
        "couldntParseXDG": ["\nCouldn't parse the XDG config file: ", optionalArg],
        "createdDir": ["\nCreated the directory: ", optionalArg],
        "dirAlreadyExists": ["\nCould not create this directory since it already existed: ", optionalArg],
        "removedDir": ["\nRemoved the directory: ", optionalArg],
        "dirNotEmpty": ["\nCould not remove this directory because it was not empty: ", optionalArg],
        "dirNotExists": ["\nCould not remove this directory because it did not exist: ", optionalArg],
        "proceedToThemes": ["\nProceeded to themes", None],
        "changeTheme": ["\nChanged theme to ", optionalArg],
        "killedPlasma": ["\nKilled Plasma", None],
        "failedKillingPlasma": ["\nFailed to kill Plasma. Trying SIGKILL", None],
        "killedPlasmaSIGKILL": ["\nKilled Plasma using SIGKILL", None],
        "startPlasma": ["\nStarted Plasma", None],
        "killedKwin": ["\nKilled Kwin", None],
        "failedKillingKwin": ["\nFailed Killing Kwin. Trying SIGKILL", None],
        "killedPlasmaSIGKILL": ["\nKilled Kwin using SIGKILL", None],
        "startKwin": ["\nSent DBUS command to reload Kwin configuration", None],
        "proceedToWallpapers": ["\nProceeded to Wallpapers", None],
        "changedWallpaper": ["\nChanged the wallpaper to ", optionalArg],
        "proceedToFinal": ["\nProceeded to Final", None],
        "launchSystemSettings": ["\nLaunched System Settings", None],
        "launchHelp": ["\nLaunched help", None],
        "exitTurbulence": ["\nExited Turbulence at: " + time.strftime("%d/%m/%Y %H:%M:%S") + "\n\n", None]
    }
    logOrNot = logExists()
    if not logOrNot:
        exit("Log has not been created yet")
        return False
        
    openedLog = open(fullPathAndFile, 'a')
    
    for eventName, eventSettings in eventLogic.items():
        if event == eventName:
           openedLog.write(eventSettings[0])
           if eventSettings[1] != None:
               openedLog.write(eventSettings[1])
    openedLog.close()
    return True
    
    