#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#Import needed libraries
from PyQt4 import QtCore, QtGui
from tools_ import * 


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

def widgetConfigurer(widgetType, xPos, yPos, xSize, ySize, name, image=None, styleSheet=None):
    widgetType.setGeometry(QtCore.QRect(xPos, yPos, xSize, ySize))
    widgetType.setObjectName(_fromUtf8(name))
    
    if image != None:
        widgetType.setPixmap(QtGui.QPixmap(_fromUtf8(image)))
        
    if styleSheet != None:
        widgetType.setStyleSheet(_fromUtf8(styleSheet))
        
def createStaticWidgets(parent):
    global blackBackground; blackBackground = QtGui.QLabel(parent)
    global headerBack; headerBack = QtGui.QLabel(parent)
    global turbulenceLogo; turbulenceLogo = QtGui.QLabel(parent)
    global menuBackg; menuBackg = QtGui.QLabel(parent)
    global footerBack; footerBack = QtGui.QLabel(parent)
    
    staticWidgets = {
        "blackBackground": [blackBackground, -14, 0, 891, 625, "blackBackground", "/usr/share/turbulence/images/manjaro-grey/background.jpg"],
        "headerBack": [headerBack, -20, 10, 921, 71, "headerBack", "/usr/share/turbulence/images/manjaro-grey/header.png"],
        "turbulenceLogo": [turbulenceLogo, 20, 20, 51, 51, "turbulenceLogo", "/usr/share/turbulence/images/manjaro-grey/turbulence.png"],
        "menuBackg": [menuBackg, -20, 90, 901, 41, "menuBackg", None],
        "footerBack": [footerBack, 0, 570, 861, 51, "footerBack", None]
    }
    
    for widgetName, widgetSettings in staticWidgets.items():
        widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])

    return blackBackground, headerBack, turbulenceLogo, menuBackg, footerBack


