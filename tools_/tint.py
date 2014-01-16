#!/usr/bin/env python2

import os
from sys import exit

from tools_ import logger

#Stops people from running this program directly.
if __name__ == "__main__":
    print "This script should not be ran manually. It's apart of a package for the turbulence utility."
    exit()
    

#Needed variables
homeDir = os.path.expanduser("~")
neededFiles = {
    "tintTwo": "/.config/tint2/tint2rc", 
    "conkyrc": "/.conkyrc"
}

#Attempts to set file paths
for configFileName, configFile in neededFiles.items():
    try:
       with open(homeDir + configFile):
           if configFileName == "tintTwo":
               tintTwo = homeDir + configFile
           elif configFileName == "conkyrc":
               conkyRC = homeDir + configFile
    except IOError:
       print "I couldn't find the themefile: " + homeDir + configFile

#Changes the tint2 position
def panelPosition(position):
    positionValues = {
        "top": ["panel_position = top center horizontal"],
        "bottom": ["panel_position = bottom center horizontal"],
        "right": ["panel_position = center right vertical"],
        "left": ["panel_position = center left vertical"],
    }
    
    for screenPosition, positionSettings in positionValues.items():
        if position == screenPosition:
            query = "panel_position"
            with open(tintTwo, 'rw') as search:
                for line in search:
                    line = line.rstrip()
                    if line.startswith(query):
                        search.close()
                        break
            tintTwoRead = open(tintTwo).read()
            tintTwoRead = tintTwoRead.replace(line, positionSettings[0])
            tintTwoWrite = open(tintTwo, 'w')
            tintTwoWrite.write(tintTwoRead)
            tintTwoWrite.close()
        
            logger.writeLog('changedTintPanel', screenPosition)
            return True
        

