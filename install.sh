#!/usr/bin/bash

if [ $EUID != 0 ]; then
    echo "This script needs to be ran as root! Exiting..."
    exit
fi

if [ `printf '%s\n' "${PWD##*/}"` != "turbulence" ]; then
    echo "This scrip needs to be ran in the turbulence directory. Exiting..."
    exit
fi

if [ "$1" == "--remove" ] || [ "$1" == "-r" ]; then
    echo "Removing turbulence..."
    rm -rf '/usr/share/wallpapers/Cherry Japan'
    rm -rf '/usr/share/wallpapers/Dark Stairs'
    rm -rf '/usr/share/wallpapers/Earth In Space'
    rm -rf '/usr/share/wallpapers/Mountain Lake'
    rm -rf '/usr/share/wallpapers/Orange Splash'
    rm -rf '/usr/share/wallpapers/Ozone-Turbulence'
    rm -rf '/usr/share/wallpapers/Sunset Plane'
    rm -rf '/usr/share/wallpapers/White Tiger'
    rm -f /usr/bin/turbulence
    rm -rf /usr/share/turbulence
    exit
fi

echo "Installing turbulence..."

if [ ! -d "/usr/share/turbulence" ]; then
    mkdir /usr/share/turbulence
    echo "Created the directory /usr/share/turbulence."
else
    echo "Could not create the directory /usr/share/turbulence since it already existed. Do you already have turbulence installed? Exiting..."
    exit
fi

echo "Copying data to turbulence directory..."
cp -r * /usr/share/turbulence

if [ ! -d "/usr/share/wallpapers" ]; then
    mkdir /usr/share/wallpapers
    echo "Needed to create the /usr/share/wallpapers directory."
fi
echo "Copying the wallpapers into /usr/share/wallpapers..."
mv /usr/share/turbulence/wallpapers/* /usr/share/wallpapers
rm -r /usr/share/turbulence/wallpapers

echo "Copying the turbulence executable..."
mv /usr/share/turbulence/turbulence /usr/bin

if [ -d "/usr/share/apps/aurorae/themes/ghost-deco-2_2" ]; then
    echo "Ghost theme already installed. Skipping copying the Ghost theme."
    sudo rm -r /usr/share/turbulence/themes/ghost-deco-2_2
else
    echo "Creating the themes directory for aurorae..."
    mkdir -p /usr/share/apps/aurorae/themes
    echo "Copying the Ghost theme..."
    mv /usr/share/turbulence/themes/ghost-deco-2_2 /usr/share/apps/aurorae/themes
    rm -r /usr/share/turbulence/themes/ghost-deco-2_2
fi

if [ -d "/usr/share/apps/aurorae/themes/cupertino-ish" ]; then
    echo "Cupertino-ish theme already installed. Skipping Copying the Cupertino-ish theme."
    rm -r /usr/share/turbulence/themes
else
    echo "Copying the Cupertino-ish theme"
    mv /usr/share/turbulence/themes/* /usr/share/apps/aurorae/themes
    rm -r /usr/share/turbulence/themes
fi

echo "Generating translations..."
cd /usr/share/turbulence/tr
lrelease-qt4 /usr/share/turbulence/tr/*
cd

echo "Changing permissions..."
chmod +x /usr/bin/turbulence
chmod +x /usr/share/turbulence/turbulencerunner

echo "Successfully installed turbulence."
echo "Please note that some dependencies you may need in order to run turbulence are"
echo "-python2"
echo "-python2-pyqt4"
echo "-pyqt4-common"
echo "-qt4"