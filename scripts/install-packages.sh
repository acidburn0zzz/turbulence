#!/usr/bin/bash

# trap ctrl-c and call ctrl_c()
trap ctrl_c INT

function ctrl_c() {
	clear
    echo """
Thank you for using the Turbulence package
installation script.

Press enter to exit this script
"""
    read exitCode
    exit 1
}

argsTrim=`echo "$@" | sed 's/\"//g'`
argsInstall=${argsTrim%-r*}
argsRemove=`echo "$argsTrim" | sed -e 's/.*-r//g'`

clear
echo """
 _____          _           _                     
|_   _|        | |         | |                    
  | |_   _ _ __| |__  _   _| | ___ _ __   ___ ___ 
  | | | | | '__| '_ \\| | | | |/ _ \\ '_ \\ / __/ _ \\
  | | |_| | |  | |_) | |_| | |  __/ | | | (_|  __/
  \\_/\\__,_|_|  |_.__/ \__,_|_|\___|_| |_|\\___\\___|
  
Please enter your root password, and Turbulence will 
start to install, or remove your selected packages.
"""

if [ "$argsInstall" != " " ] && [ "$argsInstall" != "" ]; then
    echo """
Turbulence will sync your mirrors first, so if pacman
tells you that you should update anything first, then
it is reccomended that you accept. You're packages
will not be installed in that case, so after the update 
has completed type \"install again\" when you're prompted.

Installing packages...
"""
    sudo pacman -Syy
    sudo pacman -S $argsInstall

    clear
    echo """
Are you satisfied with your install? If your packages
did not install due to a reccomended update first, then
this is the time when you would input \"install again\"
without the qoutes.

Otherwise, hit enter to proceed.
"""
    read proceed

    if [ "$proceed" == "install again" ] || [ "$proceed" == "\"install again\"" ]; then
        echo """
Installing your selected packages again...

You may need to re-enter your root password again.
"""
        sudo pacman -S $argsInstall
    fi
    clear
fi
if [ "$argsRemove" != " " ] && [ "$argsRemove" != "" ]; then
    echo """
Starting to remove all of your selected packages...
"""

    sudo pacman -Rs $argsRemove
fi

clear
echo """
Done!

Press enter to close this installer...
"""

read exitCode
exit 0
