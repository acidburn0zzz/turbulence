#!/usr/bin/bash

#checks that user is root.
if [ $EUID != 0 ]; then
    echo "This script needs to be ran as root! Exiting..."
    exit
fi

if [ `printf '%s\n' "${PWD##*/}"` != "turbulence" ]; then
    echo "This scrip needs to be ran in the turbulence directory. Exiting..."
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
mv wallpapers/* /usr/share/wallpapers
rm -r /usr/share/wallpapers

echo "Copying the turbulence executable..."
mv /usr/share/turbulence/turbulence /usr/bin

if [ -d "/usr/share/apps/aurorae/themes/ghost-deco-2_2" ]; then
    echo "Ghost theme already installed. Skipping copying the Ghost theme."
else
    echo "Creating the themes directory for aurorae..."
    mkdir -p /usr/share/apps/aurorae/themes
    echo "Copying the Ghost theme..."
    mv /usr/share/turbulence/themes/* /usr/share/apps/aurorae/themes
    rm -r /usr/share/turbulence/themes
fi

echo "Changing permissions..."
chmod +x /usr/bin/turbulence
chmod +x /usr/share/turbulence/turbulencerunner

echo "Successfully installed turbulence."
echo "Please note that some dependencies you may need in order to run turbulence are"
echo "-python2"
echo "-python2-pyqt4"
echo "-pyqt4-common"
echo "-qt4"