# What is Turbulence?

Turbulence is a utility similar to Chakra's kapudan, that
configures multiple aspects of Openbox and KDE Desktop at 
first boot. Some of it's features are:

* Sleak grey graphical layout
* Provides information of Manjaro to new users
* Provides process detection to better serve configuration options based on what you're running
* Can allow the user to easily select which Folders he wants in his home directory
* Allows users to select which placement for their tint2 (OpenBox)
* Allows users to select which wallpaper they want (Openbox/KDE)
* Allows users to select what packages they want and don't want (OpenBox only for now.)
* Can also allow people to open system settings after they've ran through everything else to set any last minute details

# How to install Turbulence

To install Turbulence, just run the following commands.

```
git clone http://git.manjaro.org/community/turbulence.git turbulence
cd turbulence
chmod +x install.sh
sudo bash install.sh
```

# How to remove Turbulence

To remove Turbulence, just `cd` to the turbulence directory and run the following command.

```
sudo bash install.sh -r
```

# Dependencies

* python
* python-pyqt5
* pyqt5-common
* qt5-base
* wmctrl

# Optional Dependencies

* lxterminal
* kdeplasma-theme-cupertino-ish
* kde-theme-air-black-remix-green

# Roadmap and TODO

* Add package selection support to KDE
* Code Clean up and restructure
* Add a config file
* Add more settings to configure KDE options as well as OpenBox
* Figure out alternatives to opening a terminal with the pacman installer script