#Begins to main class
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
      
        #Grabs the stylesheet
        styleSheetFile = open("/usr/share/turbulence/stylesheets/manjarogrey.stylesheet", "r")
        self.styleData = styleSheetFile.read()
        styleSheetFile.close()
      
        #Sets up the main window
        MainWindow.setObjectName(_fromUtf8("Turbulence"))
        MainWindow.resize(839, 594)
        MainWindow.setMinimumSize(QtCore.QSize(839, 594))
        MainWindow.setMaximumSize(QtCore.QSize(839, 594))
        MainWindow.setStyleSheet(_fromUtf8(""))
        MainWindow.setWindowIcon(QtGui.QIcon('/usr/share/turbulence/images/manjaro-grey/turbulence.png'))
        MainWindow.setStyleSheet(self.styleData)
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        #Defines the stacked widget
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        widgetConfigurer(self.stackedWidget, -10, -20, 861, 621, "stackedWidget", None, None)
        
        #Starts the first page in the stacked widget, or Manjaro welcome
        self.welcomeToManjaro = QtGui.QWidget()
        self.welcomeToManjaro.setObjectName(_fromUtf8("welcomeToManjaro"))

        #Defines all the widgets
        createStaticWidgets(self.welcomeToManjaro)
        self.header = QtGui.QLabel(self.welcomeToManjaro)
        self.welcomeButton = QtGui.QPushButton(self.welcomeToManjaro)
        self.arrow = QtGui.QLabel(self.welcomeToManjaro)
        self.folders2 = QtGui.QPushButton(self.welcomeToManjaro)
        self.whatIsManjaro = QtGui.QLabel(self.welcomeToManjaro)
        self.manjaroDesc = QtGui.QLabel(self.welcomeToManjaro)
        self.bullet1 = QtGui.QLabel(self.welcomeToManjaro)
        self.bullet2 = QtGui.QLabel(self.welcomeToManjaro)
        self.bullet3 = QtGui.QLabel(self.welcomeToManjaro)
        self.bullet4 = QtGui.QLabel(self.welcomeToManjaro)
        self.forward = QtGui.QPushButton(self.welcomeToManjaro)
        self.cancel = QtGui.QPushButton(self.welcomeToManjaro)
        
        #widget dictionary
        firstPageWidgets = {
            "header": [self.header, 80, 20, 281, 51, "header", None],
            "welcomeButton": [self.welcomeButton, 20, 90, 111, 41, "welcomeButton", None],
            "arrow": [self.arrow, 140, 90, 111, 41, "arrow", "/usr/share/turbulence/images/manjaro-grey/arrow.png"],
            "folders2": [self.folders2, 170, 90, 81, 41, "folders2", None],
            "whatIsManjaro": [self.whatIsManjaro, 30, 180, 351, 71, "whatIsManjaro", None],
            "manjaroDesc": [self.manjaroDesc, 70, 260, 651, 261, "manjaroDesc", None],
            "bullet1": [self.bullet1, 70, 365, 21, 21, "bullet1", "/usr/share/turbulence/images/manjaro-grey/bullet.png"],
            "bullet2": [self.bullet2, 70, 395, 21, 21, "bullet2", "/usr/share/turbulence/images/manjaro-grey/bullet.png"],
            "bullet3": [self.bullet3, 70, 425, 21, 21, "bullet3", "/usr/share/turbulence/images/manjaro-grey/bullet.png"],
            "bullet4": [self.bullet4, 70, 470, 21, 21, "bullet4", "/usr/share/turbulence/images/manjaro-grey/bullet.png"],
            "forward": [self.forward, 740, 575, 101, 33, "forward", None],
            "cancel": [self. cancel, 20, 575, 91, 33, "cancel", None],
        }
        
        #defines all the widget parameters
        for widgetName, widgetSettings in firstPageWidgets.items():
            widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
        
        #defines all the custom settings
        self.welcomeButton.setFlat(True)
        self.folders2.setFlat(True)
        self.forward.setFlat(True)
        self.cancel.setFlat(True)
        
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("/usr/share/turbulence/images/manjaro-grey/arrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.forward.setIcon(icon1)
        self.forward.setIconSize(QtCore.QSize(28, 30))
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("/usr/share/turbulence/images/manjaro-grey/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel.setIcon(icon)
        
        #adds the first page
        self.stackedWidget.addWidget(self.welcomeToManjaro)
        
        
        #Starts the second page in the stacked widget.
        self.folders = QtGui.QWidget()
        self.folders.setObjectName(_fromUtf8("folders"))
        
        #Defines all the widget for the second page
        createStaticWidgets(self.folders)
        
        self.header2 = QtGui.QLabel(self.folders)
        self.foldersHead = QtGui.QPushButton(self.folders)
        self.arrow2 = QtGui.QLabel(self.folders)
        self.themes = QtGui.QPushButton(self.folders)
        self.cancel2 = QtGui.QPushButton(self.folders)
        self.forward2 = QtGui.QPushButton(self.folders)
        self.previous = QtGui.QPushButton(self.folders)
        self.folderIcon = QtGui.QLabel(self.folders)
        self.folderDesc = QtGui.QLabel(self.folders)
        self.folderHeaderHead = QtGui.QLabel(self.folders)
        self.folderIcon1 = QtGui.QLabel(self.folders)
        self.folderIcon2 = QtGui.QLabel(self.folders)
        self.folderIcon3 = QtGui.QLabel(self.folders)
        self.folderIcon4 = QtGui.QLabel(self.folders)
        self.folderIcon5 = QtGui.QLabel(self.folders)
        self.folderIcon6 = QtGui.QLabel(self.folders)
        self.folderIcon7 = QtGui.QLabel(self.folders)
        self.folderIcon8 = QtGui.QLabel(self.folders)
        self.folderHeader1 = QtGui.QLabel(self.folders)
        self.folderHeader2 = QtGui.QLabel(self.folders)
        self.folderHeader3 = QtGui.QLabel(self.folders)
        self.folderHeader4 = QtGui.QLabel(self.folders)
        self.folderHeader5 = QtGui.QLabel(self.folders)
        self.folderHeader6 = QtGui.QLabel(self.folders)
        self.folderHeader7 = QtGui.QLabel(self.folders)
        self.folderHeader8 = QtGui.QLabel(self.folders)
        self.folderName1 = QtGui.QLabel(self.folders)
        self.folderName2 = QtGui.QLabel(self.folders)
        self.folderName3 = QtGui.QLabel(self.folders)
        self.folderName4 = QtGui.QLabel(self.folders)
        self.folderName5 = QtGui.QLabel(self.folders)
        self.folderName6 = QtGui.QLabel(self.folders)
        self.folderName7 = QtGui.QLabel(self.folders)
        self.folderName8 = QtGui.QLabel(self.folders)
        self.folderActive1 = QtGui.QCheckBox(self.folders)
        self.folderActive2 = QtGui.QCheckBox(self.folders)
        self.folderActive3 = QtGui.QCheckBox(self.folders)
        self.folderActive4 = QtGui.QCheckBox(self.folders)
        self.folderActive5 = QtGui.QCheckBox(self.folders)
        self.folderActive6 = QtGui.QCheckBox(self.folders)
        self.folderActive7 = QtGui.QCheckBox(self.folders)
        self.folderActive8 = QtGui.QCheckBox(self.folders)
        
        #widget dictionary. Almost like a bestiary of QT ^_^
        secondPageWidgets = {
            "header2": [self.header2, 80, 20, 111, 51, "header2", None],
            "foldersHead": [self.foldersHead, 20, 90, 91, 41, "foldersHead", None],
            "arrow2": [self.arrow2, 120, 90, 31, 41, "arrow2", "/usr/share/turbulence/images/manjaro-grey/arrow.png"],
            "themes": [self.themes, 150, 90, 91, 41, "themes", None],
            "cancel2": [self.cancel2, 20, 575, 91, 33, "cancel2", None],
            "forward2": [self.forward2, 740, 575, 101, 33, "forward2", None],
            "previous": [self.previous, 630, 575, 101, 33, "previous", None],
            "folderIcon": [self.folderIcon, 40, 150, 61, 61, "folderIcon", "/usr/share/turbulence/images/manjaro-grey/foldericons/folder.png"],
            "folderDesc": [self.folderDesc, 110, 170, 591, 31, "folderDesc", None],
            "folderHeaderHead": [self.folderHeaderHead, 50, 240, 81, 31, "folderHeaderHead", None],
            "folderIcon1": [self.folderIcon1, 60, 290, 81, 81, "folderIcon1", "/usr/share/turbulence/images/manjaro-grey/foldericons/desktop.png"],
            "folderIcon2": [self.folderIcon2, 60, 440, 81, 81, "folderIcon2", "/usr/share/turbulence/images/manjaro-grey/foldericons/pictures.png"],
            "folderIcon3": [self.folderIcon3, 270, 290, 81, 81, "folderIcon3", "/usr/share/turbulence/images/manjaro-grey/foldericons/documents.png"],
            "folderIcon4": [self.folderIcon4, 690, 290, 81, 81, "folderIcon4", "/usr/share/turbulence/images/manjaro-grey/foldericons/music.png"],
            "folderIcon5": [self.folderIcon5, 480, 290, 81, 81, "folderIcon5", "/usr/share/turbulence/images/manjaro-grey/foldericons/downloads.png"],
            "folderIcon6": [self.folderIcon6, 270, 440, 81, 81, "folderIcon6", "/usr/share/turbulence/images/manjaro-grey/foldericons/public.png"],
            "folderIcon7": [self.folderIcon7, 480, 440, 81, 81, "folderIcon7", "/usr/share/turbulence/images/manjaro-grey/foldericons/templates.png"],
            "folderIcon8": [self.folderIcon8, 690, 440, 81, 81, "folderIcon8", "/usr/share/turbulence/images/manjaro-grey/foldericons/videos.png"],
            "folderHeader1": [self.folderHeader1, 50, 371, 131, 21, "folderHeader1", None],
            "folderHeader2": [self.folderHeader2, 260, 371, 131, 21, "folderHeader2", None],
            "folderHeader3": [self.folderHeader3, 470, 370, 131, 21, "folderHeader3", None],
            "folderHeader4": [self.folderHeader4, 680, 370, 131, 21, "folderHeader4", None],
            "folderHeader5": [self.folderHeader5, 50, 520, 131, 21, "folderHeader5", None],
            "folderHeader6": [self.folderHeader6, 260, 520, 131, 21, "folderHeader6", None],
            "folderHeader7": [self.folderHeader7, 470, 520, 131, 21, "folderHeader7", None],
            "folderHeader8": [self.folderHeader8, 680, 520, 131, 21, "folderHeader8", None],
            "folderName1": [self.folderName1, 69, 270, 71, 21, "folderName1", None],
            "folderName2": [self.folderName2, 265, 270, 91, 21, "folderName2", None],
            "folderName3": [self.folderName3, 477, 270, 91, 21, "folderName3", None],
            "folderName4": [self.folderName4, 708, 270, 91, 21, "folderName4", None],
            "folderName5": [self.folderName5, 70, 420, 71, 21, "folderName5", None],
            "folderName6": [self.folderName6, 288, 420, 51, 21, "folderName6", None],
            "folderName7": [self.folderName7, 482, 420, 81, 21, "folderName7", None],
            "folderName8": [self.folderName8, 702, 420, 61, 20, "folderName8", None],
            "folderActive1": [self.folderActive1, 50, 390, 71, 21, "folderActive1", None],
            "folderActive2": [self.folderActive2, 260, 390, 71, 21, "folderActive2", None],
            "folderActive3": [self.folderActive3, 470, 390, 71, 21, "folderActive3", None],
            "folderActive4": [self.folderActive4, 680, 390, 71, 21, "folderActive4", None],
            "folderActive5": [self.folderActive5, 50, 540, 71, 21, "folderActive5", None],
            "folderActive6": [self.folderActive6, 260, 540, 71, 21, "folderActive6", None],
            "folderActive7": [self.folderActive7, 470, 540, 71, 21, "folderActive7", None],
            "folderActive8": [self.folderActive8, 680, 540, 71, 21, "folderActive8", None]
        }
        
        #defines all the widget parameters
        for widgetName, widgetSettings in secondPageWidgets.items():
            widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
        
        #defines the custom settings
        self.foldersHead.setFlat(True)
        self.themes.setFlat(True)
        self.cancel2.setFlat(True)
        self.forward2.setFlat(True)
        self.previous.setFlat(True)
        
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("/usr/share/turbulence/images/manjaro-grey/arrowreverse.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous.setIcon(icon2)
        
        self.forward2.setIconSize(QtCore.QSize(28, 30))
        self.previous.setIconSize(QtCore.QSize(28, 30))
        
        self.cancel2.setIcon(icon)
        self.forward2.setIcon(icon1)
        
        #adds the second page
        self.stackedWidget.addWidget(self.folders)
        
        
        #Starts the third page in the stacked widget.
        self.Theme = QtGui.QWidget()
        self.Theme.setObjectName(_fromUtf8("Theme"))
        
        createStaticWidgets(self.Theme)
        self.header3 = QtGui.QLabel(self.Theme)
        self.themesMenu = QtGui.QPushButton(self.Theme)
        self.arrow3 = QtGui.QLabel(self.Theme)
        self.menuWallpapers = QtGui.QPushButton(self.Theme)
        self.cancel3 = QtGui.QPushButton(self.Theme)
        self.forward3 = QtGui.QPushButton(self.Theme)
        self.previous2 = QtGui.QPushButton(self.Theme)
        self.themeIcon = QtGui.QLabel(self.Theme)
        self.folderDesc2 = QtGui.QLabel(self.Theme)
        self.themesHeader = QtGui.QLabel(self.Theme)
        self.themePreview1 = QtGui.QLabel(self.Theme)
        self.themePreview2 = QtGui.QLabel(self.Theme)
        self.themePreview3 = QtGui.QLabel(self.Theme)
        self.themePreview4 = QtGui.QLabel(self.Theme)
        self.themeRadio1 = QtGui.QRadioButton(self.Theme)
        self.themeRadio2 = QtGui.QRadioButton(self.Theme)
        self.themeRadio3 = QtGui.QRadioButton(self.Theme)
        self.themeRadio4 = QtGui.QRadioButton(self.Theme)
        
        thirdPageWidgets = {
            "header3": [self.header3, 80, 20, 111, 51, "header3", None],
            "themesMenu": [self.themesMenu, 20, 90, 91, 41, "themesMenu", None],
            "arrow3": [self.arrow3, 120, 90, 31, 41, "arrow3", "/usr/share/turbulence/images/manjaro-grey/arrow.png"],
            "menuWallpapers": [self.menuWallpapers, 150, 90, 111, 41, "menuWallpapers", None],
            "cancel3": [self.cancel3, 20, 575, 91, 33, "cancel3", None],
            "forward3": [self.forward3, 740, 575, 101, 33, "forward3", None],
            "previous2": [self.previous2, 630, 575, 101, 33, "previous2", None],
            "themeIcon": [self.themeIcon, 40, 160, 61, 61, "themeIcon", "/usr/share/turbulence/images/manjaro-grey/themes/theme.png"],
            "folderDesc2": [self.folderDesc2, 110, 167, 591, 51, "folderDesc2", None],
            "themesHeader": [self.themesHeader, 50, 240, 91, 31, "themesHeader", None],
            "themePreview1": [self.themePreview1, 90, 280, 241, 81, "themePreview1", "/usr/share/turbulence/images/manjaro-grey/themes/ozone.png"],
            "themePreview2": [self.themePreview2, 510, 280, 241, 81, "themePreview2", "/usr/share/turbulence/images/manjaro-grey/themes/laptop.png"],
            "themePreview3": [self.themePreview3, 90, 410, 241, 81, "themePreview3", "/usr/share/turbulence/images/manjaro-grey/themes/oxygen.png"],
            "themePreview4": [self.themePreview4, 510, 410, 241, 81, "themePreview4", "/usr/share/turbulence/images/manjaro-grey/themes/plastik.png"],
            "themeRadio1": [self.themeRadio1, 170, 370, 81, 21, "themeRadio1", None],
            "themeRadio2": [self.themeRadio2, 590, 370, 81, 21, "themeRadio2", None],
            "themeRadio3": [self.themeRadio3, 167, 500, 91, 21, "themeRadio3", None],
            "themeRadio4": [self.themeRadio4, 591, 510, 91, 21, "themeRadio4", None]
        }
        
        #defines all the widget parameters
        for widgetName, widgetSettings in thirdPageWidgets.items():
            widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
        
        #Defines the custom settings
        self.themesMenu.setFlat(True)
        self.menuWallpapers.setFlat(True)
        self.cancel3.setFlat(True)
        self.forward3.setFlat(True)
        self.previous2.setFlat(True)
        
        self.cancel3.setIcon(icon)
        self.forward3.setIcon(icon1)
        self.previous2.setIcon(icon2)
        
        self.forward3.setIconSize(QtCore.QSize(28, 30))
        self.previous2.setIconSize(QtCore.QSize(28, 30))
        
        #Adds the third page
        self.stackedWidget.addWidget(self.Theme)
        
        
        #Starts code for fourth page
        self.Wallpaper = QtGui.QWidget()
        self.Wallpaper.setObjectName(_fromUtf8("Wallpaper"))
        
        #defines all the widgets
        createStaticWidgets(self.Wallpaper)
        
        self.header4 = QtGui.QLabel(self.Wallpaper)
        self.wallpapersMenu = QtGui.QPushButton(self.Wallpaper)
        self.arrow4 = QtGui.QLabel(self.Wallpaper)
        self.menuFinish = QtGui.QPushButton(self.Wallpaper)
        self.wallpaperIcon = QtGui.QLabel(self.Wallpaper)
        self.wallpaperDesc = QtGui.QLabel(self.Wallpaper)
        self.previous3 = QtGui.QPushButton(self.Wallpaper)
        self.forward4 = QtGui.QPushButton(self.Wallpaper)
        self.cancel4 = QtGui.QPushButton(self.Wallpaper)
        self.wallpaperHeader = QtGui.QLabel(self.Wallpaper)
        self.wallpaper1 = QtGui.QLabel(self.Wallpaper)
        self.wallpaper2 = QtGui.QLabel(self.Wallpaper)
        self.wallpaper3 = QtGui.QLabel(self.Wallpaper)
        self.wallpaper4 = QtGui.QLabel(self.Wallpaper)
        self.wallpaper5 = QtGui.QLabel(self.Wallpaper) 
        self.wallpaper6 = QtGui.QLabel(self.Wallpaper)
        self.wallpaper7 = QtGui.QLabel(self.Wallpaper)
        self.wallpaper8 = QtGui.QLabel(self.Wallpaper)
        self.wallpaperChoice1 = QtGui.QRadioButton(self.Wallpaper)
        self.wallpaperChoice2 = QtGui.QRadioButton(self.Wallpaper)
        self.wallpaperChoice3 = QtGui.QRadioButton(self.Wallpaper)
        self.wallpaperChoice4 = QtGui.QRadioButton(self.Wallpaper)
        self.wallpaperChoice5 = QtGui.QRadioButton(self.Wallpaper)
        self.wallpaperChoice6 = QtGui.QRadioButton(self.Wallpaper)
        self.wallpaperChoice7 = QtGui.QRadioButton(self.Wallpaper)
        self.wallpaperChoice8 = QtGui.QRadioButton(self.Wallpaper)
        
        fourthPageWidgets = {
            "header4": [self.header4, 80, 20, 161, 51, "header4", None],
            "wallpapersMenu": [self.wallpapersMenu, 20, 90, 121, 41, "wallpapersMenu", None],
            "arrow4": [self.arrow4, 150, 90, 31, 41, "arrow4", "/usr/share/turbulence/images/manjaro-grey/arrow.png"],
            "menuFinish": [self.menuFinish, 180, 90, 71, 41, "menuFinish", None],
            "wallpaperIcon": [self.wallpaperIcon, 40, 160, 61, 61, "wallpaperIcon", "/usr/share/turbulence/images/manjaro-grey/wallpapers/wallpapers.png"],
            "wallpaperDesc": [self.wallpaperDesc, 110, 160, 591, 51, "wallpaperDesc", None],
            "previous3": [self.previous3, 630, 575, 101, 33, "previous3", None],
            "forward4": [self.forward4, 740, 575, 101, 33, "forward4", None],
            "cancel4": [self.cancel4, 20, 575, 91, 33, "cancel4", None],
            "wallpaperHeader": [self.wallpaperHeader, 50, 240, 121, 31, "wallpaperHeader", None],
            "wallpaper1": [self.wallpaper1, 40, 280, 141, 91, "wallpaper1", "/usr/share/turbulence/images/manjaro-grey/wallpapers/ozone.png"],
            "wallpaper2": [self.wallpaper2, 250, 280, 141, 91, "wallpaper2", "/usr/share/turbulence/images/manjaro-grey/wallpapers/orangesplash.png"],
            "wallpaper3": [self.wallpaper3, 470, 280, 141, 91, "wallpaper3", "/usr/share/turbulence/images/manjaro-grey/wallpapers/sunsetplane.png"],
            "wallpaper4": [self.wallpaper4, 680, 280, 141, 91, "wallpaper4", "/usr/share/turbulence/images/manjaro-grey/wallpapers/mountainlake.png"],
            "wallpaper5": [self.wallpaper5, 40, 410, 141, 91, "wallpaper5", "/usr/share/turbulence/images/manjaro-grey/wallpapers/earthinspace.png"],
            "wallpaper6": [self.wallpaper6, 250, 410, 141, 91, "wallpaper6", "/usr/share/turbulence/images/manjaro-grey/wallpapers/darkstairs.png"],
            "wallpaper7": [self.wallpaper7, 470, 410, 141, 91, "wallpaper7", "/usr/share/turbulence/images/manjaro-grey/wallpapers/cherryjapan.png"],
            "wallpaper8": [self.wallpaper8, 680, 410, 141, 91, "wallpaper8", "/usr/share/turbulence/images/manjaro-grey/wallpapers/whitetiger.png"],
            "wallpaperChoice1": [self.wallpaperChoice1, 70, 380, 81, 21, "wallpaperChoice1", None],
            "wallpaperChoice2": [self.wallpaperChoice2, 250, 380, 141, 21, "wallpaperChoice2", None],
            "wallpaperChoice3": [self.wallpaperChoice3, 480, 380, 131, 21, "wallpaperChoice3", None],
            "wallpaperChoice4": [self.wallpaperChoice4, 680, 380, 141, 21, "wallpaperChoice4", None],
            "wallpaperChoice5": [self.wallpaperChoice5, 70, 510, 81, 21, "wallpaperChoice5", None],
            "wallpaperChoice6": [self.wallpaperChoice6, 262, 510, 111, 21, "wallpaperChoice6", None],
            "wallpaperChoice7": [self.wallpaperChoice7, 477, 510, 131, 21, "wallpaperChoice7", None],
            "wallpaperChoice8": [self.wallpaperChoice8, 692, 510, 121, 21, "wallpaperChoice8", None]
        }

        #defines all the widget parameters
        for widgetName, widgetSettings in fourthPageWidgets.items():
            widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
        
        #Defines all the custom settings.
        self.wallpapersMenu.setFlat(True)
        self.menuFinish.setFlat(True)
        self.previous3.setFlat(True)
        self.forward4.setFlat(True)
        self.cancel4.setFlat(True)
        
        self.previous3.setIcon(icon2)
        self.previous3.setIconSize(QtCore.QSize(28, 30))
        self.forward4.setIcon(icon1)
        self.forward4.setIconSize(QtCore.QSize(28, 30))
        self.cancel4.setIcon(icon)
        
        self.stackedWidget.addWidget(self.Wallpaper)
        
        #Adds the fifth and final page
        self.Finish = QtGui.QWidget()
        self.Finish.setObjectName(_fromUtf8("Finish"))
        
        createStaticWidgets(self.Finish)
        
        self.header5 = QtGui.QLabel(self.Finish)
        self.wallpapersMenu2 = QtGui.QPushButton(self.Finish)
        self.finishMenu = QtGui.QPushButton(self.Finish)
        self.arrow5 = QtGui.QLabel(self.Finish)
        self.cancel5 = QtGui.QPushButton(self.Finish)
        self.forward5 = QtGui.QPushButton(self.Finish)
        self.previous4 = QtGui.QPushButton(self.Finish)
        self.finishDesc = QtGui.QLabel(self.Finish)
        self.systemSettings = QtGui.QLabel(self.Finish)
        self.systemSettingsPic = QtGui.QLabel(self.Finish)
        self.systemSettingsDesc = QtGui.QLabel(self.Finish)
        self.systemSettingsButton = QtGui.QPushButton(self.Finish)
        self.helpHead = QtGui.QLabel(self.Finish)
        self.helpPic = QtGui.QLabel(self.Finish)
        self.helpDesc = QtGui.QLabel(self.Finish)
        self.helpButton = QtGui.QPushButton(self.Finish)
        
        finalPageWidgets = {
            "header5": [self.header5, 80, 20, 231, 51, "header5", None],
            "wallpapersMenu2": [self.wallpapersMenu2, 20, 90, 111, 41, "wallpapersMenu2", None],
            "arrow5": [self.arrow5, 140, 90, 31, 41, "arrow5", "/usr/share/turbulence/images/manjaro-grey/arrow.png"],
            "finishMenu": [self.finishMenu, 170, 90, 81, 41, "finishMenu", None],
            "cancel5": [self.cancel5, 20, 575, 91, 33, "cancel5", None],
            "forward5": [self.forward5, 750, 575, 91, 33, "forward5", None],
            "previous4": [self.previous4, 640, 575, 101, 33, "previous4", None],
            "finishDesc": [self.finishDesc, 30, 150, 711, 51, "finishDesc", None],
            "systemSettings": [self.systemSettings, 40, 220, 161, 31, "systemSettings", None],
            "systemSettingsPic": [self.systemSettingsPic, 70, 260, 111, 101, "systemSettingsPic", "/usr/share/turbulence/images/manjaro-grey/finish/preferences-system.png"],
            "systemSettingsDesc": [self.systemSettingsDesc, 200, 280, 371, 31, "systemSettingsDesc", None],
            "systemSettingsButton": [self.systemSettingsButton, 300, 310, 181, 31, "systemSettingsButton", None],
            "helpHead": [self.helpHead, 40, 400, 51, 31, "helpHead", None, None],
            "helpPic": [self.helpPic, 70, 440, 111, 101, "helpPic", "/usr/share/turbulence/images/manjaro-grey/finish/help-icon.png"],
            "helpDesc": [self.helpDesc, 200, 440, 371, 51, "helpDesc", None],
            "helpButton": [self.helpButton, 300, 491, 181, 31, "helpButton", None]
        }

        #defines all the widget parameters
        for widgetName, widgetSettings in finalPageWidgets.items():
            widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
        
        #Defines the custom settings
        self.wallpapersMenu2.setFlat(True)
        self.finishMenu.setFlat(True)
        self.cancel5.setFlat(True)
        self.forward5.setFlat(True)
        self.previous4.setFlat(True)
        self.systemSettingsButton.setFlat(True)
        self.helpButton.setFlat(True)
        
        self.cancel5.setIcon(icon)
        
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("/usr/share/turbulence/images/manjaro-grey/checkmark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.forward5.setIcon(icon4)
        self.forward5.setIconSize(QtCore.QSize(16, 18))
        
        self.previous4.setIcon(icon2)
        self.previous4.setIconSize(QtCore.QSize(28, 30))
        
        self.stackedWidget.addWidget(self.Finish)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0) #Sets the index for the stacked widget to 0.

        #sets the current checked boxes and status. It's at the bottom to be out of the way.
        neededDirs = folders.findKeyDir('active')
        neededFolders = {
            "Desktop": [self.folderActive1, self.folderHeader1],
            "Documents": [self.folderActive2, self.folderHeader2],
            "Downloads": [self.folderActive3, self.folderHeader3],
            "Music": [self.folderActive4, self.folderHeader4],
            "Pictures": [self.folderActive5, self.folderHeader5],
            "Public": [self.folderActive6, self.folderHeader6],
            "Templates": [self.folderActive7, self.folderHeader7],
            "Videos": [self.folderActive8, self.folderHeader8]
        }

        for x in neededDirs:
	    for y in neededDirs:
                if folders.getObject(neededDirs, y, 'bool'): 
                    neededname = folders.getObject(neededDirs, y, 'name')
                    for neededName, folderWidgets in neededFolders.items():
                        if neededName == y:
                            folderWidgets[0].setChecked(True)
                            folderWidgets[1].setText(_translate("MainWindow", "Status: Active", None))
                            break
        
        #Handlers for button clicks and whatnot.
        QtCore.QObject.connect(self.folders2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonNext)
        QtCore.QObject.connect(self.forward, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonNext)
        QtCore.QObject.connect(self.cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.themes, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonNext)
        QtCore.QObject.connect(self.previous, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonPrev)
        QtCore.QObject.connect(self.forward2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonNextFolders)
        QtCore.QObject.connect(self.cancel2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.menuWallpapers, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonNextThemes)
        QtCore.QObject.connect(self.previous2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonPrevFolders)
        QtCore.QObject.connect(self.forward3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonNextThemes)
        QtCore.QObject.connect(self.cancel3, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.menuFinish, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonNextWallpapers)
        QtCore.QObject.connect(self.cancel4, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.previous3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonPrev)
        QtCore.QObject.connect(self.forward4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonNextWallpapers)
        QtCore.QObject.connect(self.wallpapersMenu2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonPrev)
        QtCore.QObject.connect(self.systemSettingsButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonSystemSettings)
        QtCore.QObject.connect(self.helpButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonLaunchHelp)
        QtCore.QObject.connect(self.cancel5, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.previous4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonPrev)
        QtCore.QObject.connect(self.forward5, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    #Starts the translation function.
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Turbulence", None))
        self.header.setText(_translate("MainWindow", "Welcome To Manjaro", None))
        self.welcomeButton.setText(_translate("MainWindow", "Welcome", None))
        self.folders2.setText(_translate("MainWindow", "Folders", None))
        self.whatIsManjaro.setText(_translate("MainWindow", "What is Manjaro?", None))
        self.manjaroDesc.setText(_translate("MainWindow", """Hello, and welcome to Manjaro.\n\nManjaro is a sleek and fast distro, featuring benefits from the popular Arch OS, along with ease of use.\nDeveloped in Austria, France, and Germany, Manjaro aims at new users, and experienced users.\n\nSome of Manjaro\'s features are:\n\n     Speed, power, and efficiency\n\n     Access to the very latest cutting and bleeding edge software\n\n     A ‘rolling release’ development model that provides the most up-to-date system possible without\n     the need to install new versions\n\n     Access to the Arch User Repository (AUR).\n\nOver these next few steps, Turbulence will guide you through customizing your new copy of Manjaro.""", None))
        self.cancel.setText(_translate("MainWindow", "Cancel", None))
        self.forward.setText(_translate("MainWindow", "Forward", None))
        self.header2.setText(_translate("MainWindow", "Folders", None))
        self.foldersHead.setText(_translate("MainWindow", "Folders", None))
        self.themes.setText(_translate("MainWindow", "Themes", None))
        self.cancel2.setText(_translate("MainWindow", "Cancel", None))
        self.forward2.setText(_translate("MainWindow", "Forward", None))
        self.previous.setText(_translate("MainWindow", "Previous", None))
        self.folderDesc.setText(_translate("MainWindow", "Here, you can choose which folders you want in your home directory. You have a choice from \nsome of the most commonly used folders.", None))
        self.folderHeaderHead.setText(_translate("MainWindow", "Folders", None))
        self.folderHeader1.setText(_translate("MainWindow", "Status: Deactivated", None))
        self.folderHeader2.setText(_translate("MainWindow", "Status: Deactivated", None))
        self.folderHeader3.setText(_translate("MainWindow", "Status: Deactivated", None))
        self.folderHeader4.setText(_translate("MainWindow", "Status: Deactivated", None))
        self.folderHeader5.setText(_translate("MainWindow", "Status: Deactivated", None))
        self.folderHeader6.setText(_translate("MainWindow", "Status: Deactivated", None))
        self.folderHeader7.setText(_translate("MainWindow", "Status: Deactivated", None))
        self.folderHeader8.setText(_translate("MainWindow", "Status: Deactivated", None))
        self.folderName1.setText(_translate("MainWindow", "Desktop", None))
        self.folderName2.setText(_translate("MainWindow", "Documents", None))
        self.folderName3.setText(_translate("MainWindow", "Downloads", None))
        self.folderName4.setText(_translate("MainWindow", "Music", None))
        self.folderName5.setText(_translate("MainWindow", "Pictures", None))
        self.folderName6.setText(_translate("MainWindow", "Public", None))
        self.folderName7.setText(_translate("MainWindow", "Templates", None))
        self.folderName8.setText(_translate("MainWindow", "Videos", None))
        self.folderActive1.setText(_translate("MainWindow", "Active", None))
        self.folderActive2.setText(_translate("MainWindow", "Active", None))
        self.folderActive3.setText(_translate("MainWindow", "Active", None))
        self.folderActive4.setText(_translate("MainWindow", "Active", None))
        self.folderActive5.setText(_translate("MainWindow", "Active", None))
        self.folderActive6.setText(_translate("MainWindow", "Active", None))
        self.folderActive7.setText(_translate("MainWindow", "Active", None))
        self.folderActive8.setText(_translate("MainWindow", "Active", None))
        self.header3.setText(_translate("MainWindow", "Themes", None))
        self.themesMenu.setText(_translate("MainWindow", "Themes", None))
        self.menuWallpapers.setText(_translate("MainWindow", "Wallpapers", None))
        self.cancel3.setText(_translate("MainWindow", "Cancel", None))
        self.forward3.setText(_translate("MainWindow", "Forward", None))
        self.previous2.setText(_translate("MainWindow", "Previous", None))
        self.folderDesc2.setText(_translate("MainWindow", "Here you can choose what type of theme you want for your window decorations.\n", None))
        self.themesHeader.setText(_translate("MainWindow", "Themes", None))
        self.themeRadio1.setText(_translate("MainWindow", "Ozone", None))
        self.themeRadio2.setText(_translate("MainWindow", "Laptop", None))
        self.themeRadio3.setText(_translate("MainWindow", "Oxygen", None))
        self.themeRadio4.setText(_translate("MainWindow", "Plastik", None))
        self.header4.setText(_translate("MainWindow", "Wallpapers", None))
        self.wallpapersMenu.setText(_translate("MainWindow", "Wallpapers", None))
        self.menuFinish.setText(_translate("MainWindow", "Finish", None))
        self.wallpaperDesc.setText(_translate("MainWindow", "Here you can set which wallpaper you want.", None))
        self.previous3.setText(_translate("MainWindow", "Previous", None))
        self.forward4.setText(_translate("MainWindow", "Forward", None))
        self.cancel4.setText(_translate("MainWindow", "Cancel", None))
        self.wallpaperHeader.setText(_translate("MainWindow", "Wallpapers", None))
        self.wallpaperChoice1.setText(_translate("MainWindow", "Ozone", None))
        self.wallpaperChoice2.setText(_translate("MainWindow", "Orange Splash", None))
        self.wallpaperChoice3.setText(_translate("MainWindow", "Sunset Plane", None))
        self.wallpaperChoice4.setText(_translate("MainWindow", "Mountain Lake", None))
        self.wallpaperChoice5.setText(_translate("MainWindow", "Space", None))
        self.wallpaperChoice6.setText(_translate("MainWindow", "Dark Stairs", None))
        self.wallpaperChoice7.setText(_translate("MainWindow", "Cherry Japan", None))
        self.wallpaperChoice8.setText(_translate("MainWindow", "White Tiger", None))
        self.header5.setText(_translate("MainWindow", "Congratulations!", None))
        self.wallpapersMenu2.setText(_translate("MainWindow", "Wallpapers", None))
        self.finishMenu.setText(_translate("MainWindow", "Finish", None))
        self.cancel5.setText(_translate("MainWindow", "Cancel", None))
        self.forward5.setText(_translate("MainWindow", "Finish", None))
        self.previous4.setText(_translate("MainWindow", "Previous", None))
        self.finishDesc.setText(_translate("MainWindow", "All of your settings have been applied. Now, you can start enjoying Manjaro, or look at some of the programs \nand links below. Also, if you haven\'t already, make sure to join the Manjaro community as well!", None))
        self.systemSettings.setText(_translate("MainWindow", "System Settings", None))
        self.systemSettingsDesc.setText(_translate("MainWindow", "Control panel to edit various aspects of the KDE desktop, \nand more.", None))
        self.systemSettingsButton.setText(_translate("MainWindow", "Launch System Settings", None))
        self.helpHead.setText(_translate("MainWindow", "Help", None))
        self.helpDesc.setText(_translate("MainWindow", "For help and support, you can visit Manjaro.org for access \nto a terrific forum, wiki, and IRC!", None))
        self.helpButton.setText(_translate("MainWindow", "Launch Manjaro.org", None))
        
    #Functions to be used in the slots.
    #Moves to next page in the stacked widget.
    def handleButtonNext(self):
        index = self.stackedWidget.currentIndex() + 1
        if index < self.stackedWidget.count():
            self.stackedWidget.setCurrentIndex(index)
            logger.writeLog('proceedToFolders')
            
    #Moved to the next page, but also applies to settings for folders.
    def handleButtonNextFolders(self):
        checkboxDirectoryPairs = {
            "Desktop": self.folderActive1,
            "Documents": self.folderActive2,
            "Downloads":self.folderActive3,
            "Music": self.folderActive4,
            "Pictures": self.folderActive5,
            "Public": self.folderActive6,
            "Templates": self.folderActive7,
            "Videos": self.folderActive8
        }

        for directoryPoint, checkbox in checkboxDirectoryPairs.items():
            if checkbox.isChecked():
                folders.createDir(directoryPoint)
                logger.writeLog('folderChosen', directoryPoint)
            else:
                folders.deleteDir(directoryPoint)
                logger.writeLog('folderNotChosen', directoryPoint)
            
        index = self.stackedWidget.currentIndex() + 1
        if index < self.stackedWidget.count():
            self.stackedWidget.setCurrentIndex(index)
            logger.writeLog('proceedToThemes')

    #Moves next a page, but also applies to settings for themes.
    def handleButtonNextThemes(self):
        kwinThemes = {
            "ozone": self.themeRadio1,
            "laptop": self.themeRadio2,
            "oxygen": self.themeRadio3,
            "plastik": self.themeRadio4,
        }
            
        for themeName, themeRadio in kwinThemes.items():
            if themeRadio.isChecked():
                themes.kwinThemer(themeName)
                plasma_control.startKwin()

        index = self.stackedWidget.currentIndex() + 1
        if index < self.stackedWidget.count():
            self.stackedWidget.setCurrentIndex(index)
            logger.writeLog('proceedToWallpapers')
    
    #Moves next a page, but also applies the wallpaper settings.
    def handleButtonNextWallpapers(self):
        wallpapersDict = {
            "ozoneTurbulence": self.wallpaperChoice1,
            "orangeSplash": self.wallpaperChoice2,
            "sunsetPlane": self.wallpaperChoice3,
            "mountainLake": self.wallpaperChoice4,
            "earthInSpace": self.wallpaperChoice5,
            "darkStairs": self.wallpaperChoice6,
            "cherryJapan": self.wallpaperChoice7,
            "whiteTiger": self.wallpaperChoice8
        }
        
        for wallpaperName, wallpaperRadio in wallpapersDict.items():
            if wallpaperRadio.isChecked():
                wallpapers.changeWallpaperPlus(wallpaperName)
                
        index = self.stackedWidget.currentIndex() + 1
        if index < self.stackedWidget.count():
            self.stackedWidget.setCurrentIndex(index)
            logger.writeLog('proceedToFinal')

    #Moves back from the themes to folders, and reloads the settings for folders.
    def handleButtonPrevFolders(self):
        checkboxDirectoryPairs = {
            "Desktop": [self.folderActive1, self.folderHeader1],
            "Documents": [self.folderActive2, self.folderHeader2],
            "Downloads": [self.folderActive3, self.folderHeader3],
            "Music": [self.folderActive4, self.folderHeader4],
            "Pictures": [self.folderActive5, self.folderHeader5],
            "Public": [self.folderActive6, self.folderHeader6],
            "Templates": [self.folderActive7, self.folderHeader7],
            "Videos": [self.folderActive8, self.folderHeader8]
        }

        for directoryPoint, folderWidgets in checkboxDirectoryPairs.items():
            if folderWidgets[0].isChecked():
                folderWidgets[1].setText(_translate("MainWindow", "Status: Active", None))
            else:
                folderWidgets[1].setText(_translate("MainWindow", "Status: Deactivated", None))
                
        index = self.stackedWidget.currentIndex() - 1
        if index >= 0:
            self.stackedWidget.setCurrentIndex(index)
            
    def handleButtonSystemSettings(self):
        final.launchSystemSettings()
        
    def handleButtonLaunchHelp(self):
        final.launchHelp()

    #Just moves back a page..
    def handleButtonPrev(self):
        index = self.stackedWidget.currentIndex() - 1
        if index >= 0:
            self.stackedWidget.setCurrentIndex(index)