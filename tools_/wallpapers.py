#!/usr/bin/env python2

import os
import subprocess
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
  
def changeWallpaperOpenbox(wallpaperChoice, wallpaperOptions):
    for wallpaperName, wallpaperPath in wallpaperOptions.items():
        if wallpaperChoice == wallpaperName:
            setWallpaper = subprocess.Popen(["nitrogen", "--set-scaled", "--save", wallpaperPath], stdout=subprocess.PIPE)
            setWallpaper.wait()
            logger.writeLog("changedWallpaper", wallpaperName)
            
def changeWallpaperKde(wallpaperChoice, wallpaperOptions):
    if not plasmaRCExists():
        print "You don't seem to have a " + fullPath + " file."
        return False
      
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

#Changes the wallpaper
def wallpaperChanger(wallpaperChoice, edition):
    if edition == "kde":
        wallpaperOptions = {
            "cherryJapan": "wallpaper=/usr/share/wallpapers/Cherry Japan",
            "darkStairs": "wallpaper=/usr/share/wallpapers/Dark Stairs",
            "earthInSpace": "wallpaper=/usr/share/wallpapers/Earth In Space",
            "mountainLake": "wallpaper=/usr/share/wallpapers/Mountain Lake",
            "orangeSplash": "wallpaper=/usr/share/wallpapers/Orange Splash",
            "manjarostyle": "wallpaper=/usr/share/wallpapers/manjaro-style",
            "sunsetPlane": "wallpaper=/usr/share/wallpapers/Sunset Plane",
            "whiteTiger": "wallpaper=/usr/share/wallpapers/White Tiger"
        }
        changeWallpaperKde(wallpaperChoice, wallpaperOptions)
    elif edition == "openbox":
        wallpaperOptions = {
            "cherryJapan": "/usr/share/backgrounds/Cherry Japan.jpg",
            "darkStairs": "/usr/share/backgrounds/Dark Stairs.jpg",
            "earthInSpace": "/usr/share/backgrounds/Earth In Space.jpg",
            "mountainLake": "/usr/share/backgrounds/Mountain Lake.jpg",
            "evolight": "/usr/share/backgrounds/evolight.jpg",
            "evodark": "/usr/share/backgrounds/evodark.jpg",
            "sunsetPlane": "/usr/share/backgrounds/Sunset Plane.jpg",
            "whiteTiger": "/usr/share/backgrounds/White Tiger.jpg"
        }
        changeWallpaperOpenbox(wallpaperChoice, wallpaperOptions)
    else:
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
        changeWallpaperKde(wallpaperChoice, wallpaperOptions)

#Changes the wallpaper plus restarts plasma
def changeWallpaperPlus(wallpaper, edition):
    if edition == "openbox":
        wallpaperChanger(wallpaper, edition)
        return True
    elif edition == "kde":
        plasma_control.killPlasma()
        wallpaperChanger(wallpaper, edition)
        plasma_control.startPlasma()
        return True
    else:
        plasma_control.killPlasma()
        wallpaperChanger(wallpaper, edition)
        plasma_control.startPlasma()
        return True
        