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

#Detect what processes you're running for DE/WM specific processess.

tintStatus = utils_detector.detectTint() #Tint
kwinStatus = utils_detector.detectKwin() #Kwin
plasmaStatus = utils_detector.detectPlasma() #Plasma
nitrogenStatus = utils_detector.detectNitrogen() #Nitrogen


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
class Ui_MainWindow(QtCore.QObject):
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
        
        forwardIcon = QtGui.QIcon()
        forwardIcon.addPixmap(QtGui.QPixmap(_fromUtf8("/usr/share/turbulence/images/manjaro-grey/arrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        cancelIcon = QtGui.QIcon()
        cancelIcon.addPixmap(QtGui.QPixmap(_fromUtf8("/usr/share/turbulence/images/manjaro-grey/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        previousIcon = QtGui.QIcon()
        previousIcon.addPixmap(QtGui.QPixmap(_fromUtf8("/usr/share/turbulence/images/manjaro-grey/arrowreverse.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        finishIcon = QtGui.QIcon()
        finishIcon.addPixmap(QtGui.QPixmap(_fromUtf8("/usr/share/turbulence/images/manjaro-grey/checkmark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        #Defines the stacked widget
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        widgetConfigurer(self.stackedWidget, -10, -20, 861, 621, "stackedWidget", None, None)
        
        #Starts the first page in the stacked widget, or Manjaro welcome
        self.welcomeToManjaro = QtGui.QWidget()
        self.welcomeToManjaro.setObjectName(_fromUtf8("welcomeToManjaro"))

        #Defines all the widgets for the first page
        createStaticWidgets(self.welcomeToManjaro)
        self.welcomeHeader = QtGui.QLabel(self.welcomeToManjaro)
        self.welcomeButton = QtGui.QPushButton(self.welcomeToManjaro)
        self.welcomeArrow = QtGui.QLabel(self.welcomeToManjaro)
        self.welcomeFolders = QtGui.QPushButton(self.welcomeToManjaro)
        self.welcomeWhatIsManjaro = QtGui.QLabel(self.welcomeToManjaro)
        self.welcomeManjaroDesc = QtGui.QLabel(self.welcomeToManjaro)
        self.welcomeBullet1 = QtGui.QLabel(self.welcomeToManjaro)
        self.welcomeBullet2 = QtGui.QLabel(self.welcomeToManjaro)
        self.welcomeBullet3 = QtGui.QLabel(self.welcomeToManjaro)
        self.welcomeBullet4 = QtGui.QLabel(self.welcomeToManjaro)
        self.welcomeForward = QtGui.QPushButton(self.welcomeToManjaro)
        self.welcomeCancel = QtGui.QPushButton(self.welcomeToManjaro)
        
        #widget dictionary
        firstPageWidgets = {
            "welcomeHeader": [self.welcomeHeader, 80, 20, 361, 51, "welcomeHeader", None],
            "welcomeButton": [self.welcomeButton, 20, 90, 111, 41, "welcomeButton", None],
            "welcomeArrow": [self.welcomeArrow, 140, 90, 111, 41, "welcomeArrow", "/usr/share/turbulence/images/manjaro-grey/arrow.png"],
            "welcomeFolders": [self.welcomeFolders, 170, 90, 81, 41, "welcomeFolders", None],
            "welcomeWhatIsManjaro": [self.welcomeWhatIsManjaro, 30, 180, 480, 71, "welcomeWhatIsManjaro", None],
            "welcomeManjaroDesc": [self.welcomeManjaroDesc, 70, 260, 760, 261, "welcomeManjaroDesc", None],
            "welcomeBullet1": [self.welcomeBullet1, 70, 365, 21, 21, "welcomeBullet1", "/usr/share/turbulence/images/manjaro-grey/bullet.png"],
            "welcomeBullet2": [self.welcomeBullet2, 70, 395, 21, 21, "welcomeBullet2", "/usr/share/turbulence/images/manjaro-grey/bullet.png"],
            "welcomeBullet3": [self.welcomeBullet3, 70, 425, 21, 21, "welcomeBullet3", "/usr/share/turbulence/images/manjaro-grey/bullet.png"],
            "welcomeBullet4": [self.welcomeBullet4, 70, 470, 21, 21, "welcomeBullet4", "/usr/share/turbulence/images/manjaro-grey/bullet.png"],
            "welcomeForward": [self.welcomeForward, 730, 575, 111, 33, "welcomeForward", None],
            "welcomeCancel": [self. welcomeCancel, 20, 575, 110, 33, "welcomeCancel", None],
        }
        
        #defines all the widget parameters
        for widgetName, widgetSettings in firstPageWidgets.items():
            widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
        
        #defines all the custom settings
        self.welcomeButton.setFlat(True)
        self.welcomeFolders.setFlat(True)
        self.welcomeForward.setFlat(True)
        self.welcomeCancel.setFlat(True)
        
        self.welcomeForward.setIcon(forwardIcon)
        self.welcomeForward.setIconSize(QtCore.QSize(28, 30))
        self.welcomeCancel.setIcon(cancelIcon)
        
        #adds the first page
        self.stackedWidget.addWidget(self.welcomeToManjaro)
        
        #Hooks up the button handlers
        QtCore.QObject.connect(self.welcomeFolders, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonNext)
        QtCore.QObject.connect(self.welcomeForward, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonNext)
        QtCore.QObject.connect(self.welcomeCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        
        #Translates, or sets the text to the widgets
        self.welcomeHeader.setText(_translate("MainWindow", "Welcome To Manjaro", None))
        self.welcomeButton.setText("Welcome")
        self.welcomeFolders.setText("Folders")
        self.welcomeWhatIsManjaro.setText(_translate("MainWindow", "What is Manjaro?", None))
        self.welcomeManjaroDesc.setText(_translate("MainWindow", """Hello, and welcome to Manjaro.\n\nManjaro is a sleek and fast distro, featuring benefits from the popular Arch OS, along with ease of use.\nDeveloped in Austria, France, and Germany, Manjaro aims at new users, and experienced users.\n\nSome of Manjaro\'s features are:\n\n     Speed, power, and efficiency\n\n     Access to the very latest cutting and bleeding edge software\n\n     A ‘rolling release’ development model that provides the most up-to-date system possible without\n     the need to install new versions\n\n     Access to the Arch User Repository (AUR).\n\nOver these next few steps, Turbulence will guide you through customizing your new copy of Manjaro.""", None))
        self.welcomeCancel.setText(_translate("MainWindow", "Cancel", None))
        self.welcomeForward.setText(_translate("MainWindow", "Forward", None))
        
        
        #Starts the second page in the stacked widget.
        self.folders = QtGui.QWidget()
        self.folders.setObjectName(_fromUtf8("folders"))
        
        #Defines all the widget for the second page
        createStaticWidgets(self.folders)
        
        self.folderHeader = QtGui.QLabel(self.folders)
        self.folderMenu = QtGui.QPushButton(self.folders)
        self.folderArrow = QtGui.QLabel(self.folders)
        self.folderThemes = QtGui.QPushButton(self.folders)
        self.folderCancel = QtGui.QPushButton(self.folders)
        self.folderForward = QtGui.QPushButton(self.folders)
        self.folderPrevious = QtGui.QPushButton(self.folders)
        self.folderIcon = QtGui.QLabel(self.folders)
        self.folderDesc = QtGui.QLabel(self.folders)
        self.folderSubHeader = QtGui.QLabel(self.folders)
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
        
        #widget dictionary.
        secondPageWidgets = {
            "folderHeader": [self.folderHeader, 80, 20, 111, 51, "folderHeader", None],
            "folderMenu": [self.folderMenu, 20, 90, 91, 41, "folderMenu", None],
            "folderArrow": [self.folderArrow, 120, 90, 31, 41, "folderArrow", "/usr/share/turbulence/images/manjaro-grey/arrow.png"],
            "folderThemes": [self.folderThemes, 150, 90, 91, 41, "folderThemes", None],
            "folderCancel": [self.folderCancel, 20, 575, 110, 33, "folderCancel", None],
            "folderForward": [self.folderForward, 730, 575, 111, 33, "folderForward", None],
            "folderPrevious": [self.folderPrevious, 620, 575, 101, 33, "folderPrevious", None],
            "folderIcon": [self.folderIcon, 40, 150, 61, 61, "folderIcon", "/usr/share/turbulence/images/manjaro-grey/foldericons/folder.png"],
            "folderDesc": [self.folderDesc, 110, 170, 591, 31, "folderDesc", None],
            "folderSubHeader": [self.folderSubHeader, 50, 240, 81, 31, "foldeSubHeader", None],
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
            "folderActive1": [self.folderActive1, 50, 390, 100, 21, "folderActive1", None],
            "folderActive2": [self.folderActive2, 260, 390, 100, 21, "folderActive2", None],
            "folderActive3": [self.folderActive3, 470, 390, 100, 21, "folderActive3", None],
            "folderActive4": [self.folderActive4, 680, 390, 100, 21, "folderActive4", None],
            "folderActive5": [self.folderActive5, 50, 540, 100, 21, "folderActive5", None],
            "folderActive6": [self.folderActive6, 260, 540, 100, 21, "folderActive6", None],
            "folderActive7": [self.folderActive7, 470, 540, 100, 21, "folderActive7", None],
            "folderActive8": [self.folderActive8, 680, 540, 100, 21, "folderActive8", None]
        }
        
        #defines all the widget parameters
        for widgetName, widgetSettings in secondPageWidgets.items():
            widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
        
        #defines the custom settings
        self.folderMenu.setFlat(True)
        self.folderThemes.setFlat(True)
        self.folderCancel.setFlat(True)
        self.folderForward.setFlat(True)
        self.folderPrevious.setFlat(True)
        
        self.folderPrevious.setIcon(previousIcon)
        self.folderCancel.setIcon(cancelIcon)
        self.folderForward.setIcon(forwardIcon)
        self.folderForward.setIconSize(QtCore.QSize(28, 30))
        self.folderPrevious.setIconSize(QtCore.QSize(28, 30))
        
        #adds the second page
        self.stackedWidget.addWidget(self.folders)
        
        #Handles the button clicks.
        QtCore.QObject.connect(self.folderThemes, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonNext)
        QtCore.QObject.connect(self.folderPrevious, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonPrev)
        QtCore.QObject.connect(self.folderForward, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonNextFolders)
        QtCore.QObject.connect(self.folderCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        
        #Translates, or sets the text for all the widgets
        self.folderHeader.setText(_translate("MainWindow", "Folders", None))
        self.folderMenu.setText("Folders")
        self.folderThemes.setText("Themes")
        self.folderCancel.setText(_translate("MainWindow", "Cancel", None))
        self.folderForward.setText(_translate("MainWindow", "Forward", None))
        self.folderPrevious.setText(_translate("MainWindow", "Previous", None))
        self.folderDesc.setText(_translate("MainWindow", "Here, you can choose which folders you want in your home directory. You have a choice from \nsome of the most commonly used folders.", None))
        self.folderSubHeader.setText("Folders")
        self.folderHeader1.setText(_translate("MainWindow", "Status: Deactivated", None))
        self.folderHeader2.setText(_translate("MainWindow", "Status: Deactivated", None))
        self.folderHeader3.setText(_translate("MainWindow", "Status: Deactivated", None))
        self.folderHeader4.setText(_translate("MainWindow", "Status: Deactivated", None))
        self.folderHeader5.setText(_translate("MainWindow", "Status: Deactivated", None))
        self.folderHeader6.setText(_translate("MainWindow", "Status: Deactivated", None))
        self.folderHeader7.setText(_translate("MainWindow", "Status: Deactivated", None))
        self.folderHeader8.setText(_translate("MainWindow", "Status: Deactivated", None))
        self.folderName1.setText("Desktop")
        self.folderName2.setText("Documents")
        self.folderName3.setText("Downloads")
        self.folderName4.setText("Music")
        self.folderName5.setText("Pictures")
        self.folderName6.setText("Public")
        self.folderName7.setText("Templates")
        self.folderName8.setText("Videos")
        self.folderActive1.setText(_translate("MainWindow", "Active", None))
        self.folderActive2.setText(_translate("MainWindow", "Active", None))
        self.folderActive3.setText(_translate("MainWindow", "Active", None))
        self.folderActive4.setText(_translate("MainWindow", "Active", None))
        self.folderActive5.setText(_translate("MainWindow", "Active", None))
        self.folderActive6.setText(_translate("MainWindow", "Active", None))
        self.folderActive7.setText(_translate("MainWindow", "Active", None))
        self.folderActive8.setText(_translate("MainWindow", "Active", None))
        
        
        #Checks if Kwin is running, and if so displays the kwin themer
        if kwinStatus:
            self.Theme = QtGui.QWidget()
            self.Theme.setObjectName(_fromUtf8("Theme"))
        
            createStaticWidgets(self.Theme)
            self.themeHeader = QtGui.QLabel(self.Theme)
            self.themeMenu = QtGui.QPushButton(self.Theme)
            self.themeArrow = QtGui.QLabel(self.Theme)
            self.themeMenuWallpapers = QtGui.QPushButton(self.Theme)
            self.themeCancel = QtGui.QPushButton(self.Theme)
            self.themeForward = QtGui.QPushButton(self.Theme)
            self.themePrevious = QtGui.QPushButton(self.Theme)
            self.themeIcon = QtGui.QLabel(self.Theme)
            self.themeDesc = QtGui.QLabel(self.Theme)
            self.themeHeaderHead = QtGui.QLabel(self.Theme)
            self.themePreview1 = QtGui.QLabel(self.Theme)
            self.themePreview2 = QtGui.QLabel(self.Theme)
            self.themePreview3 = QtGui.QLabel(self.Theme)
            self.themePreview4 = QtGui.QLabel(self.Theme)
            self.themeRadio1 = QtGui.QRadioButton(self.Theme)
            self.themeRadio2 = QtGui.QRadioButton(self.Theme)
            self.themeRadio3 = QtGui.QRadioButton(self.Theme)
            self.themeRadio4 = QtGui.QRadioButton(self.Theme)
        
            thirdPageWidgets = {
                "themeHeader": [self.themeHeader, 80, 20, 111, 51, "themeHeader", None],
                "themeMenu": [self.themeMenu, 20, 90, 91, 41, "themeMenu", None],
                "themeArrow": [self.themeArrow, 120, 90, 31, 41, "themeArrow", "/usr/share/turbulence/images/manjaro-grey/arrow.png"],
                "themeMenuWallpapers": [self.themeMenuWallpapers, 150, 90, 111, 41, "themeMenuWallpapers", None],
                "themeCancel": [self.themeCancel, 20, 575, 110, 33, "themeCancel", None],
                "themeForward": [self.themeForward, 730, 575, 111, 33, "themeForward", None],
                "themePrevious": [self.themePrevious, 620, 575, 101, 33, "themePrevious", None],
                "themeIcon": [self.themeIcon, 40, 160, 61, 61, "themeIcon", "/usr/share/turbulence/images/manjaro-grey/themes/theme.png"],
                "themeDesc": [self.themeDesc, 110, 167, 591, 51, "themeDesc", None],
                "themeHeaderHead": [self.themeHeaderHead, 50, 240, 91, 31, "themeHeaderHead", None],
                "themePreview1": [self.themePreview1, 90, 280, 241, 81, "themePreview1", "/usr/share/turbulence/images/manjaro-grey/themes/ozone.png"],
                "themePreview2": [self.themePreview2, 510, 280, 241, 81, "themePreview2", "/usr/share/turbulence/images/manjaro-grey/themes/cupertino-ish.png"],
                "themePreview3": [self.themePreview3, 90, 410, 241, 81, "themePreview3", "/usr/share/turbulence/images/manjaro-grey/themes/oxygen.png"],
                "themePreview4": [self.themePreview4, 510, 410, 241, 81, "themePreview4", "/usr/share/turbulence/images/manjaro-grey/themes/plastik.png"],
                "themeRadio1": [self.themeRadio1, 170, 370, 81, 21, "themeRadio1", None],
                "themeRadio2": [self.themeRadio2, 566, 370, 131, 21, "themeRadio2", None],
                "themeRadio3": [self.themeRadio3, 167, 500, 91, 21, "themeRadio3", None],
                "themeRadio4": [self.themeRadio4, 591, 510, 91, 21, "themeRadio4", None]
             }
        
            #defines all the widget parameters
            for widgetName, widgetSettings in thirdPageWidgets.items():
                widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
        
            #Defines the custom settings
            self.themeMenu.setFlat(True)
            self.themeMenuWallpapers.setFlat(True)
            self.themeCancel.setFlat(True)
            self.themeForward.setFlat(True)
            self.themePrevious.setFlat(True)
        
            self.themeCancel.setIcon(cancelIcon)
            self.themeForward.setIcon(forwardIcon)
            self.themePrevious.setIcon(previousIcon)
            self.themeForward.setIconSize(QtCore.QSize(28, 30))
            self.themePrevious.setIconSize(QtCore.QSize(28, 30))
        
            #Adds the third page
            self.stackedWidget.addWidget(self.Theme)
            
            #Hooks up the button handlers
            QtCore.QObject.connect(self.themeMenuWallpapers, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonNextThemes)
            QtCore.QObject.connect(self.themeCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
            QtCore.QObject.connect(self.themeForward, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonNextThemes)
            QtCore.QObject.connect(self.themePrevious, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonPrevFolders)
            
            #Translates the text
            self.themeHeader.setText("Themes")
            self.themeMenu.setText("Themes")
            self.themeMenuWallpapers.setText("Wallpapers")
            self.themeCancel.setText(_translate("MainWindow", "Cancel", None))
            self.themeForward.setText(_translate("MainWindow", "Forward", None))
            self.themePrevious.setText(_translate("MainWindow", "Previous", None))
            self.themeDesc.setText(_translate("MainWindow", "Here you can choose what type of theme you want for your window decorations.\n", None))
            self.themeHeaderHead.setText("Themes")
            self.themeRadio1.setText("Ozone")
            self.themeRadio2.setText("Cuptertino-ish")
            self.themeRadio3.setText("Oxygen")
            self.themeRadio4.setText("Plastik")
        
        
        #Starts code for fourth page
        if plasmaStatus:
            self.Wallpaper = QtGui.QWidget()
            self.Wallpaper.setObjectName(_fromUtf8("Wallpaper"))
        
            #defines all the widgets
            createStaticWidgets(self.Wallpaper)
        
            self.wallpaperHeader = QtGui.QLabel(self.Wallpaper)
            self.wallpaperMenu = QtGui.QPushButton(self.Wallpaper)
            self.wallpaperArrow = QtGui.QLabel(self.Wallpaper)
            self.wallpaperMenuFinish = QtGui.QPushButton(self.Wallpaper)
            self.wallpaperIcon = QtGui.QLabel(self.Wallpaper)
            self.wallpaperDesc = QtGui.QLabel(self.Wallpaper)
            self.wallpaperPrevious = QtGui.QPushButton(self.Wallpaper)
            self.wallpaperForward = QtGui.QPushButton(self.Wallpaper)
            self.wallpaperCancel = QtGui.QPushButton(self.Wallpaper)
            self.wallpaperHeaderHead = QtGui.QLabel(self.Wallpaper)
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
                "wallpaperHeader": [self.wallpaperHeader, 80, 20, 161, 51, "wallpaperHeader", None],
                "wallpaperMenu": [self.wallpaperMenu, 20, 90, 121, 41, "wallpaperMenu", None],
                "wallpaperArrow": [self.wallpaperArrow, 150, 90, 31, 41, "wallpaperArrow", "/usr/share/turbulence/images/manjaro-grey/arrow.png"],
                "wallpaperMenuFinish": [self.wallpaperMenuFinish, 180, 90, 71, 41, "wallpaperMenuFinish", None],
                "wallpaperIcon": [self.wallpaperIcon, 40, 160, 61, 61, "wallpaperIcon", "/usr/share/turbulence/images/manjaro-grey/wallpapers/wallpapers.png"],
                "wallpaperDesc": [self.wallpaperDesc, 110, 160, 591, 51, "wallpaperDesc", None],
                "wallpaperPrevious": [self.wallpaperPrevious, 620, 575, 101, 33, "wallpaperPrevious", None],
                "wallpaperForward": [self.wallpaperForward, 730, 575, 111, 33, "wallpaperForward", None],
                "wallpaperCancel": [self.wallpaperCancel, 20, 575, 110, 33, "wallpaperCancel", None],
                "wallpaperHeaderHead": [self.wallpaperHeaderHead, 50, 240, 121, 31, "wallpaperHeaderHead", None],
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
            self.wallpaperMenu.setFlat(True)
            self.wallpaperMenuFinish.setFlat(True)
            self.wallpaperPrevious.setFlat(True)
            self.wallpaperForward.setFlat(True)
            self.wallpaperCancel.setFlat(True)
        
            self.wallpaperPrevious.setIcon(previousIcon)
            self.wallpaperForward.setIcon(forwardIcon)
            self.wallpaperCancel.setIcon(cancelIcon)
            self.wallpaperPrevious.setIconSize(QtCore.QSize(28, 30))
            self.wallpaperForward.setIconSize(QtCore.QSize(28, 30))
        
            self.stackedWidget.addWidget(self.Wallpaper)
            
            #Handles the button clicks
            QtCore.QObject.connect(self.wallpaperMenuFinish, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonNextWallpapers)
            QtCore.QObject.connect(self.wallpaperCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
            QtCore.QObject.connect(self.wallpaperPrevious, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonPrev)
            QtCore.QObject.connect(self.wallpaperForward, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonNextWallpapers)
        
            #Sets text, or translates widgets
            self.wallpaperHeader.setText("Wallpapers")
            self.wallpaperMenu.setText("Wallpapers")
            self.wallpaperMenuFinish.setText("Finish")
            self.wallpaperDesc.setText(_translate("MainWindow", "Here you can set which wallpaper you want.", None))
            self.wallpaperPrevious.setText(_translate("MainWindow", "Previous", None))
            self.wallpaperForward.setText(_translate("MainWindow", "Forward", None))
            self.wallpaperCancel.setText(_translate("MainWindow", "Cancel", None))
            self.wallpaperHeaderHead.setText("Wallpapers")
            self.wallpaperChoice1.setText("Ozone")
            self.wallpaperChoice2.setText("Orange Splash")
            self.wallpaperChoice3.setText("Sunset Plane")
            self.wallpaperChoice4.setText("Mountain Lake")
            self.wallpaperChoice5.setText("Space")
            self.wallpaperChoice6.setText("Dark Stairs")
            self.wallpaperChoice7.setText("Cherry Japan")
            self.wallpaperChoice8.setText("White Tiger")
        
        
        #Adds the fifth and final page
        self.Finish = QtGui.QWidget()
        self.Finish.setObjectName(_fromUtf8("Finish"))
        
        createStaticWidgets(self.Finish)
        
        self.finishHeader = QtGui.QLabel(self.Finish)
        self.finishWallpaperMenu = QtGui.QPushButton(self.Finish)
        self.finishMenu = QtGui.QPushButton(self.Finish)
        self.finishArrow = QtGui.QLabel(self.Finish)
        self.finishCancel = QtGui.QPushButton(self.Finish)
        self.finishForward = QtGui.QPushButton(self.Finish)
        self.finishPrevious = QtGui.QPushButton(self.Finish)
        self.finishDesc = QtGui.QLabel(self.Finish)
        self.finishSystemSettings = QtGui.QLabel(self.Finish)
        self.finishSystemSettingsPic = QtGui.QLabel(self.Finish)
        self.finishSystemSettingsDesc = QtGui.QLabel(self.Finish)
        self.finishSystemSettingsButton = QtGui.QPushButton(self.Finish)
        self.finishHelpHead = QtGui.QLabel(self.Finish)
        self.finishHelpPic = QtGui.QLabel(self.Finish)
        self.finishHelpDesc = QtGui.QLabel(self.Finish)
        self.finishHelpButton = QtGui.QPushButton(self.Finish)
        
        finalPageWidgets = {
            "finishHeader": [self.finishHeader, 80, 20, 231, 51, "finishHeader", None],
            "finishWallpaperMenu": [self.finishWallpaperMenu, 20, 90, 111, 41, "finishWallpaperMenu", None],
            "finishArrow": [self.finishArrow, 140, 90, 31, 41, "finishArrow", "/usr/share/turbulence/images/manjaro-grey/arrow.png"],
            "finishMenu": [self.finishMenu, 170, 90, 81, 41, "finishMenu", None],
            "finishCancel": [self.finishCancel, 20, 575, 110, 33, "finishCancel", None],
            "finishForward": [self.finishForward, 750, 575, 91, 33, "finishForward", None],
            "finishPrevious": [self.finishPrevious, 640, 575, 101, 33, "finishPrevious", None],
            "finishDesc": [self.finishDesc, 30, 150, 781, 51, "finishDesc", None],
            "finishSystemSettings": [self.finishSystemSettings, 40, 220, 250, 31, "finishSystemSettings", None],
            "finishSystemSettingsPic": [self.finishSystemSettingsPic, 70, 260, 111, 101, "finishSystemSettingsPic", "/usr/share/turbulence/images/manjaro-grey/finish/preferences-system.png"],
            "finishSystemSettingsDesc": [self.finishSystemSettingsDesc, 200, 280, 371, 31, "finishSystemSettingsDesc", None],
            "finishSystemSettingsButton": [self.finishSystemSettingsButton, 300, 310, 181, 41, "finishSystemSettingsButton", None],
            "finishHelpHead": [self.finishHelpHead, 40, 400, 71, 31, "finishHelpHead", None, None],
            "finishHelpPic": [self.finishHelpPic, 70, 440, 111, 101, "finishHelpPic", "/usr/share/turbulence/images/manjaro-grey/finish/help-icon.png"],
            "finishHelpDesc": [self.finishHelpDesc, 200, 440, 381, 51, "finishHelpDesc", None],
            "finishHelpButton": [self.finishHelpButton, 300, 491, 181, 41, "finishHelpButton", None]
        }

        #defines all the widget parameters
        for widgetName, widgetSettings in finalPageWidgets.items():
            widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
        
        #Defines the custom settings
        self.finishWallpaperMenu.setFlat(True)
        self.finishMenu.setFlat(True)
        self.finishCancel.setFlat(True)
        self.finishForward.setFlat(True)
        self.finishPrevious.setFlat(True)
        self.finishSystemSettingsButton.setFlat(True)
        self.finishHelpButton.setFlat(True)
        
        self.finishCancel.setIcon(cancelIcon)
        self.finishForward.setIcon(finishIcon)
        self.finishPrevious.setIcon(previousIcon)
        self.finishForward.setIconSize(QtCore.QSize(16, 18))
        self.finishPrevious.setIconSize(QtCore.QSize(28, 30))
        
        self.stackedWidget.addWidget(self.Finish)
        
        #Handles the button click
        QtCore.QObject.connect(self.finishWallpaperMenu, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonPrev)
        QtCore.QObject.connect(self.finishSystemSettingsButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonSystemSettings)
        QtCore.QObject.connect(self.finishHelpButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonLaunchHelp)
        QtCore.QObject.connect(self.finishCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.finishPrevious, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonPrev)
        QtCore.QObject.connect(self.finishForward, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        
        #Translates the widgets, or sets text
        self.finishHeader.setText(_translate("MainWindow", "Congratulations!", None))
        self.finishWallpaperMenu.setText("Wallpapers")
        self.finishMenu.setText("Finish")
        self.finishCancel.setText(_translate("MainWindow", "Cancel", None))
        self.finishForward.setText("Finish")
        self.finishPrevious.setText(_translate("MainWindow", "Previous", None))
        self.finishDesc.setText(_translate("MainWindow", "All of your settings have been applied. Now, you can start enjoying Manjaro, or look at some of the programs \nand links below. Also, if you haven\'t already, make sure to join the Manjaro community as well!", None))
        self.finishSystemSettings.setText(_translate("MainWindow", "System Settings", None))
        self.finishSystemSettingsDesc.setText(_translate("MainWindow", "Control panel to edit various aspects of the KDE desktop, \nand more.", None))
        self.finishSystemSettingsButton.setText(_translate("MainWindow", "Launch System Settings", None))
        self.finishHelpHead.setText(_translate("MainWindow", "Help", None))
        self.finishHelpDesc.setText(_translate("MainWindow", "For help and support, you can visit Manjaro.org for access \nto a terrific forum, wiki, and IRC!", None))
        self.finishHelpButton.setText(_translate("MainWindow", "Launch Manjaro.org", None))
        
        
        #Configures the window a bit more.
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("Turbulence")
        self.stackedWidget.setCurrentIndex(0) #Sets the index for the stacked widget to 0.
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #sets the current checked boxes and status. It's at the bottom to be out of the way.
        neededDirs = folders.findKeyDir('active')
        neededFolders = {
            "DESKTOP": [self.folderActive1, self.folderHeader1],
            "DOCUMENTS": [self.folderActive2, self.folderHeader2],
            "DOWNLOAD": [self.folderActive3, self.folderHeader3],
            "MUSIC": [self.folderActive4, self.folderHeader4],
            "PICTURES": [self.folderActive5, self.folderHeader5],
            "PUBLICSHARE": [self.folderActive6, self.folderHeader6],
            "TEMPLATES": [self.folderActive7, self.folderHeader7],
            "VIDEOS": [self.folderActive8, self.folderHeader8]
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
        
        
    #Moves to next page in the stacked widget.
    def handleButtonNext(self):
        index = self.stackedWidget.currentIndex() + 1
        if index < self.stackedWidget.count():
            self.stackedWidget.setCurrentIndex(index)
            logger.writeLog('proceedToFolders')
            
            
    #Moved to the next page, but also applies to settings for folders.
    def handleButtonNextFolders(self):
        checkboxDirectoryPairs = {
            self.folderActive1: ["Desktop", "XDG_DESKTOP_DIR"],
            self.folderActive2: ["Documents", "XDG_DOCUMENTS_DIR"],
            self.folderActive3: ["Downloads", "XDG_DOWNLOAD_DIR"],
            self.folderActive4: ["Music", "XDG_MUSIC_DIR"],
            self.folderActive5: ["Pictures", "XDG_PICTURES_DIR"],
            self.folderActive6: ["Public", "XDG_PUBLICSHARE_DIR"],
            self.folderActive7: ["Templates", "XDG_TEMPLATES_DIR"],
            self.folderActive8: ["Videos", "XDG_VIDEOS_DIR"]
        }

        for checkbox, directoryPoint in checkboxDirectoryPairs.items():
            if checkbox.isChecked():
                folders.createDir(directoryPoint[0], directoryPoint[1])
                logger.writeLog('folderChosen', directoryPoint[0])
            else:
                folders.deleteDir(directoryPoint[1])
                logger.writeLog('folderNotChosen', directoryPoint[1])
            
        index = self.stackedWidget.currentIndex() + 1
        if index < self.stackedWidget.count():
            self.stackedWidget.setCurrentIndex(index)
            logger.writeLog('proceedToThemes')

    #Moves next a page, but also applies to settings for themes.
    def handleButtonNextThemes(self):
        kwinThemes = {
            "ozone": self.themeRadio1,
            "cupertino-ish": self.themeRadio2,
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