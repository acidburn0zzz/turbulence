#!/usr/bin/bash

if [ $EUID != 0 ]; then
    echo "This script needs to be ran as root! Exiting..."
    exit
fi

if [ `printf '%s\n' "${PWD##*/}"` != "turbulence" ] && [ `printf '%s\n' "${PWD##*/}"` != "turbulence-evolution" ]; then
    if [ -f "turbulencerunner" ] && [ -f "turbulence" ] && [ -d "GUI_" ] && [ -d "tools_" ] && [ -d "stylesheets" ]; then
        echo -e " This directory isn't named properly, but I detected enough files to run. If you're not running this script\n"\
              "with the intention of installing or removing Turbulence, then you should press ctrl ^C now. Otherwise, hit enter"
        read someVar
    else
        echo "This script needs to be ran in the turbulence directory. Exiting..."
        exit
    fi
fi

if [ "$1" == "--remove" ] || [ "$1" == "-r" ]; then
    echo "Removing turbulence..."
    rm -rf '/usr/share/wallpapers/Cherry Japan'
    rm -rf '/usr/share/wallpapers/Dark Stairs'
    rm -rf '/usr/share/wallpapers/Earth In Space'
    rm -rf '/usr/share/wallpapers/manjaro-style-turbulence'
    rm -rf '/usr/share/wallpapers/Mountain Lake'
    rm -rf '/usr/share/wallpapers/Orange Splash'
    rm -rf '/usr/share/wallpapers/Ozone-Turbulence'
    rm -rf '/usr/share/wallpapers/Sunset Plane'
    rm -rf '/usr/share/wallpapers/White Tiger'
    rm -rf '/usr/share/backgrounds/Cherry Japan.jpg'
    rm -rf '/usr/share/backgrounds/Dark Stairs.jpg'
    rm -rf '/usr/share/backgrounds/Earth In Space.jpg'
    rm -rf '/usr/share/backgrounds/Mountain Lake.jpg'
    rm -rf '/usr/share/backgrounds/Orange Splash.jpg'
    rm -rf '/usr/share/backgrounds/Ozone-Turbulence.jpg'
    rm -rf '/usr/share/backgrounds/Sunset Plane.jpg'
    rm -rf '/usr/share/backgrounds/White Tiger.jpg'
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

if [ ! -d "/usr/share/backgrounds" ]; then
    mkdir /usr/share/backgrounds
    echo "Needed to create the /usr/share/backgrounds directory."
fi
echo "Copying the wallpapers into /usr/share/backgrounds..."
mv /usr/share/turbulence/backgrounds/* /usr/share/backgrounds
rm -r /usr/share/turbulence/backgrounds

echo "Generating translations..."
cd /usr/share/turbulence/tr
lrelease-qt4 /usr/share/turbulence/tr/*
cd

echo "Cleaning up some unneeded files..."
rm -r /usr/share/turbulence/translate.pro
rm -r /usr/share/turbulence/install.sh
rm -r /usr/share/turbulence/create_ts

echo "Changing permissions..."
chmod +x /usr/bin/turbulence
chmod +x /usr/share/turbulence/turbulencerunner

echo "Successfully installed turbulence."
echo "Please note that some dependencies you may need in order to run turbulence are"
echo "-python2"
echo "-python2-pyqt4"
echo "-pyqt4-common"
echo "-qt4"
echo "-kdeplasma-theme-cupertino-ish"
echo "-kde-theme-air-black-remix-green"
