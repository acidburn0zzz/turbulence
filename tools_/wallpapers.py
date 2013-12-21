#!/usr/bin/env python2

import os
from sys import exit

from tools_ import logger
import plasma_control

#Stops people from running this program directly.
if __name__ == "__main__":
    print "This script should not be ran manually. It's apart of a package for the turbulence utility."
    exit()
    

#Sets needed variables
homeDir = os.path.expanduser("~")
fullPath = homeDir + "/.kde4/share/config/plasma-desktop-appletsrc"
wallpapersDir = "/usr/share/wallpapers"

#Checks the existence of plasmaRC
def plasmaRCExists():
    if os.path.isfile(fullPath):
        try:
            with open(fullPath):
                return True
        except IOError:
            return False
    else:
        return False
  
#Changes the wallpaper
def wallpaperChanger(wallpaperChoice):
  
    if not plasmaRCExists():
        print "You don't seem to have a " + fullPath + " file."
        return False
      
    wallpaperOptions = {
        "cherryJapan": "wallpaper=/usr/share/wallpapers/Cherry Japan",
        "darkStairs": "wallpaper=/usr/share/wallpapers/Dark Stairs",
        "earthInSpace": "wallpaper=/usr/share/wallpapers/Earth In Space",
        "mountainLake": "wallpaper=/usr/share/wallpapers/Mountain Lake",
        "orangeSplash": "wallpaper=/usr/share/wallpapers/Orange Splash",
        "ozoneTurbulence": "wallpaper=/usr/share/wallpapers/Ozone-Turbulence",
        "sunsetPlane": "wallpaper=/usr/share/wallpapers/Sunset Plane",
        "whiteTiger": "wallpaper=/usr/share/wallpapers/White Tiger"
    }
  
    for wallpaperName, wallpaperPath in wallpaperOptions.items():
        if wallpaperChoice == wallpaperName:
            query = "wallpaper="
            with open(fullPath, 'rw') as search:
                for line in search:
                    line = line.rstrip()
                    if line.startswith(query):
                        search.close()
                        break
            plasmaRCRead = open(fullPath).read()
            plasmaRCRead = plasmaRCRead.replace(line, wallpaperPath)
            plasmaRCWrite = open(fullPath, 'w')
            plasmaRCWrite.write(plasmaRCRead)
            plasmaRCWrite.close()
            logger.writeLog('changedWallpaper', wallpaperChoice)
            return True

#Changes the wallpaper plus restarts plasma
def changeWallpaperPlus(wallpaper):
    plasma_control.killPlasma()
    wallpaperChanger(wallpaper)
    plasma_control.startPlasma()