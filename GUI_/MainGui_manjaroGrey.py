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

#Detect what processes you're running for DE/WM specific slides.
tintStatus = utils_detector.detectTint() #Tint
kwinStatus = utils_detector.detectKwin() #Kwin
plasmaStatus = utils_detector.detectPlasma() #Plasma
nitrogenStatus = utils_detector.detectNitrogen() #Nitrogen
openboxStatus = utils_detector.detectOpenBox() #Openbox
kdeStatus = utils_detector.detectKde() #Kde

#Configure normal widgets
def widgetConfigurer(widgetType, xPos, yPos, xSize, ySize, name, image=None, styleSheet=None):
    widgetType.setGeometry(QtCore.QRect(xPos, yPos, xSize, ySize))
    widgetType.setObjectName(_fromUtf8(name))
    
    if image is not None:
        widgetType.setPixmap(QtGui.QPixmap(_fromUtf8(image)))
        
    if styleSheet is not None:
        widgetType.setStyleSheet(_fromUtf8(styleSheet))
        
#Configure widgets held in a layout
def layoutConfigurer(name, widgetType, minW, minH, maxH, maxW, flat, focus, image):
    widgetType.setObjectName(_fromUtf8(name))
    if minW or minH is not None:
        widgetType.setMinimumSize(QtCore.QSize(minW, minH))
    
    if maxH or maxW is not None:
        widgetType.setMaximumSize(QtCore.QSize(maxH, maxW))
        
    if flat:
        widgetType.setFlat(True)
    
    if focus:
        widgetType.setFocusPolicy(QtCore.Qt.NoFocus)
    
    if image:
        widgetType.setPixmap(QtGui.QPixmap(_fromUtf8(image)))
        

