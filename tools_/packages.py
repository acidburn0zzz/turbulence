#!/usr/bin/env python2

import urllib2
import subprocess
from sys import exit
from os import system

from tools_ import logger

packagesInstallAdditions = {
    "yaourt": ["autoconf", "automake", "binutils", "bison", "fakeroot", "file", "findutils", "flex", "gawk", "gcc", "gettext", "grep", "groff", "gzip", "libtool", "m4", "make", "patch", "pkg-config", "sed", "sudo", "texinfo", "util-linux", "which", "locale-info"],
    "flashplugin": ["a52dec", "faac", "faad2", "flac", "jasper", "lame", "libdca", "libdv", "libmad", "libmpeg2", "libtheora", "libvorbis", "libxv", "wavpack", "x264", "xvidcore", "gstreamer0.10-bad-plugins", "gstreamer0.10-base-plugins", "gstreamer0.10-ffmpeg", "gstreamer0.10-good-plugins", "gstreamer0.10-ugly-plugins",]
}
packagesRemoveAdditions = {
    "thunar": ["thunar-volman", "thunar-archive-plugin"]
}

#Stops people from running this program directly.
if __name__ == "__main__":
    print "This script should not be ran manually. It's apart of a package for the turbulence utility."
    exit()
    

def checkInternet():
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
    
    packagesTBIListUnedited = list(set(packagesTBI) - set(currentPackages)) #Packages to be installed
    packagesTBIList = packagesTBIListUnedited
    for packageName, packagesAdditions in packagesInstallAdditions.items():
        if packageName in packagesTBIListUnedited:
            packagesTBIList = packagesTBIList + packagesInstallAdditions[packageName]
    
    packagesTBIStr = ' '.join(packagesTBIList)
    logger.writeLog("packagesToBeInstalled", packagesTBIStr)
    packagesTBNList = list(set(currentPackages) - set(packagesTBR)) #Packages that don't need to be removed or installed (neutral).
    
    packagesTBRListUnedited = list(set(currentPackages) - set(packagesTBNList)) #Packages to be removed
    packagesTBRList = packagesTBRListUnedited
    for packageName, packagesAdditions in packagesInstallAdditions.items():
        if packageName in packagesTBRListUnedited:
            packagesTBRList = packagesTBRList + packagesRemoveAdditions[packageName]
    
    packagesTBRStr = ' '.join(packagesTBRList)
    logger.writeLog("packagesToBeRemoved", packagesTBRStr)
    
    installPackages = subprocess.Popen(["lxterminal", "-e", "bash",  "/usr/share/turbulence/scripts/install-packages.sh", "\"" + ' '.join(packagesTBIList) + "\"", "-r", "\"" + ' '.join(packagesTBRList) + "\""])
    installPackages.wait()
    system("wmctrl -a LXTerminal")
