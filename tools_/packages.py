#!/usr/bin/env python

import subprocess
import urllib.request, urllib.error
from sys import exit
from os import system
from time import sleep

from tools_ import logger

packagesInstallAdditions = {
    "yaourt": ["autoconf", "automake", "binutils", "bison", "fakeroot", "file", "findutils", "flex", "gawk", "gcc", "gettext", "grep", "groff", "gzip", "libtool", "m4", "make", "patch", "pkg-config", "sed", "sudo", "texinfo", "util-linux", "which", "locale-info"],
    "flashplugin": ["a52dec", "faac", "faad2", "flac", "jasper", "lame", "libdca", "libdv", "libmad", "libmpeg2", "libtheora", "libvorbis", "libxv", "wavpack", "x264", "xvidcore", "gst-plugins-bad", "gst-plugins-base", "gst-plugins-base-libs", "gst-plugins-good", "gst-plugins-ugly", "gstreamer0.10-bad-plugins", "gstreamer0.10-base-plugins", "gstreamer0.10-ffmpeg", "gstreamer0.10-good-plugins", "gstreamer0.10-ugly-plugins"],
    "thunar": ["thunar-volman", "thunar-archive-plugin"],
    "transmission-gtk": ["transmission-cli"]
}
packagesRemoveAdditions = {
    "thunar": ["thunar-volman", "thunar-archive-plugin"]
}

#Stops people from running this program directly.
if __name__ == "__main__":
    print("This script should not be ran manually. It's apart of a package for the turbulence utility.")
    exit()
    

def checkInternet():
    try:
        response=urllib.request.urlopen('http://74.125.228.100',timeout=20)
        return True
    except urllib.error.URLError as err: pass
    return False
    
def getCurrentPackages():
        packagesText = subprocess.check_output("pacman -Qq", shell=True)
        packagesList = packagesText.decode("utf-8").split("\n")
        return packagesList

def handlePackages(packagesTBI, packagesTBR): #packagesTBI = packages to be installed #packagesTBR = packages to br removed
    currentPackages = getCurrentPackages()
    
    packagesTBIListUnedited = list(set(packagesTBI) - set(currentPackages)) #Packages to be installed
    packagesTBNList = list(set(currentPackages) - set(packagesTBR)) #Packages that don't need to be removed or installed (neutral).
    packagesTBRListUnedited = list(set(currentPackages) - set(packagesTBNList)) #Packages to be removed
    
    packagesTBIList = packagesTBIListUnedited
    for packageName, packagesAdditions in packagesInstallAdditions.items():
        if packageName in packagesTBIListUnedited:
            packagesTBIList = packagesTBIList + list(set(packagesInstallAdditions[packageName]) - set(packagesTBNList))
    
    packagesTBRList = packagesTBRListUnedited
    for packageName, packagesAdditions in packagesRemoveAdditions.items():
        if packageName in packagesTBRListUnedited:
            packagesTBRList = packagesTBRList + list(set(packagesRemoveAdditions[packageName]) & set(packagesTBNList))
    
    packagesTBIStr = ' '.join(packagesTBIList)
    packagesTBRStr = ' '.join(packagesTBRList)
    logger.writeLog("packagesToBeInstalled", packagesTBIStr)
    logger.writeLog("packagesToBeRemoved", packagesTBRStr)
    
    installPackages = subprocess.Popen(["lxterminal", "-e", "bash",  "/usr/share/turbulence/scripts/install-packages.sh", "\"" + ' '.join(packagesTBIList) + "\"", "-r", "\"" + ' '.join(packagesTBRList) + "\""])
    sleep(2)
    system("wmctrl -a LXTerminal")