#Create static widgets that are the same on all pages        
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
        self.welcomeMenuContainer = QtGui.QWidget(self.welcomeToManjaro)
        self.welcomeMenuContainerHLayout = QtGui.QHBoxLayout(self.welcomeMenuContainer)
        self.welcomeButton = QtGui.QPushButton(self.welcomeMenuContainer)
        self.welcomeArrow = QtGui.QLabel(self.welcomeMenuContainer)
        self.welcomeFolders = QtGui.QPushButton(self.welcomeMenuContainer)
        self.welcomeMenuSpacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.welcomeWhatIsManjaro = QtGui.QLabel(self.welcomeToManjaro)
        self.welcomeManjaroDesc = QtGui.QLabel(self.welcomeToManjaro)
        #self.welcomeBullet1 = QtGui.QLabel(self.welcomeToManjaro)
        #self.welcomeBullet2 = QtGui.QLabel(self.welcomeToManjaro)
        #self.welcomeBullet3 = QtGui.QLabel(self.welcomeToManjaro)
        #self.welcomeBullet4 = QtGui.QLabel(self.welcomeToManjaro)
        self.welcomeFooterContainer = QtGui.QWidget(self.welcomeToManjaro)
        self.welcomeFooterContainerHLayout = QtGui.QHBoxLayout(self.welcomeFooterContainer)
        self.welcomeFooterSpacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.welcomeForward = QtGui.QPushButton(self.welcomeFooterContainer)
        self.welcomeCancel = QtGui.QPushButton(self.welcomeFooterContainer)
        
        
        #widget dictionary
        firstPageWidgets = {
            "welcomeHeader": [self.welcomeHeader, 80, 20, 361, 51, "welcomeHeader", None],
            "welcomeWhatIsManjaro": [self.welcomeWhatIsManjaro, 30, 180, 480, 71, "welcomeWhatIsManjaro", None],
            "welcomeManjaroDesc": [self.welcomeManjaroDesc, 70, 260, 610, 260, "welcomeManjaroDesc", None],
            #"welcomeBullet1": [self.welcomeBullet1, 70, 365, 21, 21, "welcomeBullet1", "/usr/share/turbulence/images/manjaro-grey/bullet.png"],
            #"welcomeBullet2": [self.welcomeBullet2, 70, 395, 21, 21, "welcomeBullet2", "/usr/share/turbulence/images/manjaro-grey/bullet.png"],
            #"welcomeBullet3": [self.welcomeBullet3, 70, 425, 21, 21, "welcomeBullet3", "/usr/share/turbulence/images/manjaro-grey/bullet.png"],
            #"welcomeBullet4": [self.welcomeBullet4, 70, 470, 21, 21, "welcomeBullet4", "/usr/share/turbulence/images/manjaro-grey/bullet.png"],
        }
        
        firstPageLayouts = {
            "welcomeButton": [self.welcomeButton, 0, 39, None, None, True, True, False],
            "welcomeArrow": [self.welcomeArrow, None, None, 21, 500, False, False, "/usr/share/turbulence/images/manjaro-grey/menu-arrow.png"],
            "welcomeFolders": [self.welcomeFolders, 0, 39, None, None, True, True, False],
            "welcomeForward": [self.welcomeForward, 0, 34, None, None, True, True, False],
            "welcomeCancel": [self.welcomeCancel, 0, 34, None, None, True, True, False]
        }
        
        #defines all the widget parameters
        for widgetName, widgetSettings in firstPageWidgets.items():
            widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
            
        for widgetName, widgetSettings in firstPageLayouts.items():
            layoutConfigurer(widgetName, widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6], widgetSettings[7])
        
        #defines all the custom settings        
        self.welcomeForward.setIcon(forwardIcon)
        self.welcomeCancel.setIcon(cancelIcon)
        self.welcomeForward.setIconSize(QtCore.QSize(28, 30))
        self.welcomeCancel.setIconSize(QtCore.QSize(16, 16))
        
        self.welcomeMenuContainerHLayout.addWidget(self.welcomeButton)
        self.welcomeMenuContainerHLayout.addWidget(self.welcomeArrow)
        self.welcomeMenuContainerHLayout.addWidget(self.welcomeFolders)
        self.welcomeMenuContainerHLayout.addItem(self.welcomeMenuSpacer)
        self.welcomeFooterContainerHLayout.addWidget(self.welcomeCancel)
        self.welcomeFooterContainerHLayout.addItem(self.welcomeFooterSpacer)
        self.welcomeFooterContainerHLayout.addWidget(self.welcomeForward)
        self.welcomeMenuContainer.setGeometry(QtCore.QRect(20, 87, 511, 43))
        self.welcomeFooterContainer.setGeometry(QtCore.QRect(15, 567, 830, 51))
        
        self.welcomeManjaroDesc.setTextFormat(QtCore.Qt.RichText)
        self.welcomeManjaroDesc.setWordWrap(True)
        
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
        #self.welcomeManjaroDesc.setText(_translate("MainWindow", """Hello, and welcome to Manjaro.\n\nManjaro is a sleek and fast distro, featuring benefits from the popular Arch OS, along with ease of use.\nDeveloped in Austria, France, and Germany, Manjaro aims at new users, and experienced users.\n\nSome of Manjaro\'s features are:\n\n     Speed, power, and efficiency\n\n     Access to the very latest cutting and bleeding edge software\n\n     A ‘rolling release’ development model that provides the most up-to-date system possible without\n     the need to install new versions\n\n     Access to the Arch User Repository (AUR).\n\nOver these next few steps, Turbulence will guide you through customizing your new copy of Manjaro.""", None))
        self.welcomeManjaroDesc.setText(_translate("MainWindow", """<b>Manjaro</b> is a sleek and fast distro, featuring benefits from the popular Arch OS, along with ease of use. Developed in Austria, France, and Germany, Manjaro aims at new users, and experienced users.<br><br>Some of Manjaro\'s features are:  <ul><li>Speed, power, and efficiency</li><li>Access to the very latest cutting and bleeding edge software</li> <li>A ‘rolling release’ development model that provides the most up-to-date system possible without the need to install new versions</li><li>Access to the Arch User Repository (AUR).</li></ul>Over these next few steps, Turbulence will guide you through customizing your new copy of Manjaro.""", None))
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
            "folderSubHeader": [self.folderSubHeader, 50, 240, 81, 31, "folderSubHeader", None],
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
        
        self.folderMenu.setFocusPolicy(QtCore.Qt.NoFocus)
        self.folderThemes.setFocusPolicy(QtCore.Qt.NoFocus)
        self.folderCancel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.folderForward.setFocusPolicy(QtCore.Qt.NoFocus)
        self.folderPrevious.setFocusPolicy(QtCore.Qt.NoFocus)
        
        self.folderPrevious.setIcon(previousIcon)
        self.folderCancel.setIcon(cancelIcon)
        self.folderForward.setIcon(forwardIcon)
        self.folderPrevious.setIconSize(QtCore.QSize(28, 30))
        self.folderForward.setIconSize(QtCore.QSize(28, 30))
        self.folderCancel.setIconSize(QtCore.QSize(16, 16))
        
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
        
            self.themeMenu.setFocusPolicy(QtCore.Qt.NoFocus)
            self.themeMenuWallpapers.setFocusPolicy(QtCore.Qt.NoFocus)
            self.themeCancel.setFocusPolicy(QtCore.Qt.NoFocus)
            self.themeForward.setFocusPolicy(QtCore.Qt.NoFocus)
            self.themePrevious.setFocusPolicy(QtCore.Qt.NoFocus)
        
            self.themeCancel.setIcon(cancelIcon)
            self.themeForward.setIcon(forwardIcon)
            self.themePrevious.setIcon(previousIcon)
            self.themeForward.setIconSize(QtCore.QSize(28, 30))
            self.themePrevious.setIconSize(QtCore.QSize(28, 30))
            self.themeCancel.setIconSize(QtCore.QSize(16, 16))
        
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
             
        if tintStatus:
            #Starts the third page in the stacked widget.
            self.Tint = QtGui.QWidget()
            self.Tint.setObjectName(_fromUtf8("Tint"))
        
            createStaticWidgets(self.Tint)
            self.tintHeader = QtGui.QLabel(self.Tint)
            self.tintMenu = QtGui.QPushButton(self.Tint)
            self.tintArrow = QtGui.QLabel(self.Tint)
            self.tintMenuWallpapers = QtGui.QPushButton(self.Tint)
            self.tintCancel = QtGui.QPushButton(self.Tint)
            self.tintForward = QtGui.QPushButton(self.Tint)
            self.tintPrevious = QtGui.QPushButton(self.Tint)
            self.tintPositionIcon = QtGui.QLabel(self.Tint)
            self.tintPositionDesc = QtGui.QLabel(self.Tint)
            self.tintPositionHeader = QtGui.QLabel(self.Tint)
            self.tintPosition1 = QtGui.QLabel(self.Tint)
            self.tintPosition2 = QtGui.QLabel(self.Tint)
            self.tintPosition3 = QtGui.QLabel(self.Tint)
            self.tintPosition4 = QtGui.QLabel(self.Tint)
            self.tintPositionRadio1 = QtGui.QRadioButton(self.Tint)
            self.tintPositionRadio2 = QtGui.QRadioButton(self.Tint)
            self.tintPositionRadio3 = QtGui.QRadioButton(self.Tint)
            self.tintPositionRadio4 = QtGui.QRadioButton(self.Tint)
        
            thirdPageWidgets = {
                "tintHeader": [self.tintHeader, 80, 20, 111, 51, "tintHeader", None],
                "tintMenu": [self.tintMenu, 20, 90, 81, 41, "tintMenu", None],
                "tintArrow": [self.tintArrow, 120, 90, 31, 41, "tintArrow", "/usr/share/turbulence/images/manjaro-grey/arrow.png"],
                "tintMenuWallpapers": [self.tintMenuWallpapers, 150, 90, 111, 41, "tintMenuWallpapers", None],
                "tintCancel": [self.tintCancel, 20, 575, 110, 33, "tintCancel", None],
                "tintForward": [self.tintForward, 730, 575, 111, 33, "tintForward", None],
                "tintPrevious": [self.tintPrevious, 620, 575, 101, 33, "tintPrevious", None],
                "tintPositionIcon": [self.tintPositionIcon, 40, 160, 61, 61, "tintPositionIcon", "/usr/share/turbulence/images/manjaro-grey/tint-previews/position.png"],
                "tintPositionDesc": [self.tintPositionDesc, 110, 168, 591, 51, "tintPositionDesc", None],
                "tintPositionHeader": [self.tintPositionHeader, 50, 240, 91, 31, "tintPositionHeader", None],
                "tintPosition1": [self.tintPosition1, 90, 280, 241, 83, "tintPosition1", "/usr/share/turbulence/images/manjaro-grey/tint-previews/top.png"],
                "tintPosition2": [self.tintPosition2, 530, 280, 241, 83, "tintPosition2", "/usr/share/turbulence/images/manjaro-grey/tint-previews/right.png"],
                "tintPosition3": [self.tintPosition3, 90, 410, 241, 83, "tintPosition3", "/usr/share/turbulence/images/manjaro-grey/tint-previews/bottom.png"],
                "tintPosition4": [self.tintPosition4, 530, 410, 241, 83, "tintPosition4", "/usr/share/turbulence/images/manjaro-grey/tint-previews/left.png"],
                "tintPositionRadio1": [self.tintPositionRadio1, 165, 370, 131, 21, "tintPositionRadio1", None],
                "tintPositionRadio2": [self.tintPositionRadio2, 600, 370, 131, 21, "tintPositionRadio2", None],
                "tintPositionRadio3": [self.tintPositionRadio3, 165, 500, 131, 21, "tintPositionRadio3", None],
                "tintPositionRadio4": [self.tintPositionRadio4, 600, 500, 131, 21, "tintPositionRadio4", None]
            }
        
            #defines all the widget parameters
            for widgetName, widgetSettings in thirdPageWidgets.items():
                widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
        
            #Defines the custom settings
            self.tintMenu.setFlat(True)
            self.tintMenuWallpapers.setFlat(True)
            self.tintCancel.setFlat(True)
            self.tintForward.setFlat(True)
            self.tintPrevious.setFlat(True)
         
            self.tintMenu.setFocusPolicy(QtCore.Qt.NoFocus)
            self.tintMenuWallpapers.setFocusPolicy(QtCore.Qt.NoFocus)
            self.tintCancel.setFocusPolicy(QtCore.Qt.NoFocus)
            self.tintForward.setFocusPolicy(QtCore.Qt.NoFocus)
            self.tintPrevious.setFocusPolicy(QtCore.Qt.NoFocus)
        
            self.tintCancel.setIcon(cancelIcon)
            self.tintForward.setIcon(forwardIcon)
            self.tintPrevious.setIcon(previousIcon)
            self.tintCancel.setIconSize(QtCore.QSize(16, 16))
            self.tintForward.setIconSize(QtCore.QSize(28, 30))
            self.tintPrevious.setIconSize(QtCore.QSize(28, 30))
        
            #Adds the third page
            self.stackedWidget.addWidget(self.Tint)
            
            #Handles button clicks
            QtCore.QObject.connect(self.tintMenuWallpapers, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonNextTint)
            QtCore.QObject.connect(self.tintPrevious, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonPrevFolders)
            QtCore.QObject.connect(self.tintForward, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonNextTint)
            QtCore.QObject.connect(self.tintCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
            
            #Sets text and translates widgets
            self.tintHeader.setText(_translate("MainWindow", "Tint 2", None))
            self.tintMenu.setText(_translate("MainWindow", "Tint 2", None))
            self.tintMenuWallpapers.setText("Wallpapers")
            self.tintCancel.setText(_translate("MainWindow", "Cancel", None))
            self.tintForward.setText(_translate("MainWindow", "Forward", None))
            self.tintPrevious.setText(_translate("MainWindow", "Previous", None))
            self.tintPositionDesc.setText(_translate("MainWindow", "Here you can choose what position you want of your Tint 2 panel.\n", None))
            self.tintPositionHeader.setText(_translate("MainWindow", "Tint 2", None))
            self.tintPositionRadio1.setText(_translate("MainWindow", "Top", None))
            self.tintPositionRadio2.setText(_translate("MainWindow", "Right", None))
            self.tintPositionRadio3.setText(_translate("MainWindow", "Bottom", None))
            self.tintPositionRadio4.setText(_translate("MainWindow", "Left", None))
        
        
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
            
            self.wallpaperMenu.setFocusPolicy(QtCore.Qt.NoFocus)
            self.wallpaperMenuFinish.setFocusPolicy(QtCore.Qt.NoFocus)
            self.wallpaperPrevious.setFocusPolicy(QtCore.Qt.NoFocus)
            self.wallpaperForward.setFocusPolicy(QtCore.Qt.NoFocus)
            self.wallpaperCancel.setFocusPolicy(QtCore.Qt.NoFocus)
        
            self.wallpaperPrevious.setIcon(previousIcon)
            self.wallpaperForward.setIcon(forwardIcon)
            self.wallpaperCancel.setIcon(cancelIcon)
            self.wallpaperPrevious.setIconSize(QtCore.QSize(28, 30))
            self.wallpaperForward.setIconSize(QtCore.QSize(28, 30))
            self.wallpaperCancel.setIconSize(QtCore.QSize(16, 16))
        
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
            self.wallpaperChoice8.setText("Snow Leopard")
        
        
        if openboxStatus:
            #Adds the sixth page.
            self.Packages = QtGui.QWidget()
            self.Packages.setObjectName(_fromUtf8("Packages"))
        
            #Creates all the widgets
            createStaticWidgets(self.Packages)
            
            self.packagesHeader = QtGui.QLabel(self.Packages)
            self.packagesMenu = QtGui.QPushButton(self.Packages)
            self.packagesArrow = QtGui.QLabel(self.Packages)
            self.packagesMenuFinish = QtGui.QPushButton(self.Packages)
            self.packagesIcon = QtGui.QLabel(self.Packages)
            self.packagesDesc = QtGui.QLabel(self.Packages)
            self.packagesPrevious = QtGui.QPushButton(self.Packages)
            self.packagesForward = QtGui.QPushButton(self.Packages)
            self.packagesCancel = QtGui.QPushButton(self.Packages)
            self.packagesHeaderHead = QtGui.QLabel(self.Packages)
            self.packagesTabs = QtGui.QTabWidget(self.Packages)
            self.packagesNetwork = QtGui.QWidget()
            self.packagesNetworkBack = QtGui.QLabel(self.packagesNetwork)
            self.packagesAroraPic = QtGui.QLabel(self.packagesNetwork)
            self.packagesAroraCheck = QtGui.QCheckBox(self.packagesNetwork)
            self.packagesDelugePic = QtGui.QLabel(self.packagesNetwork)
            self.packagesDelugeCheck = QtGui.QCheckBox(self.packagesNetwork)
            self.packagesChromiumPic = QtGui.QLabel(self.packagesNetwork)
            self.packagesChromiumCheck = QtGui.QCheckBox(self.packagesNetwork)
            self.packagesFirefoxPic = QtGui.QLabel(self.packagesNetwork)
            self.packagesFirefoxCheck = QtGui.QCheckBox(self.packagesNetwork)
            self.packagesMidoriPic = QtGui.QLabel(self.packagesNetwork)
            self.packagesMidoriCheck = QtGui.QCheckBox(self.packagesNetwork)
            self.packagesOperaPic = QtGui.QLabel(self.packagesNetwork)
            self.packagesOperaCheck = QtGui.QCheckBox(self.packagesNetwork)
            self.packagesTransmissionPic = QtGui.QLabel(self.packagesNetwork)
            self.packagesTransmissionCheck = QtGui.QCheckBox(self.packagesNetwork)
            self.packagesNotActive = QtGui.QLabel(self.packagesNetwork)
            self.packagesMultimedia = QtGui.QWidget()
            self.packagesMultimediaBack = QtGui.QLabel(self.packagesMultimedia)
            self.packagesVlcPic = QtGui.QLabel(self.packagesMultimedia)
            self.packagesVlcCheck = QtGui.QCheckBox(self.packagesMultimedia)
            self.packagesSmplayerPic = QtGui.QLabel(self.packagesMultimedia)
            self.packagesSmplayerCheck = QtGui.QCheckBox(self.packagesMultimedia)
            self.packagesAudaciousPic = QtGui.QLabel(self.packagesMultimedia)
            self.packagesAudaciousCheck = QtGui.QCheckBox(self.packagesMultimedia)
            self.packagesClemetinePic = QtGui.QLabel(self.packagesMultimedia)
            self.packagesClementineCheck = QtGui.QCheckBox(self.packagesMultimedia)
            self.packagesDeadbeefPic = QtGui.QLabel(self.packagesMultimedia)
            self.packagesDeadbeefCheck = QtGui.QCheckBox(self.packagesMultimedia)
            self.packagesGraphics = QtGui.QWidget()
            self.packagesGraphicsBack = QtGui.QLabel(self.packagesGraphics)
            self.packagesBlenderPic = QtGui.QLabel(self.packagesGraphics)
            self.packagesBlenderCheck = QtGui.QCheckBox(self.packagesGraphics)
            self.packagesEvincePic = QtGui.QLabel(self.packagesGraphics)
            self.packagesEvinceCheck = QtGui.QCheckBox(self.packagesGraphics)
            self.packagesGimpPic = QtGui.QLabel(self.packagesGraphics)
            self.packagesGimpCheck = QtGui.QCheckBox(self.packagesGraphics)
            self.packagesGpicviewPic = QtGui.QLabel(self.packagesGraphics)
            self.packagesGpicviewCheck = QtGui.QCheckBox(self.packagesGraphics)
            self.packagesViewniorPic = QtGui.QLabel(self.packagesGraphics)
            self.packagesViewniorCheck = QtGui.QCheckBox(self.packagesGraphics)
            self.packagesAccessories = QtGui.QWidget()
            self.packagesAccessoriesBack = QtGui.QLabel(self.packagesAccessories)
            self.packagesGeanyPic = QtGui.QLabel(self.packagesAccessories)
            self.packagesGeanyCheck = QtGui.QCheckBox(self.packagesAccessories)
            self.packagesHexchatPic = QtGui.QLabel(self.packagesAccessories)
            self.packagesHexchatCheck = QtGui.QCheckBox(self.packagesAccessories)
            self.packagesLeafpadPic = QtGui.QLabel(self.packagesAccessories)
            self.packagesLeafpadCheck = QtGui.QCheckBox(self.packagesAccessories)
            self.packagesPcmanfmPic = QtGui.QLabel(self.packagesAccessories)
            self.packagesPcmanfmCheck = QtGui.QCheckBox(self.packagesAccessories)
            self.packagesSpacefmPic = QtGui.QLabel(self.packagesAccessories)
            self.packagesSpacefmCheck = QtGui.QCheckBox(self.packagesAccessories)
            self.packagesTerminatorPic = QtGui.QLabel(self.packagesAccessories)
            self.packagesTerminatorCheck = QtGui.QCheckBox(self.packagesAccessories)
            self.packagesThunarPic = QtGui.QLabel(self.packagesAccessories)
            self.packagesThunarCheck = QtGui.QCheckBox(self.packagesAccessories)
            self.packagesExtras = QtGui.QWidget()
            self.packagesExtrasBack = QtGui.QLabel(self.packagesExtras)
            self.packagesAurSupportPic = QtGui.QLabel(self.packagesExtras)
            self.packagesAurSupportCheck = QtGui.QCheckBox(self.packagesExtras)
            self.packagesMultimediaSupportPic = QtGui.QLabel(self.packagesExtras)
            self.packagesMultimediaSupportCheck = QtGui.QCheckBox(self.packagesExtras)
            self.packagesPrinterSupportPic = QtGui.QLabel(self.packagesExtras)
            self.packagesPrinterSupportCheck = QtGui.QCheckBox(self.packagesExtras)
            self.packagesInstall = QtGui.QWidget()
            self.packagesInstallBack = QtGui.QLabel(self.packagesInstall)
            self.packagesInstallButton = QtGui.QPushButton(self.packagesInstall)
            self.packagesCheckConnection = QtGui.QPushButton(self.Packages)
        
            fifthPageWidgets = {
                "packagesHeader": [self.packagesHeader, 80, 20, 141, 51, "packagesHeader", None],
                "packagesMenu": [self.packagesMenu, 20, 90, 121, 41, "packagesMenu", None],
                "packagesArrow": [self.packagesArrow, 150, 90, 31, 41, "packagesArrow", "/usr/share/turbulence/images/manjaro-grey/arrow.png"],
                "packagesMenuFinish": [self.packagesMenuFinish, 180, 90, 71, 41, "packagesMenuFinish", None],
                "packagesIcon": [self.packagesIcon, 40, 160, 61, 61, "packagesIcon", "/usr/share/turbulence/images/manjaro-grey/packages/packagesicon.png"],
                "packagesDesc": [self.packagesDesc, 110, 140, 650, 100, "packagesDesc", None],
                "packagesPrevious": [self.packagesPrevious, 620, 575, 101, 33, "packagesPrevious", None],
                "packagesForward": [self.packagesForward, 730, 575, 111, 33, "packagesForward", None],
                "packagesCancel": [self.packagesCancel, 20, 575, 110, 33, "packagesCancel", None],
                "packagesHeaderHead": [self.packagesHeaderHead, 50, 240, 101, 31, "packagesHeaderHead", None],
                "packagesTabs": [self.packagesTabs, 60, 290, 741, 251, "packagesTabs", None],
                "packagesNetworkBack": [self.packagesNetworkBack, -14, -7, 761, 241, "packagesNetworkBack", "/usr/share/turbulence/images/manjaro-grey/packages/packages-back.png"],
                "packagesAroraPic": [self.packagesAroraPic, 20, 10, 71, 71, "packagesAroraPic", "/usr/share/turbulence/images/manjaro-grey/packages/network/arora.png"],
                "packagesAroaCheck": [self.packagesAroraCheck, 10, 80, 111, 31, "packagesAroraCheck", None],
                "packagesChromiumPic": [self.packagesChromiumPic, 140, 10, 71, 71, "packagesChromiumPic", "/usr/share/turbulence/images/manjaro-grey/packages/network/chromium.png"],
                "packagesChromiumCheck": [self.packagesChromiumCheck, 130, 80, 102, 31, "packagesChromiumCheck", None],
                "packagesDelugePic": [self.packagesDelugePic, 270, 10, 71, 71, "packagesDelugePic", "/usr/share/turbulence/images/manjaro-grey/packages/network/deluge.png"],
                "packagesDelugeCheck": [self.packagesDelugeCheck, 260, 80, 102, 31, "packagesDelugeCheck", None],
                "packagesFirefoxPic": [self.packagesFirefoxPic, 400, 10, 71, 71, "packagesFirefoxPic", "/usr/share/turbulence/images/manjaro-grey/packages/network/firefox.png"],
                "packagesFirefoxCheck": [self.packagesFirefoxCheck, 390, 80, 102, 31, "packagesFirefoxCheck", None],
                "packagesMidoriPic": [self.packagesMidoriPic, 520, 10, 71, 71, "packagesMidoriPic", "/usr/share/turbulence/images/manjaro-grey/packages/network/midori.png"],
                "packagesMidoriCheck": [self.packagesMidoriCheck, 510, 80, 121, 31, "packagesMidoriCheck", None],
                "packagesOperaPic": [self.packagesOperaPic, 640, 10, 71, 71, "packagesOperaPic", "/usr/share/turbulence/images/manjaro-grey/packages/network/opera.png"],
                "packagesOperaCheck": [self.packagesOperaCheck, 630, 80, 102, 31, "packagesOperaCheck", None],
                "packagesTransmissionPic": [self.packagesTransmissionPic, 20, 110, 71, 71, "packagesTransmissionPic", "/usr/share/turbulence/images/manjaro-grey/packages/network/transmission.png"],
                "packagesTransmissionCheck": [self.packagesTransmissionCheck, 10, 180, 121, 31, "packagesTransmissionCheck", None],
                "packagesNotActive": [self.packagesNotActive, -10, -10, 751, 241, "packagesNotActive", None],
                "packagesMultimediaBack": [self.packagesMultimediaBack, -20, -10, 761, 241, "packagesMultimediaBack", "/usr/share/turbulence/images/manjaro-grey/packages/packages-back.png"],
                "packagesAudaciousPic": [self.packagesAudaciousPic, 20, 10, 71, 71, "packagesAudaciousPic", "/usr/share/turbulence/images/manjaro-grey/packages/multimedia/audacious.png"],
                "packagesAudaciousCheck": [self.packagesAudaciousCheck, 10, 80, 111, 31, "packagesAudaciousCheck", None],
                "packagesClementinePic": [self.packagesClemetinePic, 140, 10, 71, 71, "packagesClementinePic", "/usr/share/turbulence/images/manjaro-grey/packages/multimedia/clementine.png"],
                "packagesClementineCheck": [self.packagesClementineCheck, 130, 80, 111, 31, "packagesClementineCheck", None],
                "packagesDeadbeefPic": [self.packagesDeadbeefPic, 270, 10, 71, 71, "packagesDeadbeefPic", "/usr/share/turbulence/images/manjaro-grey/packages/multimedia/deadbeef.png"],
                "packagesDeadbeefCheck": [self.packagesDeadbeefCheck, 260, 80, 111, 31, "packagesDeadbeefCheck", None],
                "packagesSmplayerPic": [self.packagesSmplayerPic, 400, 10, 71, 71, "packagesSmplayerPic", "/usr/share/turbulence/images/manjaro-grey/packages/multimedia/smplayer.png"],
                "packagesSmplayerCheck": [self.packagesSmplayerCheck, 390, 80, 102, 31, "packagesSmplayerCheck", None],
                "packagesVlcPic": [self.packagesVlcPic, 520, 10, 71, 71, "packagesVlcPic", "/usr/share/turbulence/images/manjaro-grey/packages/multimedia/vlc.png"],
                "packagesVlcCheck": [self.packagesVlcCheck, 510, 80, 102, 31, "packagesVlcCheck", None],
                "packagesGraphicsBack": [self.packagesGraphicsBack, -20, -10, 761, 241, "packagesGraphicsBack", "/usr/share/turbulence/images/manjaro-grey/packages/packages-back.png"],
                "packagesBlenderPic": [self.packagesBlenderPic, 20, 10, 71, 71, "packagesBlenderPic", "/usr/share/turbulence/images/manjaro-grey/packages/graphics/blender.png"],
                "packagesBlenderCheck": [self.packagesBlenderCheck, 10, 80, 111, 31, "packagesBlenderCheck", None],
                "packagesEvincePic": [self.packagesEvincePic, 140, 10, 71, 71, "packagesEvincePic", "/usr/share/turbulence/images/manjaro-grey/packages/graphics/evince.png"],
                "packagesEvinceCheck": [self.packagesEvinceCheck, 130, 80, 111, 31, "packagesEvinceCheck", None],
                "packagesGimpPic": [self.packagesGimpPic, 270, 10, 71, 71, "packagesGimpPic", "/usr/share/turbulence/images/manjaro-grey/packages/graphics/gimp.png"],
                "packagesGimpCheck": [self.packagesGimpCheck, 260, 80, 111, 31, "packagesGimpCheck", None],
                "packagesGpicviewPic": [self.packagesGpicviewPic, 400, 10, 71, 71, "packagesGpicviewPic", "/usr/share/turbulence/images/manjaro-grey/packages/graphics/gpicview.png"],
                "packagesGpicviewCheck": [self.packagesGpicviewCheck, 390, 80, 111, 31, "packagesGpicviewCheck", None],
                "packagesViewniorPic": [self.packagesViewniorPic, 520, 10, 71, 71, "packagesViewniorPic", "/usr/share/turbulence/images/manjaro-grey/packages/graphics/viewnior.png"],
                "packagesViewniorCheck": [self.packagesViewniorCheck, 510, 80, 111, 31, "packagesViewniorCheck", None],
                "packagesAccessoriesBack": [self.packagesAccessoriesBack, -20, -10, 761, 241, "packagesAccessoriesBack", "/usr/share/turbulence/images/manjaro-grey/packages/packages-back.png"],
                "packagesGeanyPic": [self.packagesGeanyPic, 20, 10, 71, 71, "packagesGeanyPic", "/usr/share/turbulence/images/manjaro-grey/packages/accessories/geany.png"],
                "packagesGeanyCheck": [self.packagesGeanyCheck, 10, 80, 111, 31, "packagesGeanyCheck", None],
                "packagesHexchatPic": [self.packagesHexchatPic, 140, 10, 71, 71, "packagesHexchatPic", "/usr/share/turbulence/images/manjaro-grey/packages/accessories/hexchat.png"],
                "packagesHexchatCheck": [self.packagesHexchatCheck, 130, 80, 111, 31, "packagesHexchatCheck", None],
                "packagesLeafpadPic": [self.packagesLeafpadPic, 270, 10, 71, 71, "packagesLeafpadPic", "/usr/share/turbulence/images/manjaro-grey/packages/accessories/leafpad.png"],
                "packagesLeafpadCheck": [self.packagesLeafpadCheck, 260, 80, 111, 31, "packagesLeafpadCheck", None],
                "packagesPcmanfmPic": [self.packagesPcmanfmPic, 400, 10, 71, 71, "packagesPcmanfmPic", "/usr/share/turbulence/images/manjaro-grey/packages/accessories/pcmanfm.png"],
                "packagesPcmanfmCheck": [self.packagesPcmanfmCheck, 390, 80, 111, 31, "packagesPcmanfmCheck", None],
                "packagesSpacefmPic": [self.packagesSpacefmPic, 520, 10, 71, 71, "packagesSpacefmPic", "/usr/share/turbulence/images/manjaro-grey/packages/accessories/spacefm.png"],
                "packagesSpacefmCheck": [self.packagesSpacefmCheck, 510, 80, 111, 31, "packagesSpacefmCheck", None],
                "packagesTerminatorPic": [self.packagesTerminatorPic, 640, 10, 71, 71, "packagesTerminatorPic", "/usr/share/turbulence/images/manjaro-grey/packages/accessories/terminator.png"],
                "packagesTerminatorCheck": [self.packagesTerminatorCheck, 630, 80, 111, 31, "packagesTerminatorCheck", None],
                "packagesThunarPic": [self.packagesThunarPic, 20, 110, 71, 71, "packagesThunarPic" , "/usr/share/turbulence/images/manjaro-grey/packages/accessories/thunar.png"],
                "packagesThunarCheck": [self.packagesThunarCheck, 10, 180, 111, 31, "packagesThunarCheck", None],
                "packagesExtrasBack": [self.packagesExtrasBack, -20, -10, 761, 241, "packagesExtrasBack", "/usr/share/turbulence/images/manjaro-grey/packages/packages-back.png"],
                "packagesAurSupportPic": [self.packagesAurSupportPic, 20, 10, 71, 71, "packagesAurSupportPic" , "/usr/share/turbulence/images/manjaro-grey/packages/extras/aursupport.png"],
                "packagesAurSupportCheck": [self.packagesAurSupportCheck, 10, 90, 111, 41, "packagesAurSupportCheck", None],
                "packagesMultimediaSupportPic": [self.packagesMultimediaSupportPic, 140, 10, 71, 71, "packagesMultimediaSupportPic" , "/usr/share/turbulence/images/manjaro-grey/packages/extras/multimediasupport.png"],
                "packagesMultimediaSupportCheck": [self.packagesMultimediaSupportCheck, 130, 90, 111, 34, "packagesMultimediaSupportCheck", None],
                "packagesPrinterSupportPic": [self.packagesPrinterSupportPic, 270, 10, 71, 71, "packagesPrinterSupportPic" , "/usr/share/turbulence/images/manjaro-grey/packages/extras/printersupport.png"],
                "packagesPrinterSupportCheck": [self.packagesPrinterSupportCheck, 260, 90, 111, 41, "packagesPrinterSupportCheck", None],
                "packagesInstallBack": [self.packagesInstallBack, -20, -10, 761, 241, "packagesInstallBack", None],
                "packagesInstallButton": [self.packagesInstallButton, 310, 95, 111, 31, "packagesInstallButton", None],
                "packagesCheckConnection": [self.packagesCheckConnection, 230, 400, 380, 60, "packagesCheckConnection", None]
            }

            #defines all the widget parameters
            for widgetName, widgetSettings in fifthPageWidgets.items():
                widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
        
            #Adds any custom widgets.
            self.packagesMenu.setFlat(True)
            self.packagesMenuFinish.setFlat(True)
            self.packagesPrevious.setFlat(True)
            self.packagesForward.setFlat(True)
            self.packagesCancel.setFlat(True)
            self.packagesCheckConnection.setFlat(True)
            self.packagesInstallButton.setFlat(True)
        
            self.packagesMenu.setFocusPolicy(QtCore.Qt.NoFocus)
            self.packagesMenuFinish.setFocusPolicy(QtCore.Qt.NoFocus)
            self.packagesPrevious.setFocusPolicy(QtCore.Qt.NoFocus)
            self.packagesForward.setFocusPolicy(QtCore.Qt.NoFocus)
            self.packagesCancel.setFocusPolicy(QtCore.Qt.NoFocus)
            self.packagesCheckConnection.setFocusPolicy(QtCore.Qt.NoFocus)
            self.packagesInstallButton.setFocusPolicy(QtCore.Qt.NoFocus)
        
            self.packagesPrevious.setIcon(previousIcon)
            self.packagesForward.setIcon(forwardIcon)
            self.packagesCancel.setIcon(cancelIcon)
            self.packagesPrevious.setIconSize(QtCore.QSize(28, 30))
            self.packagesForward.setIconSize(QtCore.QSize(28, 30))
            self.packagesCancel.setIconSize(QtCore.QSize(16, 16))
         
            self.packagesNetwork.setObjectName(_fromUtf8("Network"))
            self.packagesMultimedia.setObjectName(_fromUtf8("Multimedia"))
            self.packagesGraphics.setObjectName(_fromUtf8("Graphics"))
            self.packagesAccessories.setObjectName(_fromUtf8("Accessories"))
            self.packagesExtras.setObjectName(_fromUtf8("Extras"))
            self.packagesInstall.setObjectName(_fromUtf8("Install"))
        
            self.packagesTabs.addTab(self.packagesNetwork, _fromUtf8(""))
            self.packagesTabs.addTab(self.packagesMultimedia, _fromUtf8(""))
            self.packagesTabs.addTab(self.packagesGraphics, _fromUtf8(""))
            self.packagesTabs.addTab(self.packagesAccessories, _fromUtf8(""))
            self.packagesTabs.addTab(self.packagesExtras, _fromUtf8(""))
            self.packagesTabs.addTab(self.packagesInstall, _fromUtf8(""))
        
            self.packagesTabs.tabBar().setEnabled(False)
            self.stackedWidget.addWidget(self.Packages)
            
            #Handles button clicks
            QtCore.QObject.connect(self.packagesCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
            QtCore.QObject.connect(self.packagesPrevious, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonPrev)
            QtCore.QObject.connect(self.packagesForward, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonNextPackages)
            QtCore.QObject.connect(self.packagesMenuFinish, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonNextPackages)
            QtCore.QObject.connect(self.packagesCheckConnection, QtCore.SIGNAL(_fromUtf8("clicked()")), self.checkInternetStatus)
            QtCore.QObject.connect(self.packagesInstallButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonInstallPackages)
            
            #Fifth page
            self.packagesHeader.setText("Packages")
            self.packagesMenu.setText("Packages")
            self.packagesMenuFinish.setText("Finish")
            self.packagesDesc.setText(_translate("MainWindow", "Here, you can choose what packages you would like to install. Hover over any of the \npackages to see a description, and select or unselect any packages you want to add or \nremove. Packages that are installed will be auto-selected.\n\nWhen you are done, go to the Install tab, and click \"Install\".", None))
            self.packagesPrevious.setText(_translate("MainWindow", "Previous", None))
            self.packagesForward.setText(_translate("MainWindow", "Forward", None))
            self.packagesCancel.setText(_translate("MainWindow", "Cancel", None))
            self.packagesHeaderHead.setText("Packages")
            self.packagesCheckConnection.setText(_translate("MainWindow", "Check For Internet Connection", None))
            self.packagesFirefoxPic.setToolTip(_translate("MainWindow", "Standalone web browser from mozilla.org", None))
            self.packagesAroraPic.setToolTip(_translate("MainWindow", "Lightweight cross-platform Web browser", None))
            self.packagesAroraCheck.setText(_translate("MainWindow", "Arora", None))
            self.packagesChromiumPic.setToolTip(_translate("MainWindow", "The open-source project behind Google Chrome, an \n" "attempt at creating a safer, faster, and more stable browser", None))
            self.packagesOperaPic.setToolTip(_translate("MainWindow", "Fast and secure web browser and Internet suite", None))
            self.packagesTransmissionPic.setToolTip(_translate("MainWindow", "Fast, easy, and free BitTorrent client", None))
            self.packagesFirefoxCheck.setText(_translate("MainWindow", "Firefox", None))
            self.packagesMidoriPic.setToolTip(_translate("MainWindow", "Lightweight web browser (GTK2)", None))
            self.packagesChromiumCheck.setText(_translate("MainWindow", "Chomium", None))
            self.packagesOperaCheck.setText(_translate("MainWindow", "Opera", None))
            self.packagesTransmissionCheck.setText(_translate("MainWindow", "Transmission", None))
            self.packagesMidoriCheck.setText(_translate("MainWindow", "Midori", None))
            self.packagesDelugePic.setToolTip(_translate("MainWindow", "A BitTorrent client with multiple user interfaces \n" "in a client/server model", None))
            self.packagesDelugeCheck.setText(_translate("MainWindow", "Deluge", None))
            self.packagesTabs.setTabText(self.packagesTabs.indexOf(self.packagesNetwork), _translate("MainWindow", "Network", None))
            self.packagesVlcPic.setToolTip(_translate("MainWindow", "A multi-platform MPEG, VCD/DVD, and DivX player", None))
            self.packagesVlcCheck.setText(_translate("MainWindow", "VLC", None))
            self.packagesSmplayerPic.setToolTip(_translate("MainWindow", "A complete front-end for MPlayer", None))
            self.packagesSmplayerCheck.setText(_translate("MainWindow", "SMPlayer", None))
            self.packagesAudaciousPic.setToolTip(_translate("MainWindow", "Lightweight, advanced audio player focused on audio quality", None))
            self.packagesAudaciousCheck.setText(_translate("MainWindow", "Audacious", None))
            self.packagesClemetinePic.setToolTip(_translate("MainWindow", "A music player and library organizer", None))
            self.packagesClementineCheck.setText(_translate("MainWindow", "Clementine", None))
            self.packagesDeadbeefPic.setToolTip(_translate("MainWindow", "An audio player for GNU/Linux based on GTK2.", None))
            self.packagesDeadbeefCheck.setText(_translate("MainWindow", "DeaDBeeF", None))
            self.packagesTabs.setTabText(self.packagesTabs.indexOf(self.packagesMultimedia), _translate("MainWindow", "Multimedia", None))
            self.packagesBlenderPic.setToolTip(_translate("MainWindow", "A fully integrated 3D graphics creation suite", None))
            self.packagesBlenderCheck.setText(_translate("MainWindow", "Blender", None))
            self.packagesEvincePic.setToolTip(_translate("MainWindow", "Simply a document viewer", None))
            self.packagesEvinceCheck.setText(_translate("MainWindow", "Evince", None))
            self.packagesGimpPic.setToolTip(_translate("MainWindow", "GNU Image Manipulation Program", None))
            self.packagesGimpCheck.setText(_translate("MainWindow", "Gimp", None))
            self.packagesGpicviewPic.setToolTip(_translate("MainWindow", "Lightweight image viewer", None))
            self.packagesGpicviewCheck.setText(_translate("MainWindow", "GPicView", None))
            self.packagesViewniorPic.setToolTip(_translate("MainWindow", "A simple, fast and elegant image viewer program", None))
            self.packagesViewniorCheck.setText(_translate("MainWindow", "Viewnior", None))
            self.packagesTabs.setTabText(self.packagesTabs.indexOf(self.packagesGraphics), _translate("MainWindow", "Graphics", None))
            self.packagesGeanyPic.setToolTip(_translate("MainWindow", "Fast and lightweight IDE", None))
            self.packagesGeanyCheck.setText(_translate("MainWindow", "Geany", None))
            self.packagesHexchatPic.setToolTip(_translate("MainWindow", "A popular and easy to use graphical IRC (chat) client", None))
            self.packagesHexchatCheck.setText(_translate("MainWindow", "Hexchat", None))
            self.packagesLeafpadPic.setToolTip(_translate("MainWindow", "A notepad clone for GTK+ 2.0", None))
            self.packagesLeafpadCheck.setText(_translate("MainWindow", "Leafpad", None))
            self.packagesPcmanfmPic.setToolTip(_translate("MainWindow", "An extremely fast and lightweight file manager", None))
            self.packagesPcmanfmCheck.setText(_translate("MainWindow", "PCManFM", None))
            self.packagesSpacefmPic.setToolTip(_translate("MainWindow", "Multi-panel tabbed file manager", None))
            self.packagesSpacefmCheck.setText(_translate("MainWindow", "SpaceFM", None))
            self.packagesTerminatorPic.setToolTip(_translate("MainWindow", "Terminal emulator that supports tabs and grids", None))
            self.packagesTerminatorCheck.setText(_translate("MainWindow", "Terminator", None))
            self.packagesThunarPic.setToolTip(_translate("MainWindow", "Modern file manager for Xfce", None))
            self.packagesThunarCheck.setText(_translate("MainWindow", "Thunar", None))
            self.packagesTabs.setTabText(self.packagesTabs.indexOf(self.packagesAccessories), _translate("MainWindow", "Accessories", None))
            self.packagesAurSupportPic.setToolTip(_translate("MainWindow", "Installs yaourt, and required dependencies to access the AUR", None))
            self.packagesAurSupportCheck.setText(_translate("MainWindow", "Aur \nSupport", None))
            self.packagesMultimediaSupportPic.setToolTip(_translate("MainWindow", "Installs flashplugin, and required codecs for playing media", None))
            self.packagesMultimediaSupportCheck.setText(_translate("MainWindow", "Multimedia \nSupport", None))
            self.packagesPrinterSupportPic.setToolTip(_translate("MainWindow", "Installs manjaro-printer, and CUPS to enable printers", None))
            self.packagesPrinterSupportCheck.setText(_translate("MainWindow", "Printer \nSupport", None))
            self.packagesTabs.setTabText(self.packagesTabs.indexOf(self.packagesExtras), _translate("MainWindow", "Extras", None))
            self.packagesTabs.setTabText(self.packagesTabs.indexOf(self.packagesInstall), "Install")
            self.packagesInstallButton.setText("Install")
        
        
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
            "finishSystemSettingsDesc": [self.finishSystemSettingsDesc, 200, 280, 390, 31, "finishSystemSettingsDesc", None],
            "finishSystemSettingsButton": [self.finishSystemSettingsButton, 300, 310, 181, 41, "finishSystemSettingsButton", None],
            "finishHelpHead": [self.finishHelpHead, 40, 400, 71, 31, "finishHelpHead", None, None],
            "finishHelpPic": [self.finishHelpPic, 70, 440, 111, 101, "finishHelpPic", "/usr/share/turbulence/images/manjaro-grey/finish/help-icon.png"],
            "finishHelpDesc": [self.finishHelpDesc, 200, 440, 391, 51, "finishHelpDesc", None],
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
        
        self.finishWallpaperMenu.setFocusPolicy(QtCore.Qt.NoFocus)
        self.finishMenu.setFocusPolicy(QtCore.Qt.NoFocus)
        self.finishCancel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.finishForward.setFocusPolicy(QtCore.Qt.NoFocus)
        self.finishPrevious.setFocusPolicy(QtCore.Qt.NoFocus)
        self.finishSystemSettingsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.finishHelpButton.setFocusPolicy(QtCore.Qt.NoFocus)
        
        self.finishCancel.setIcon(cancelIcon)
        self.finishForward.setIcon(finishIcon)
        self.finishPrevious.setIcon(previousIcon)
        self.finishForward.setIconSize(QtCore.QSize(16, 18))
        self.finishPrevious.setIconSize(QtCore.QSize(28, 30))
        self.finishCancel.setIconSize(QtCore.QSize(16, 16))
        
        self.stackedWidget.addWidget(self.Finish)
        
        #Handles the button click
        QtCore.QObject.connect(self.finishWallpaperMenu, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonPrev)
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
        self.finishHelpHead.setText(_translate("MainWindow", "Help", None))
        self.finishHelpDesc.setText(_translate("MainWindow", "For help and support, you can visit Manjaro.org for access \nto a terrific forum, wiki, and IRC!", None))
        self.finishHelpButton.setText(_translate("MainWindow", "Launch Manjaro.org", None))
        
        if kdeStatus:
            self.finishSystemSettings.setText(_translate("MainWindow", "System Settings", None))
            self.finishSystemSettingsDesc.setText(_translate("MainWindow", "Control panel to edit various aspects of the KDE desktop, \nand more.", None))
            self.finishSystemSettingsButton.setText(_translate("MainWindow", "Launch System Settings", None))
            QtCore.QObject.connect(self.finishSystemSettingsButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonSystemSettings)
        elif openboxStatus:
            self.finishSystemSettings.setText(_translate("MainWindow", "Customize OpenBox", None))
            self.finishSystemSettingsDesc.setText(_translate("MainWindow", "Control panel to edit various aspects of OpenBox", None))
            self.finishSystemSettingsButton.setText(_translate("MainWindow", "Launch Customize \nLook and Feel", None))
            QtCore.QObject.connect(self.finishSystemSettingsButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleButtonlxappearance)
        
        
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
            
    #Moves next a page, but also applies to settings for tint.
    def handleButtonNextTint(self):
        Tint = {
            "top": self.tintPositionRadio1,
            "right": self.tintPositionRadio2,
            "bottom": self.tintPositionRadio3,
            "left": self.tintPositionRadio4,
        }
        
        for tintPosition, tintRadio in Tint.items():
            if tintRadio.isChecked():
                tint.panelPosition(tintPosition)
                ob_control.killTintTwoPlus()

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
            logger.writeLog('proceedToPackages')

            
    def handleButtonNextPackages(self):
        index = self.stackedWidget.currentIndex() + 1
        if index < self.stackedWidget.count():
            self.stackedWidget.setCurrentIndex(index)
            logger.writeLog('proceedToFinal')
    
    #Moves from the folder slide toward the package installer.
    def handleButtonInstallPackages(self):
        packagesMFI = {
            "arora": self.packagesAroraCheck, 
            "chromium": self.packagesChromiumCheck, 
            "deluge": self.packagesDelugeCheck,
            "firefox": self.packagesFirefoxCheck,
            "midori": self.packagesMidoriCheck,
            "opera": self.packagesOperaCheck, 
            "transmission-gtk": self.packagesTransmissionCheck,
            "audacious": self.packagesAudaciousCheck,
            "clementine": self.packagesClementineCheck,
            "deadbeef": self.packagesDeadbeefCheck, 
            "smplayer": self.packagesSmplayerCheck,
            "vlc": self.packagesVlcCheck,
            "blender": self.packagesBlenderCheck,
            "evince": self.packagesEvinceCheck,
            "gimp": self.packagesGimpCheck,
            "gpicview": self.packagesGpicviewCheck,
            "viewnior": self.packagesViewniorCheck,
            "geany": self.packagesGeanyCheck,
            "hexchat": self.packagesHexchatCheck,
            "leafpad": self.packagesLeafpadCheck,
            "pcmanfm": self.packagesPcmanfmCheck,
            "spacefm": self.packagesSpacefmCheck,
            "terminator": self.packagesTerminatorCheck,
            "thunar": self.packagesThunarCheck,
            "yaourt": self.packagesAurSupportCheck, #Aur support
            "flashplugin": self.packagesMultimediaSupportCheck, #Multimedia support
            "manjaro-printer": self.packagesPrinterSupportCheck #Printing support
            
        }
        #self.installButton.lower()
        packagesTBIList = []
        packagesTBRList = []
        for packageName, packageCheck in packagesMFI.items():
            if packageCheck.isChecked():
                packagesTBIList.append(packageName)
            else:
                packagesTBRList.append(packageName)
        packages.handlePackages(packagesTBIList, packagesTBRList)
	    
    def checkInternetStatus(self):
        packagesList = packages.getCurrentPackages()
        if packages.checkInternet():
            self.packagesTabs.tabBar().setEnabled(True)
            self.packagesCheckConnection.lower()
            self.packagesNotActive.lower()
            logger.writeLog("checkInternetStatusPassed")
        else:
            self.packagesCheckConnection.setText(_translate("MainWindow", "Failed. Please Try Again.", None))
            logger.writeLog("checkInternetStatusFailed")
        
        packagesMFI = {
            "arora": self.packagesAroraCheck, 
            "chromium": self.packagesChromiumCheck, 
            "deluge": self.packagesDelugeCheck,
            "firefox": self.packagesFirefoxCheck,
            "midori": self.packagesMidoriCheck,
            "opera": self.packagesOperaCheck, 
            "transmission-gtk": self.packagesTransmissionCheck,
            "audacious": self.packagesAudaciousCheck,
            "clementine": self.packagesClementineCheck,
            "deadbeef": self.packagesDeadbeefCheck, 
            "smplayer": self.packagesSmplayerCheck,
            "vlc": self.packagesVlcCheck,
            "blender": self.packagesBlenderCheck,
            "evince": self.packagesEvinceCheck,
            "gimp": self.packagesGimpCheck,
            "gpicview": self.packagesGpicviewCheck,
            "viewnior": self.packagesViewniorCheck,
            "geany": self.packagesGeanyCheck,
            "hexchat": self.packagesHexchatCheck,
            "leafpad": self.packagesLeafpadCheck,
            "pcmanfm": self.packagesPcmanfmCheck,
            "spacefm": self.packagesSpacefmCheck,
            "terminator": self.packagesTerminatorCheck,
            "thunar": self.packagesThunarCheck,
            "yaourt": self.packagesAurSupportCheck, #Aur support
            "flashplugin": self.packagesMultimediaSupportCheck, #Multimedia support
            "manjaro-printer": self.packagesPrinterSupportCheck #Printing support
        }
        packagesAI = set(packagesList).intersection(packagesMFI)
        packagesAIList = list(packagesAI)
        
        for packagesItem in packagesAIList:
            packagesMFI[packagesItem].setChecked(True)	
            
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
        
    def handleButtonlxappearance(self):
        final.launchAppearance()
        
    def handleButtonLaunchHelp(self):
        final.launchHelp()

    #Just moves back a page..
    def handleButtonPrev(self):
        index = self.stackedWidget.currentIndex() - 1
        if index >= 0:
            self.stackedWidget.setCurrentIndex(index)