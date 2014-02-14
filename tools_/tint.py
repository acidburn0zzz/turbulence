#!/usr/bin/env python2

import os
from sys import exit

from tools_ import logger
from tools_ import utils_detector

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
       if utils_detector.detectTint():
           print "I couldn't find the themefile: " + homeDir + configFile

#Changes the tint2 position
def panelPosition(position):
    positionValues = {
        "top": ["panel_position = top center horizontal", "task_text = 1"],
        "bottom": ["panel_position = bottom center horizontal", "task_text = 1"],
        "right": ["panel_position = center right vertical", "task_text = 0"],
        "left": ["panel_position = center left vertical", "task_text = 0"],
    }
    
    for screenPosition, positionSettings in positionValues.items():
        if position == screenPosition:
            query = "panel_position"
            with open(tintTwo, 'rw') as search:
                for panel_position in search:
                    panel_position = panel_position.rstrip()
                    if panel_position.startswith(query):
                        search.close()
                        break
		      
            query = "task_text"
            with open(tintTwo, 'rw') as search:
                for task_text in search:
                    task_text = task_text.rstrip()
                    if task_text.startswith(query):
                        search.close()
                        break
                
            tintTwoRead = open(tintTwo).read()
            tintTwoRead = tintTwoRead.replace(panel_position, positionSettings[0])
            tintTwoRead = tintTwoRead.replace(task_text, positionSettings[1])
            tintTwoWrite = open(tintTwo, 'w')
            tintTwoWrite.write(tintTwoRead)
            tintTwoWrite.close()
        
            logger.writeLog('changedTintPanel', screenPosition)
            return True
        

