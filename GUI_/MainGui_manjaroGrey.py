#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import needed libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from tools_ import * 

_translate = QtCore.QCoreApplication.translate

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
    widgetType.setObjectName(name)
    
    if image is not None:
        widgetType.setPixmap(QtGui.QPixmap(image))
        
    if styleSheet is not None:
        widgetType.setStyleSheet(styleSheet)
        
#Configure widgets held in a layout
def layoutConfigurer(name, widgetType, minW, minH, maxH, maxW, flat, focus, image, position=False):
    widgetType.setObjectName(name)
    if minW or minH is not None:
        widgetType.setMinimumSize(QtCore.QSize(minW, minH))
    
    if maxH or maxW is not None:
        widgetType.setMaximumSize(QtCore.QSize(maxH, maxW))
        
    if flat:
        widgetType.setFlat(True)
    
    if focus:
        widgetType.setFocusPolicy(QtCore.Qt.NoFocus)
    
    if image:
        widgetType.setPixmap(QtGui.QPixmap(image))
        
    if position:
        widgetType.setAlignment(QtCore.Qt.AlignCenter)
        

#Create static widgets that are the same on all pages        
def createStaticWidgets(parent):
    global blackBackground; blackBackground = QtWidgets.QLabel(parent)
    global headerBack; headerBack = QtWidgets.QLabel(parent)
    global turbulenceLogo; turbulenceLogo = QtWidgets.QLabel(parent)
    global menuBackg; menuBackg = QtWidgets.QLabel(parent)
    global footerBack; footerBack = QtWidgets.QLabel(parent)
    
    staticWidgets = {
        "blackBackground": [blackBackground, -14, 0, 891, 625, "blackBackground", "/usr/share/turbulence/images/manjaro-grey/background.jpg"],
        "headerBack": [headerBack, -20, 10, 921, 71, "headerBack", "/usr/share/turbulence/images/manjaro-grey/header.png"],
        "turbulenceLogo": [turbulenceLogo, 20, 20, 51, 51, "turbulenceLogo", "/usr/share/turbulence/images/manjaro-grey/turbulence.png"],
        "menuBackg": [menuBackg, -20, 91, 901, 41, "menuBackg", None],
        "footerBack": [footerBack, 0, 572, 861, 51, "footerBack", None]
    }
    
    for widgetName, widgetSettings in staticWidgets.items():
        widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])

    return blackBackground, headerBack, turbulenceLogo, menuBackg, footerBack

#Begins to main class
class Ui_MainWindow(QtCore.QObject):
    def setupUi(self, MainWindow):
            
        #Grabs the stylesheet
        styleSheetFile = open("/usr/share/turbulence/stylesheets/manjarogrey.qss", "r")
        self.styleData = styleSheetFile.read()
        styleSheetFile.close()
      
        #Sets up the main window
        MainWindow.setObjectName("Turbulence")
        MainWindow.resize(839, 594)
        MainWindow.setMinimumSize(QtCore.QSize(839, 594))
        MainWindow.setMaximumSize(QtCore.QSize(839, 594))
        MainWindow.setWindowIcon(QtGui.QIcon('/usr/share/turbulence/images/manjaro-grey/turbulence.png'))
        MainWindow.setStyleSheet(self.styleData)
        
        forwardIcon = QtGui.QIcon()
        forwardIcon.addPixmap(QtGui.QPixmap("/usr/share/turbulence/images/manjaro-grey/arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        cancelIcon = QtGui.QIcon()
        cancelIcon.addPixmap(QtGui.QPixmap("/usr/share/turbulence/images/manjaro-grey/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        previousIcon = QtGui.QIcon()
        previousIcon.addPixmap(QtGui.QPixmap("/usr/share/turbulence/images/manjaro-grey/arrowreverse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        finishIcon = QtGui.QIcon()
        finishIcon.addPixmap(QtGui.QPixmap("/usr/share/turbulence/images/manjaro-grey/checkmark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #Defines the stacked widget
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        widgetConfigurer(self.stackedWidget, -10, -20, 861, 621, "stackedWidget", None, None)
        
        #Starts the first page in the stacked widget, or Manjaro welcome
        self.welcomeToManjaro = QtWidgets.QWidget()
        self.welcomeToManjaro.setObjectName("welcomeToManjaro")

        #Defines all the widgets for the first page
        createStaticWidgets(self.welcomeToManjaro)
        self.welcomeHeader = QtWidgets.QLabel(self.welcomeToManjaro)
        self.welcomeMenuContainer = QtWidgets.QWidget(self.welcomeToManjaro)
        self.welcomeMenuContainerHLayout = QtWidgets.QHBoxLayout(self.welcomeMenuContainer)
        self.welcomeButton = QtWidgets.QPushButton(self.welcomeMenuContainer)
        self.welcomeArrow = QtWidgets.QLabel(self.welcomeMenuContainer)
        self.welcomeFolders = QtWidgets.QPushButton(self.welcomeMenuContainer)
        self.welcomeMenuSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.welcomeWhatIsManjaro = QtWidgets.QLabel(self.welcomeToManjaro)
        self.welcomeManjaroDesc = QtWidgets.QLabel(self.welcomeToManjaro)
        self.welcomeFooterContainer = QtWidgets.QWidget(self.welcomeToManjaro)
        self.welcomeFooterContainerHLayout = QtWidgets.QHBoxLayout(self.welcomeFooterContainer)
        self.welcomeFooterSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.welcomeForward = QtWidgets.QPushButton(self.welcomeFooterContainer)
        self.welcomeCancel = QtWidgets.QPushButton(self.welcomeFooterContainer)
        
        #widget dictionary
        firstPageWidgets = {
            "welcomeHeader": [self.welcomeHeader, 80, 20, 600, 51, "welcomeHeader", None],
            "welcomeWhatIsManjaro": [self.welcomeWhatIsManjaro, 30, 180, 600, 71, "welcomeWhatIsManjaro", None],
            "welcomeManjaroDesc": [self.welcomeManjaroDesc, 70, 260, 650, 300, "welcomeManjaroDesc", None],
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
        
        self.welcomeMenuContainer.setGeometry(QtCore.QRect(20, 83, 511, 50))
        self.welcomeFooterContainer.setGeometry(QtCore.QRect(15, 567, 830, 51))
        
        self.welcomeManjaroDesc.setTextFormat(QtCore.Qt.RichText)
        self.welcomeManjaroDesc.setWordWrap(True)
        
        #adds the first page
        self.stackedWidget.addWidget(self.welcomeToManjaro)
        
        #Hooks up the button handlers
        self.welcomeFolders.clicked.connect(self.handleButtonNext)
        self.welcomeForward.clicked.connect(self.handleButtonNext)
        self.welcomeCancel.clicked.connect(MainWindow.close)
        
        #Translates, or sets the text to the widgets
        self.welcomeHeader.setText(_translate("MainWindow", "Welcome To Manjaro!"))
        self.welcomeButton.setText(_translate("MainWindow", "Welcome"))
        self.welcomeFolders.setText(_translate("MainWindow", "Folders"))
        self.welcomeWhatIsManjaro.setText(_translate("MainWindow", "What is Manjaro?"))
        self.welcomeManjaroDesc.setText(_translate("MainWindow", """<b>Manjaro</b> is a sleek and fast distro, featuring benefits from the popular Arch OS, along with ease of use. Developed in Austria, France, and Germany, Manjaro aims at new users, and experienced users.\n<br><br>\nSome of Manjaro's features are:\n<ul>\n<li>Speed, power, and efficiency</li>\n<li>Access to the very latest cutting and bleeding edge software</li>\n<li>A ‘rolling release’ development model that provides the most up-to-date system possible without the need to install new versions</li>\n<li>Access to the Arch User Repository (AUR).</li>\n</ul>\nFor newcomers, a user-friendly installer is provided, and the system itself is designed to work fully straight out of the box. For more experienced, and adventurous users, Manjaro also offers the configurability and versatility to be shaped and moulded in every respect to suit personal taste and preference.\n<br><br>\nOver these next few steps, Turbulence will guide you through customizing your new copy of Manjaro."""))
        self.welcomeCancel.setText(_translate("MainWindow", "Cancel"))
        self.welcomeForward.setText(_translate("MainWindow", "Forward"))
         
        #Starts the second page in the stacked widget.
        self.folders = QtWidgets.QWidget()
        self.folders.setObjectName("folders")
        
        #Defines all the widget for the second page
        createStaticWidgets(self.folders)
        
        self.folderHeader = QtWidgets.QLabel(self.folders)
        self.folderMenuContainer = QtWidgets.QWidget(self.folders)
        self.folderMenuContainerHLayout = QtWidgets.QHBoxLayout(self.folderMenuContainer)
        self.folderMenu = QtWidgets.QPushButton(self.folderMenuContainer)
        self.folderArrow = QtWidgets.QLabel(self.folderMenuContainer)
        self.folderThemes = QtWidgets.QPushButton(self.folderMenuContainer)
        self.folderMenuSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.folderFooterContainer = QtWidgets.QWidget(self.folders)
        self.folderFooterContainerHLayout = QtWidgets.QHBoxLayout(self.folderFooterContainer)
        self.folderCancel = QtWidgets.QPushButton(self.folderFooterContainer)
        self.folderFooterSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.folderForward = QtWidgets.QPushButton(self.folderFooterContainer)
        self.folderPrevious = QtWidgets.QPushButton(self.folderFooterContainer)
        self.folderIcon = QtWidgets.QLabel(self.folders)
        self.folderDesc = QtWidgets.QLabel(self.folders)
        self.folderContentsUpper = QtWidgets.QWidget(self.folders)
        self.folderContentsUpperLayout = QtWidgets.QGridLayout(self.folderContentsUpper)
        self.folderIcon1 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderIcon2 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderIcon3 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderIcon4 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderIcon5 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderIcon6 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderIcon7 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderIcon8 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderHeader1 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderHeader2 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderHeader3 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderHeader4 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderHeader5 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderHeader6 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderHeader7 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderHeader8 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderName1 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderName2 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderName3 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderName4 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderName5 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderName6 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderName7 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderName8 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderActive1 = QtWidgets.QCheckBox(self.folderContentsUpper)
        self.folderActive2 = QtWidgets.QCheckBox(self.folderContentsUpper)
        self.folderActive3 = QtWidgets.QCheckBox(self.folderContentsUpper)
        self.folderActive4 = QtWidgets.QCheckBox(self.folderContentsUpper)
        self.folderActive5 = QtWidgets.QCheckBox(self.folderContentsUpper)
        self.folderActive6 = QtWidgets.QCheckBox(self.folderContentsUpper)
        self.folderActive7 = QtWidgets.QCheckBox(self.folderContentsUpper)
        self.folderActive8 = QtWidgets.QCheckBox(self.folderContentsUpper)
        self.folderContentsUpperSpacer1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.folderContentsUpperSpacer2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.folderContentsUpperSpacer3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        
        if kwinStatus and tintStatus:
            self.folderThemes.setText(_translate("MainWindow", "Themes"))
        elif kwinStatus:
            self.folderThemes.setText(_translate("MainWindow", "Themes"))
        elif tintStatus:
            self.folderThemes.setText(_translate("MainWindow", "Tint 2"))
        else:
            self.folderThemes.setText(_translate("MainWindow", "Verify"))
            
        #widget dictionary.
        secondPageWidgets = {
            "folderHeader": [self.folderHeader, 80, 20, 600, 51, "folderHeader", None],
            "folderIcon": [self.folderIcon, 40, 150, 61, 61, "folderIcon", "/usr/share/turbulence/images/manjaro-grey/foldericons/folder.png"],
            "folderDesc": [self.folderDesc, 110, 160, 591, 51, "folderDesc", None]
        }
        
        secondPageLayouts = {
            "folderMenu": [self.folderMenu, 0, 39, None, None, True, True, False, False],
            "folderArrow": [self.folderArrow, None, None, 21, 500, False, False, "/usr/share/turbulence/images/manjaro-grey/menu-arrow.png", False],
            "folderThemes": [self.folderThemes, 0, 39, None, None, True, True, False, False],
            "folderForward": [self.folderForward, 0, 34, None, None, True, True, False, False],
            "folderPrevious": [self.folderPrevious, 0, 34, None, None, True, True, False, False],
            "folderCancel": [self.folderCancel, 0, 34, None, None, True, True, False, False],
            "folderIcon1": [self.folderIcon1, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/foldericons/desktop.png", True],
            "folderIcon2": [self.folderIcon2, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/foldericons/documents.png", True],
            "folderIcon3": [self.folderIcon3, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/foldericons/downloads.png", True],
            "folderIcon4": [self.folderIcon4, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/foldericons/music.png", True],
            "folderIcon5": [self.folderIcon5, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/foldericons/pictures.png", True],
            "folderIcon6": [self.folderIcon6, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/foldericons/public.png", True],
            "folderIcon7": [self.folderIcon7, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/foldericons/templates.png", True],
            "folderIcon8": [self.folderIcon8, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/foldericons/videos.png", True],
            "folderHeader1": [self.folderHeader1, None, None, None, None, False, False, False, False],
            "folderHeader2": [self.folderHeader2, None, None, None, None, False, False, False, False],
            "folderHeader3": [self.folderHeader3, None, None, None, None, False, False, False, False],
            "folderHeader4": [self.folderHeader4, None, None, None, None, False, False, False, False],
            "folderHeader5": [self.folderHeader5, None, None, None, None, False, False, False, False],
            "folderHeader6": [self.folderHeader6, None, None, None, None, False, False, False, False],
            "folderHeader7": [self.folderHeader7, None, None, None, None, False, False, False, False],
            "folderHeader8": [self.folderHeader8, None, None, None, None, False, False, False, False],
            "folderName1": [self.folderName1, None, None, None, None, False, False, False, True],
            "folderName2": [self.folderName2, None, None, None, None, False, False, False, True],
            "folderName3": [self.folderName3, None, None, None, None, False, False, False, True],
            "folderName4": [self.folderName4, None, None, None, None, False, False, False, True],
            "folderName5": [self.folderName5, None, None, None, None, False, False, False, True],
            "folderName6": [self.folderName6, None, None, None, None, False, False, False, True],
            "folderName7": [self.folderName7, None, None, None, None, False, False, False, True],
            "folderName8": [self.folderName8, None, None, None, None, False, False, False, True],
            "folderActive1": [self.folderActive1, None, None, None, None, False, False, False, False],
            "folderActive2": [self.folderActive2, None, None, None, None, False, False, False, False],
            "folderActive3": [self.folderActive3, None, None, None, None, False, False, False, False],
            "folderActive4": [self.folderActive4, None, None, None, None, False, False, False, False],
            "folderActive5": [self.folderActive5, None, None, None, None, False, False, False, False],
            "folderActive6": [self.folderActive6, None, None, None, None, False, False, False, False],
            "folderActive7": [self.folderActive7, None, None, None, None, False, False, False, False],
            "folderActive8": [self.folderActive8, None, None, None, None, False, False, False, False]
        }
        
        #defines all the widget parameters
        for widgetName, widgetSettings in secondPageWidgets.items():
            widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
           
        for widgetName, widgetSettings in secondPageLayouts.items():
            layoutConfigurer(widgetName, widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6], widgetSettings[7], widgetSettings[8])
        
        #defines the custom settings
        self.folderPrevious.setIcon(previousIcon)
        self.folderCancel.setIcon(cancelIcon)
        self.folderForward.setIcon(forwardIcon)
        self.folderPrevious.setIconSize(QtCore.QSize(28, 30))
        self.folderForward.setIconSize(QtCore.QSize(28, 30))
        self.folderCancel.setIconSize(QtCore.QSize(16, 16))
        
        self.folderDesc.setWordWrap(True)
        
        self.folderMenuContainerHLayout.addWidget(self.folderMenu)
        self.folderMenuContainerHLayout.addWidget(self.folderArrow)
        self.folderMenuContainerHLayout.addWidget(self.folderThemes)
        self.folderMenuContainerHLayout.addItem(self.folderMenuSpacer)
        
        self.folderFooterContainerHLayout.addWidget(self.folderCancel)
        self.folderFooterContainerHLayout.addItem(self.folderFooterSpacer)
        self.folderFooterContainerHLayout.addWidget(self.folderPrevious)
        self.folderFooterContainerHLayout.addWidget(self.folderForward)
        
        self.folderContentsUpperLayout.addWidget(self.folderName1, 0, 0, 1, 1)
        self.folderContentsUpperLayout.addItem(self.folderContentsUpperSpacer1, 0, 1, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderName2, 0, 2, 1, 1)
        self.folderContentsUpperLayout.addItem(self.folderContentsUpperSpacer2, 0, 3, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderName3, 0, 4, 1, 1)
        self.folderContentsUpperLayout.addItem(self.folderContentsUpperSpacer3, 0, 5, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderName4, 0, 6, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderIcon1, 1, 0, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderIcon2, 1, 2, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderIcon3, 1, 4, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderIcon4, 1, 6, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderHeader1, 2, 0, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderHeader2, 2, 2, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderHeader3, 2, 4, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderHeader4, 2, 6, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderActive1, 3, 0, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderActive2, 3, 2, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderActive3, 3, 4, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderActive4, 3, 6, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderName5, 4, 0, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderName6, 4, 2, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderName7, 4, 4, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderName8, 4, 6, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderIcon5, 5, 0, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderIcon6, 5, 2, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderIcon7, 5, 4, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderIcon8, 5, 6, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderHeader5, 6, 0, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderHeader6, 6, 2, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderHeader7, 6, 4, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderHeader8, 6, 6, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderActive5, 7, 0, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderActive6, 7, 2, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderActive7, 7, 4, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderActive8, 7, 6, 1, 1)
        
        self.folderMenuContainer.setGeometry(QtCore.QRect(20, 83, 511, 50))
        self.folderFooterContainer.setGeometry(QtCore.QRect(15, 567, 830, 51))
        self.folderContentsUpper.setGeometry(QtCore.QRect(60, 230, 730, 320))
        
        #adds the second page
        self.stackedWidget.addWidget(self.folders)
        
        #Handles the button clicks.
        self.folderPrevious.clicked.connect(self.handleButtonPrev)
        self.folderCancel.clicked.connect(MainWindow.close)
        
        #Checks if you need the verify function yet. Hopefully not, because otherwise you're not on OB or KDE.... ;)
        if not kwinStatus and not tintStatus and not nitrogenStatus and not plasmaStatus and not openboxStatus:
            self.folderThemes.clicked.connect(self.handleButtonNextVerify)
            self.folderForward.clicked.connect(self.handleButtonNextVerify)
        else:
            self.folderThemes.clicked.connect(self.handleButtonNext)
            self.folderForward.clicked.connect(self.handleButtonNext)
        
        #Translates, or sets the text for all the widgets
        self.folderHeader.setText(_translate("MainWindow", "Folders"))
        self.folderMenu.setText(_translate("MainWindow", "Folders"))
        self.folderCancel.setText(_translate("MainWindow", "Cancel"))
        self.folderForward.setText(_translate("MainWindow", "Forward"))
        self.folderPrevious.setText(_translate("MainWindow", "Previous"))
        self.folderDesc.setText(_translate("MainWindow", "Here, you can choose which folders you want in your home directory. You have a choice from some of the most commonly used folders."))
        self.folderHeader1.setText(_translate("MainWindow", "Status: Deactivated"))
        self.folderHeader2.setText(_translate("MainWindow", "Status: Deactivated"))
        self.folderHeader3.setText(_translate("MainWindow", "Status: Deactivated"))
        self.folderHeader4.setText(_translate("MainWindow", "Status: Deactivated"))
        self.folderHeader5.setText(_translate("MainWindow", "Status: Deactivated"))
        self.folderHeader6.setText(_translate("MainWindow", "Status: Deactivated"))
        self.folderHeader7.setText(_translate("MainWindow", "Status: Deactivated"))
        self.folderHeader8.setText(_translate("MainWindow", "Status: Deactivated"))
        self.folderName1.setText(_translate("MainWindow", "Desktop"))
        self.folderName2.setText(_translate("MainWindow", "Documents"))
        self.folderName3.setText(_translate("MainWindow", "Downloads"))
        self.folderName4.setText(_translate("MainWindow", "Music"))
        self.folderName5.setText(_translate("MainWindow", "Pictures"))
        self.folderName6.setText(_translate("MainWindow", "Public"))
        self.folderName7.setText(_translate("MainWindow", "Templates"))
        self.folderName8.setText(_translate("MainWindow", "Videos"))
        self.folderActive1.setText(_translate("MainWindow", "Active"))
        self.folderActive2.setText(_translate("MainWindow", "Active"))
        self.folderActive3.setText(_translate("MainWindow", "Active"))
        self.folderActive4.setText(_translate("MainWindow", "Active"))
        self.folderActive5.setText(_translate("MainWindow", "Active"))
        self.folderActive6.setText(_translate("MainWindow", "Active"))
        self.folderActive7.setText(_translate("MainWindow", "Active"))
        self.folderActive8.setText(_translate("MainWindow", "Active"))
        
        
        #Checks if Kwin is running, and if so displays the kwin themer
        if kwinStatus: 
            #Starts the kwin page in the stacked widget
            self.Theme = QtWidgets.QWidget()
            self.Theme.setObjectName("Theme")
        
            createStaticWidgets(self.Theme)
            self.themeHeader = QtWidgets.QLabel(self.Theme)
            self.themeMenuContainer = QtWidgets.QWidget(self.Theme)
            self.themeMenuContainerHLayout = QtWidgets.QHBoxLayout(self.themeMenuContainer)
            self.themeMenu = QtWidgets.QPushButton(self.themeMenuContainer)
            self.themeArrow = QtWidgets.QLabel(self.themeMenuContainer)
            self.themeMenuWallpapers = QtWidgets.QPushButton(self.themeMenuContainer)
            self.themeMenuSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeFooterContainer = QtWidgets.QWidget(self.Theme)
            self.themeFooterContainerHLayout = QtWidgets.QHBoxLayout(self.themeFooterContainer)
            self.themeCancel = QtWidgets.QPushButton(self.Theme)
            self.themeFooterSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themePrevious = QtWidgets.QPushButton(self.Theme)
            self.themeForward = QtWidgets.QPushButton(self.Theme)
            self.themeIcon = QtWidgets.QLabel(self.Theme)
            self.themeDesc = QtWidgets.QLabel(self.Theme)
            self.themeContentsContainer = QtWidgets.QWidget(self.Theme)
            self.themeContentsContainerLayout = QtWidgets.QGridLayout(self.themeContentsContainer)
            self.themePreviewContainerLayout1 = QtWidgets.QHBoxLayout()
            self.themePreviewContainerLayout2 = QtWidgets.QHBoxLayout()
            self.themePreviewContainerLayout3 = QtWidgets.QHBoxLayout()
            self.themePreviewContainerLayout4 = QtWidgets.QHBoxLayout()
            self.themePreview1 = QtWidgets.QLabel(self.themeContentsContainer)
            self.themePreview2 = QtWidgets.QLabel(self.themeContentsContainer)
            self.themePreview3 = QtWidgets.QLabel(self.themeContentsContainer)
            self.themePreview4 = QtWidgets.QLabel(self.themeContentsContainer)
            self.themeRadio1 = QtWidgets.QRadioButton(self.themeContentsContainer)
            self.themeRadio2 = QtWidgets.QRadioButton(self.themeContentsContainer)
            self.themeRadio3 = QtWidgets.QRadioButton(self.themeContentsContainer)
            self.themeRadio4 = QtWidgets.QRadioButton(self.themeContentsContainer)
            self.themeContentsRadioPush1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeContentsRadioPush2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeContentsRadioPush3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeContentsRadioPush4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeContentsRadioPush5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeContentsRadioPush6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeContentsRadioPush7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeContentsRadioPush8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeContentsPush1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeContentsPush2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeContentsPush3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeContentsPush4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.themeContentsPush5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.themeContentsPush6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
            if tintStatus:
                 self.themeMenuWallpapers.setText(_translate("MainWindow", "Tint 2"))
            elif plasmaStatus:
                 self.themeMenuWallpapers.setText(_translate("MainWindow", "Wallpapers"))
            else:
                 self.themeMenuWallpapers.setText(_translate("MainWindow", "Verify"))
                 
            thirdPageWidgets = {
                "themeHeader": [self.themeHeader, 80, 20, 600, 51, "themeHeader", None],
                "themeIcon": [self.themeIcon, 40, 160, 61, 61, "themeIcon", "/usr/share/turbulence/images/manjaro-grey/themes/theme.png"],
                "themeDesc": [self.themeDesc, 110, 160, 591, 51, "themeDesc", None],
            }
             
            thirdPageLayouts = {
                "themeMenu": [self.themeMenu, 0, 39, None, None, True, True, False, False],
                "themeArrow": [self.themeArrow, None, None, 21, 500, False, False, "/usr/share/turbulence/images/manjaro-grey/menu-arrow.png", False],
                "themeMenuWallpapers": [self.themeMenuWallpapers, 0, 39, None, None, True, True, False, False],
                "themeForward": [self.themeForward, 0, 34, None, None, True, True, False, False],
                "themePrevious": [self.themePrevious, 0, 34, None, None, True, True, False, False],
                "themeCancel": [self.themeCancel, 0, 34, None, None, True, True, False, False],
                "themePreview1": [self.themePreview1, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/themes/air-black.png", True],
                "themePreview2": [self.themePreview2, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/themes/cupertino-ish.png", True],
                "themePreview3": [self.themePreview3, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/themes/oxygen.png", True],
                "themePreview4": [self.themePreview4, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/themes/plastik.png", True],
                "themeRadio1": [self.themeRadio1, None, None, None, None, False, False, False, False],
                "themeRadio2": [self.themeRadio2, None, None, None, None, False, False, False, False],
                "themeRadio3": [self.themeRadio3, None, None, None, None, False, False, False, False],
                "themeRadio4": [self.themeRadio4, None, None, None, None, False, False, False, False]
                
            }
        
            #defines all the widget parameters
            for widgetName, widgetSettings in thirdPageWidgets.items():
                widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
        
            for widgetName, widgetSettings in thirdPageLayouts.items():
                layoutConfigurer(widgetName, widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6], widgetSettings[7], widgetSettings[8])
        
            #Defines the custom settings
            self.themeCancel.setIcon(cancelIcon)
            self.themeForward.setIcon(forwardIcon)
            self.themePrevious.setIcon(previousIcon)
            self.themeForward.setIconSize(QtCore.QSize(28, 30))
            self.themePrevious.setIconSize(QtCore.QSize(28, 30))
            self.themeCancel.setIconSize(QtCore.QSize(16, 16))
            
            self.themeDesc.setWordWrap(True)
            
            #Sets the default item
            self.themeRadio1.setChecked(True)
            
            self.themeMenuContainerHLayout.addWidget(self.themeMenu)
            self.themeMenuContainerHLayout.addWidget(self.themeArrow)
            self.themeMenuContainerHLayout.addWidget(self.themeMenuWallpapers)
            self.themeMenuContainerHLayout.addItem(self.themeMenuSpacer)
            
            self.themeFooterContainerHLayout.addWidget(self.themeCancel)
            self.themeFooterContainerHLayout.addItem(self.themeFooterSpacer)
            self.themeFooterContainerHLayout.addWidget(self.themePrevious)
            self.themeFooterContainerHLayout.addWidget(self.themeForward)
            
            self.themePreviewContainerLayout1.addItem(self.themeContentsRadioPush1)
            self.themePreviewContainerLayout1.addWidget(self.themeRadio1)
            self.themePreviewContainerLayout1.addItem(self.themeContentsRadioPush2)
            self.themePreviewContainerLayout2.addItem(self.themeContentsRadioPush3)
            self.themePreviewContainerLayout2.addWidget(self.themeRadio2)
            self.themePreviewContainerLayout2.addItem(self.themeContentsRadioPush4)
            self.themePreviewContainerLayout3.addItem(self.themeContentsRadioPush5)
            self.themePreviewContainerLayout3.addWidget(self.themeRadio3)
            self.themePreviewContainerLayout3.addItem(self.themeContentsRadioPush6)
            self.themePreviewContainerLayout4.addItem(self.themeContentsRadioPush7)
            self.themePreviewContainerLayout4.addWidget(self.themeRadio4)
            self.themePreviewContainerLayout4.addItem(self.themeContentsRadioPush8)
            
            self.themeContentsContainerLayout.addItem(self.themeContentsPush4, 0, 3, 1, 1)
            self.themeContentsContainerLayout.addItem(self.themeContentsPush1, 1, 0, 1, 1)
            self.themeContentsContainerLayout.addWidget(self.themePreview1, 1, 1, 1, 1)
            self.themeContentsContainerLayout.addItem(self.themeContentsPush2, 1, 2, 1, 1)
            self.themeContentsContainerLayout.addWidget(self.themePreview2, 1, 3, 1, 1)
            self.themeContentsContainerLayout.addItem(self.themeContentsPush3, 1, 4, 1, 1)
            self.themeContentsContainerLayout.addLayout(self.themePreviewContainerLayout1, 2, 1, 1, 1)
            self.themeContentsContainerLayout.addLayout(self.themePreviewContainerLayout2, 2, 3, 1, 1)
            self.themeContentsContainerLayout.addItem(self.themeContentsPush5, 3, 2, 1, 1)
            self.themeContentsContainerLayout.addWidget(self.themePreview3, 4, 1, 1, 1)
            self.themeContentsContainerLayout.addWidget(self.themePreview4, 4, 3, 1, 1)
            self.themeContentsContainerLayout.addLayout(self.themePreviewContainerLayout3, 5, 1, 1, 1)
            self.themeContentsContainerLayout.addLayout(self.themePreviewContainerLayout4, 5, 3, 1, 1)
            self.themeContentsContainerLayout.addItem(self.themeContentsPush6, 6, 3, 1, 1)
            
            self.themeMenuContainer.setGeometry(QtCore.QRect(20, 83, 511, 50))
            self.themeFooterContainer.setGeometry(QtCore.QRect(15, 567, 830, 51))
            self.themeContentsContainer.setGeometry(QtCore.QRect(10, 230, 840, 340))
        
            #Adds the third page
            self.stackedWidget.addWidget(self.Theme)
            
            #Hooks up the button handlers
            self.themeCancel.clicked.connect(MainWindow.close)
            self.themePrevious.clicked.connect(self.handleButtonPrev)
            
            #Checks if you need the verify function yet. Hopefully not, because otherwise you're not on OB or KDE.... ;)
            if not tintStatus and not nitrogenStatus and not plasmaStatus and not openboxStatus:
                self.themeMenuWallpapers.clicked.connect(self.handleButtonNextVerify)
                self.themeForward.clicked.connect(self.handleButtonNextVerify)
            else:
                self.themeMenuWallpapers.clicked.connect(self.handleButtonNext)
                self.themeForward.clicked.connect(self.handleButtonNext)
                
            #Translates the text
            self.themeHeader.setText(_translate("MainWindow", "Themes"))
            self.themeMenu.setText(_translate("MainWindow", "Themes"))
            self.themeCancel.setText(_translate("MainWindow", "Cancel"))
            self.themeForward.setText(_translate("MainWindow", "Forward"))
            self.themePrevious.setText(_translate("MainWindow", "Previous"))
            self.themeDesc.setText(_translate("MainWindow", "Here you can choose what type of theme you want for your window decorations."))
            self.themeRadio1.setText("Air Black Green")
            self.themeRadio2.setText("Cuptertino-ish")
            self.themeRadio3.setText("Oxygen")
            self.themeRadio4.setText("Plastik")
            
        if tintStatus:
            #Starts the tint page in the stacked widget.
            self.Tint = QtWidgets.QWidget()
            self.Tint.setObjectName("Tint")
        
            createStaticWidgets(self.Tint)
            self.tintHeader = QtWidgets.QLabel(self.Tint)
            self.tintMenuContainer = QtWidgets.QWidget(self.Tint)
            self.tintMenuContainerHLayout = QtWidgets.QHBoxLayout(self.tintMenuContainer)
            self.tintMenu = QtWidgets.QPushButton(self.tintMenuContainer)
            self.tintArrow = QtWidgets.QLabel(self.tintMenuContainer)
            self.tintMenuWallpapers = QtWidgets.QPushButton(self.tintMenuContainer)
            self.tintMenuSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintFooterContainer = QtWidgets.QWidget(self.Tint)
            self.tintFooterContainerHLayout = QtWidgets.QHBoxLayout(self.tintFooterContainer)
            self.tintCancel = QtWidgets.QPushButton(self.tintFooterContainer)
            self.tintFooterSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintPrevious = QtWidgets.QPushButton(self.tintFooterContainer)
            self.tintForward = QtWidgets.QPushButton(self.tintFooterContainer)
            self.tintPositionIcon = QtWidgets.QLabel(self.Tint)
            self.tintPositionDesc = QtWidgets.QLabel(self.Tint)
            self.tintContentsContainer = QtWidgets.QWidget(self.Tint)
            self.tintContentsContainerLayout = QtWidgets.QGridLayout(self.tintContentsContainer)
            self.tintPreviewContainerLayout1 = QtWidgets.QHBoxLayout()
            self.tintPreviewContainerLayout2 = QtWidgets.QHBoxLayout()
            self.tintPreviewContainerLayout3 = QtWidgets.QHBoxLayout()
            self.tintPreviewContainerLayout4 = QtWidgets.QHBoxLayout()
            self.tintPosition1 = QtWidgets.QLabel(self.tintContentsContainer)
            self.tintPosition2 = QtWidgets.QLabel(self.tintContentsContainer)
            self.tintPosition3 = QtWidgets.QLabel(self.tintContentsContainer)
            self.tintPosition4 = QtWidgets.QLabel(self.tintContentsContainer)
            self.tintPositionRadio1 = QtWidgets.QRadioButton(self.tintContentsContainer)
            self.tintPositionRadio2 = QtWidgets.QRadioButton(self.tintContentsContainer)
            self.tintPositionRadio3 = QtWidgets.QRadioButton(self.tintContentsContainer)
            self.tintPositionRadio4 = QtWidgets.QRadioButton(self.tintContentsContainer)
            self.tintContentsRadioPush1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintContentsRadioPush2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintContentsRadioPush3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintContentsRadioPush4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintContentsRadioPush5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintContentsRadioPush6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintContentsRadioPush7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintContentsRadioPush8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintContentsPush1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintContentsPush2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintContentsPush3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintContentsPush4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.tintContentsPush5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.tintContentsPush6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            
            if nitrogenStatus or plasmaStatus:
                self.tintMenuWallpapers.setText(_translate("MainWindow", "Wallpapers"))
            else:
                self.tintMenuWallpapers.setText(_translate("MainWindow", "Verify"))
            
            thirdPageWidgets = {
                "tintHeader": [self.tintHeader, 80, 20, 600, 51, "tintHeader", None],
                "tintPositionIcon": [self.tintPositionIcon, 40, 160, 61, 61, "tintPositionIcon", "/usr/share/turbulence/images/manjaro-grey/tint-previews/position.png"],
                "tintPositionDesc": [self.tintPositionDesc, 110, 160, 591, 51, "tintPositionDesc", None]
            }
        
            thirdPageLayouts  = {
                "tintMenu": [self.tintMenu, 0, 39, None, None, True, True, False, False],
                "tintArrow": [self.tintArrow, None, None, 21, 500, False, False, "/usr/share/turbulence/images/manjaro-grey/menu-arrow.png", False],
                "tintMenuWallpapers": [self.tintMenuWallpapers, 0, 39, None, None, True, True, False, False],
                "tintForward": [self.tintForward, 0, 34, None, None, True, True, False, False],
                "tintPrevious": [self.tintPrevious, 0, 34, None, None, True, True, False, False],
                "tintCancel": [self.tintCancel, 0, 34, None, None, True, True, False, False],
                "tintPosition1": [self.tintPosition1, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/tint-previews/top.png", True],
                "tintPosition2": [self.tintPosition2, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/tint-previews/right.png", True],
                "tintPosition3": [self.tintPosition3, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/tint-previews/bottom.png", True],
                "tintPosition4": [self.tintPosition4, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/tint-previews/left.png", True],
                "tintPositionRadio1": [self.tintPositionRadio1, None, None, None, None, False, False, False, False],
                "tintPositionRadio2": [self.tintPositionRadio2, None, None, None, None, False, False, False, False],
                "tintPositionRadio3": [self.tintPositionRadio3, None, None, None, None, False, False, False, False],
                "tintPositionRadio4": [self.tintPositionRadio4, None, None, None, None, False, False, False, False]
            }
            
            #defines all the widget parameters
            for widgetName, widgetSettings in thirdPageWidgets.items():
                widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
        
            for widgetName, widgetSettings in thirdPageLayouts.items():
                layoutConfigurer(widgetName, widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6], widgetSettings[7], widgetSettings[8])
        
            #Defines the custom settings
            self.tintCancel.setIcon(cancelIcon)
            self.tintForward.setIcon(forwardIcon)
            self.tintPrevious.setIcon(previousIcon)
            self.tintCancel.setIconSize(QtCore.QSize(16, 16))
            self.tintForward.setIconSize(QtCore.QSize(28, 30))
            self.tintPrevious.setIconSize(QtCore.QSize(28, 30))
            
            self.tintPositionDesc.setWordWrap(True)
            
            #Sets the default item
            self.tintPositionRadio1.setChecked(True)
            
            self.tintMenuContainerHLayout.addWidget(self.tintMenu)
            self.tintMenuContainerHLayout.addWidget(self.tintArrow)
            self.tintMenuContainerHLayout.addWidget(self.tintMenuWallpapers)
            self.tintMenuContainerHLayout.addItem(self.tintMenuSpacer)
            
            self.tintFooterContainerHLayout.addWidget(self.tintCancel)
            self.tintFooterContainerHLayout.addItem(self.tintFooterSpacer)
            self.tintFooterContainerHLayout.addWidget(self.tintPrevious)
            self.tintFooterContainerHLayout.addWidget(self.tintForward)
            
            self.tintPreviewContainerLayout1.addItem(self.tintContentsRadioPush1)
            self.tintPreviewContainerLayout1.addWidget(self.tintPositionRadio1)
            self.tintPreviewContainerLayout1.addItem(self.tintContentsRadioPush2)
            self.tintPreviewContainerLayout2.addItem(self.tintContentsRadioPush3)
            self.tintPreviewContainerLayout2.addWidget(self.tintPositionRadio2)
            self.tintPreviewContainerLayout2.addItem(self.tintContentsRadioPush4)
            self.tintPreviewContainerLayout3.addItem(self.tintContentsRadioPush5)
            self.tintPreviewContainerLayout3.addWidget(self.tintPositionRadio3)
            self.tintPreviewContainerLayout3.addItem(self.tintContentsRadioPush6)
            self.tintPreviewContainerLayout4.addItem(self.tintContentsRadioPush7)
            self.tintPreviewContainerLayout4.addWidget(self.tintPositionRadio4)
            self.tintPreviewContainerLayout4.addItem(self.tintContentsRadioPush8)
            
            self.tintContentsContainerLayout.addItem(self.tintContentsPush4, 0, 3, 1, 1)
            self.tintContentsContainerLayout.addItem(self.tintContentsPush1, 1, 0, 1, 1)
            self.tintContentsContainerLayout.addWidget(self.tintPosition1, 1, 1, 1, 1)
            self.tintContentsContainerLayout.addItem(self.tintContentsPush2, 1, 2, 1, 1)
            self.tintContentsContainerLayout.addWidget(self.tintPosition2, 1, 3, 1, 1)
            self.tintContentsContainerLayout.addItem(self.tintContentsPush3, 1, 4, 1, 1)
            self.tintContentsContainerLayout.addLayout(self.tintPreviewContainerLayout1, 2, 1, 1, 1)
            self.tintContentsContainerLayout.addLayout(self.tintPreviewContainerLayout2, 2, 3, 1, 1)
            self.tintContentsContainerLayout.addItem(self.tintContentsPush5, 3, 2, 1, 1)
            self.tintContentsContainerLayout.addWidget(self.tintPosition3, 4, 1, 1, 1)
            self.tintContentsContainerLayout.addWidget(self.tintPosition4, 4, 3, 1, 1)
            self.tintContentsContainerLayout.addLayout(self.tintPreviewContainerLayout3, 5, 1, 1, 1)
            self.tintContentsContainerLayout.addLayout(self.tintPreviewContainerLayout4, 5, 3, 1, 1)
            self.tintContentsContainerLayout.addItem(self.tintContentsPush6, 6, 3, 1, 1)
            
            self.tintMenuContainer.setGeometry(QtCore.QRect(20, 83, 511, 50))
            self.tintFooterContainer.setGeometry(QtCore.QRect(15, 567, 830, 51))
            self.tintContentsContainer.setGeometry(QtCore.QRect(10, 230, 840, 340))
        
            #Adds the third page
            self.stackedWidget.addWidget(self.Tint)
            
            #Handles button clicks
            self.tintPrevious.clicked.connect(self.handleButtonPrev)
            self.tintCancel.clicked.connect(MainWindow.close)
            
            #Checks if you need the verify function yet. Hopefully not, because otherwise you're not on OB or KDE.... ;)
            if not nitrogenStatus and not plasmaStatus and not openboxStatus:
                self.tintMenuWallpapers.clicked.connect(self.handleButtonNextVerify)
                self.tintForward.clicked.connect(self.handleButtonNextVerify)
            else:
                self.tintMenuWallpapers.clicked.connect(self.handleButtonNext)
                self.tintForward.clicked.connect(self.handleButtonNext)
            
            #Sets text and translates widgets
            self.tintHeader.setText(_translate("MainWindow", "Tint 2"))
            self.tintMenu.setText(_translate("MainWindow", "Tint 2"))
            self.tintCancel.setText(_translate("MainWindow", "Cancel"))
            self.tintForward.setText(_translate("MainWindow", "Forward"))
            self.tintPrevious.setText(_translate("MainWindow", "Previous"))
            self.tintPositionDesc.setText(_translate("MainWindow", "Here you can choose what position you want of your Tint 2 panel."))
            self.tintPositionRadio1.setText(_translate("MainWindow", "Top"))
            self.tintPositionRadio2.setText(_translate("MainWindow", "Right"))
            self.tintPositionRadio3.setText(_translate("MainWindow", "Bottom"))
            self.tintPositionRadio4.setText(_translate("MainWindow", "Left"))
        
        if nitrogenStatus or plasmaStatus:
            #Starts code for fourth page
            self.Wallpaper = QtWidgets.QWidget()
            self.Wallpaper.setObjectName("Wallpaper")
            
            
            #defines all the widgets
            createStaticWidgets(self.Wallpaper)
            self.wallpaperHeader = QtWidgets.QLabel(self.Wallpaper)
            self.wallpaperMenuContainer = QtWidgets.QWidget(self.Wallpaper)
            self.wallpaperMenuContainerHLayout = QtWidgets.QHBoxLayout(self.wallpaperMenuContainer)
            self.wallpaperMenu = QtWidgets.QPushButton(self.wallpaperMenuContainer)
            self.wallpaperArrow = QtWidgets.QLabel(self.wallpaperMenuContainer)
            self.wallpaperMenuFinish = QtWidgets.QPushButton(self.wallpaperMenuContainer)
            self.wallpaperMenuSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperIcon = QtWidgets.QLabel(self.Wallpaper)
            self.wallpaperDesc = QtWidgets.QLabel(self.Wallpaper)
            self.wallpaperFooterContainer = QtWidgets.QWidget(self.Wallpaper)
            self.wallpaperFooterContainerHLayout = QtWidgets.QHBoxLayout(self.wallpaperFooterContainer)
            self.wallpaperPrevious = QtWidgets.QPushButton(self.wallpaperFooterContainer)
            self.wallpaperForward = QtWidgets.QPushButton(self.wallpaperFooterContainer)
            self.wallpaperCancel = QtWidgets.QPushButton(self.wallpaperFooterContainer)
            self.wallpaperFooterSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsContainer = QtWidgets.QWidget(self.Wallpaper)
            self.wallpaperContentsContainerLayout = QtWidgets.QGridLayout(self.wallpaperContentsContainer)
            self.wallpaperPreviewContainerLayout1 = QtWidgets.QHBoxLayout()
            self.wallpaperPreviewContainerLayout2 = QtWidgets.QHBoxLayout()
            self.wallpaperPreviewContainerLayout3 = QtWidgets.QHBoxLayout()
            self.wallpaperPreviewContainerLayout4 = QtWidgets.QHBoxLayout()
            self.wallpaperPreviewContainerLayout5 = QtWidgets.QHBoxLayout()
            self.wallpaperPreviewContainerLayout6 = QtWidgets.QHBoxLayout()
            self.wallpaperPreviewContainerLayout7 = QtWidgets.QHBoxLayout()
            self.wallpaperPreviewContainerLayout8 = QtWidgets.QHBoxLayout()
            self.wallpaper1 = QtWidgets.QLabel(self.wallpaperContentsContainer)
            self.wallpaper2 = QtWidgets.QLabel(self.wallpaperContentsContainer)
            self.wallpaper3 = QtWidgets.QLabel(self.wallpaperContentsContainer)
            self.wallpaper4 = QtWidgets.QLabel(self.wallpaperContentsContainer)
            self.wallpaper5 = QtWidgets.QLabel(self.wallpaperContentsContainer) 
            self.wallpaper6 = QtWidgets.QLabel(self.wallpaperContentsContainer)
            self.wallpaper7 = QtWidgets.QLabel(self.wallpaperContentsContainer)
            self.wallpaper8 = QtWidgets.QLabel(self.wallpaperContentsContainer)
            self.wallpaperChoice1 = QtWidgets.QRadioButton(self.wallpaperContentsContainer)
            self.wallpaperChoice2 = QtWidgets.QRadioButton(self.wallpaperContentsContainer)
            self.wallpaperChoice3 = QtWidgets.QRadioButton(self.wallpaperContentsContainer)
            self.wallpaperChoice4 = QtWidgets.QRadioButton(self.wallpaperContentsContainer)
            self.wallpaperChoice5 = QtWidgets.QRadioButton(self.wallpaperContentsContainer)
            self.wallpaperChoice6 = QtWidgets.QRadioButton(self.wallpaperContentsContainer)
            self.wallpaperChoice7 = QtWidgets.QRadioButton(self.wallpaperContentsContainer)
            self.wallpaperChoice8 = QtWidgets.QRadioButton(self.wallpaperContentsContainer)
            self.wallpaperContentsRadioPush1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsPush1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsPush2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsPush3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsPush4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsPush5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsPush6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.wallpaperContentsPush7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.wallpaperContentsPush8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            
            #Sets the wallpaper release specific wallpapers.
            if openboxStatus:
                releaseWallsOne = "/usr/share/turbulence/images/manjaro-grey/wallpapers/evodark.jpg"
                releaseWallsTwo = "/usr/share/turbulence/images/manjaro-grey/wallpapers/evolight.jpg"
                self.wallpaperChoice1.setText("Evolution Dark")
                self.wallpaperChoice2.setText("Evolution Light")
            elif kdeStatus:
                releaseWallsOne = "/usr/share/turbulence/images/manjaro-grey/wallpapers/manjarostyle.jpg"
                releaseWallsTwo = "/usr/share/turbulence/images/manjaro-grey/wallpapers/orangesplash.jpg"
                self.wallpaperChoice1.setText("Manjaro Style")
                self.wallpaperChoice2.setText("Orange Splash")
            else:
                releaseWallsOne = "/usr/share/turbulence/images/manjaro-grey/wallpapers/ozone.jpg"
                releaseWallsTwo = "/usr/share/turbulence/images/manjaro-grey/wallpapers/orangesplash.jpg"
                self.wallpaperChoice1.setText("Ozone")
                self.wallpaperChoice2.setText("Orange Splash")
                
            if openboxStatus:
                self.wallpaperMenuFinish.setText(_translate("MainWindow", "Packages"))
            else:
                self.wallpaperMenuFinish.setText(_translate("MainWindow", "Verify"))
            
            fourthPageWidgets = {
                "wallpaperHeader": [self.wallpaperHeader, 80, 20, 600, 51, "wallpaperHeader", None],
                "wallpaperIcon": [self.wallpaperIcon, 40, 160, 61, 61, "wallpaperIcon", "/usr/share/turbulence/images/manjaro-grey/wallpapers/wallpapers.png"],
                "wallpaperDesc": [self.wallpaperDesc, 110, 160, 591, 51, "wallpaperDesc", None],
                "wallpaperChoice1": [self.wallpaperChoice1, 70, 380, 81, 21, "wallpaperChoice1", None],
                "wallpaperChoice2": [self.wallpaperChoice2, 250, 380, 141, 21, "wallpaperChoice2", None],
                "wallpaperChoice3": [self.wallpaperChoice3, 480, 380, 131, 21, "wallpaperChoice3", None],
                "wallpaperChoice4": [self.wallpaperChoice4, 680, 380, 141, 21, "wallpaperChoice4", None],
                "wallpaperChoice5": [self.wallpaperChoice5, 70, 510, 81, 21, "wallpaperChoice5", None],
                "wallpaperChoice6": [self.wallpaperChoice6, 262, 510, 111, 21, "wallpaperChoice6", None],
                "wallpaperChoice7": [self.wallpaperChoice7, 477, 510, 131, 21, "wallpaperChoice7", None],
                "wallpaperChoice8": [self.wallpaperChoice8, 692, 510, 121, 21, "wallpaperChoice8", None]
            }

            fourthPageLayouts = {
                "wallpaperMenu": [self.wallpaperMenu, 0, 39, None, None, True, True, False, False],
                "wallpaperArrow": [self.wallpaperArrow, None, None, 21, 500, False, False, "/usr/share/turbulence/images/manjaro-grey/menu-arrow.png", False],
                "wallpaperMenuFinish": [self.wallpaperMenuFinish, 0, 39, None, None, True, True, False, False],
                "wallpaperForward": [self.wallpaperForward, 0, 34, None, None, True, True, False, False],
                "wallpaperPrevious": [self.wallpaperPrevious, 0, 34, None, None, True, True, False, False],
                "wallpaperCancel": [self.wallpaperCancel, 0, 34, None, None, True, True, False, False],
                "wallpaper1": [self.wallpaper1, None, None, None, None, False, False, releaseWallsOne, True],
                "wallpaper2": [self.wallpaper2, None, None, None, None, False, False, releaseWallsTwo, True],
                "wallpaper3": [self.wallpaper3, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/wallpapers/sunsetplane.jpg", True],
                "wallpaper4": [self.wallpaper4, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/wallpapers/mountainlake.jpg", True],
                "wallpaper5": [self.wallpaper5, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/wallpapers/earthinspace.jpg", True],
                "wallpaper6": [self.wallpaper6, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/wallpapers/darkstairs.jpg", True],
                "wallpaper7": [self.wallpaper7, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/wallpapers/cherryjapan.jpg", True],
                "wallpaper8": [self.wallpaper8, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/wallpapers/whitetiger.jpg", True],
                "wallpaperChoice1": [self.wallpaperChoice1, None, None, None, None, False, False, False, False],
                "wallpaperChoice2": [self.wallpaperChoice2, None, None, None, None, False, False, False, False],
                "wallpaperChoice3": [self.wallpaperChoice3, None, None, None, None, False, False, False, False],
                "wallpaperChoice4": [self.wallpaperChoice4, None, None, None, None, False, False, False, False],
                "wallpaperChoice5": [self.wallpaperChoice5, None, None, None, None, False, False, False, False],
                "wallpaperChoice6": [self.wallpaperChoice6, None, None, None, None, False, False, False, False],
                "wallpaperChoice7": [self.wallpaperChoice7, None, None, None, None, False, False, False, False],
                "wallpaperChoice8": [self.wallpaperChoice8, None, None, None, None, False, False, False, False]
            }

            #defines all the widget parameters
            for widgetName, widgetSettings in fourthPageWidgets.items():
                widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
            
            for widgetName, widgetSettings in fourthPageLayouts.items():
                layoutConfigurer(widgetName, widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6], widgetSettings[7], widgetSettings[8])
            
            #Defines all the custom settings.
            self.wallpaperPrevious.setIcon(previousIcon)
            self.wallpaperForward.setIcon(forwardIcon)
            self.wallpaperCancel.setIcon(cancelIcon)
            self.wallpaperPrevious.setIconSize(QtCore.QSize(28, 30))
            self.wallpaperForward.setIconSize(QtCore.QSize(28, 30))
            self.wallpaperCancel.setIconSize(QtCore.QSize(16, 16))
            
            self.wallpaperDesc.setWordWrap(True)
            
            #Sets the default item
            self.wallpaperChoice1.setChecked(True)
            
            self.wallpaperMenuContainerHLayout.addWidget(self.wallpaperMenu)
            self.wallpaperMenuContainerHLayout.addWidget(self.wallpaperArrow)
            self.wallpaperMenuContainerHLayout.addWidget(self.wallpaperMenuFinish)
            self.wallpaperMenuContainerHLayout.addItem(self.wallpaperMenuSpacer)
            
            self.wallpaperFooterContainerHLayout.addWidget(self.wallpaperCancel)
            self.wallpaperFooterContainerHLayout.addItem(self.wallpaperFooterSpacer)
            self.wallpaperFooterContainerHLayout.addWidget(self.wallpaperPrevious)
            self.wallpaperFooterContainerHLayout.addWidget(self.wallpaperForward)
            
            self.wallpaperPreviewContainerLayout1.addItem(self.wallpaperContentsRadioPush1)
            self.wallpaperPreviewContainerLayout1.addWidget(self.wallpaperChoice1)
            self.wallpaperPreviewContainerLayout1.addItem(self.wallpaperContentsRadioPush2)
            self.wallpaperPreviewContainerLayout2.addItem(self.wallpaperContentsRadioPush3)
            self.wallpaperPreviewContainerLayout2.addWidget(self.wallpaperChoice2)
            self.wallpaperPreviewContainerLayout2.addItem(self.wallpaperContentsRadioPush4)
            self.wallpaperPreviewContainerLayout3.addItem(self.wallpaperContentsRadioPush5)
            self.wallpaperPreviewContainerLayout3.addWidget(self.wallpaperChoice3)
            self.wallpaperPreviewContainerLayout3.addItem(self.wallpaperContentsRadioPush6)
            self.wallpaperPreviewContainerLayout4.addItem(self.wallpaperContentsRadioPush7)
            self.wallpaperPreviewContainerLayout4.addWidget(self.wallpaperChoice4)
            self.wallpaperPreviewContainerLayout4.addItem(self.wallpaperContentsRadioPush8)
            self.wallpaperPreviewContainerLayout5.addItem(self.wallpaperContentsRadioPush9)
            self.wallpaperPreviewContainerLayout5.addWidget(self.wallpaperChoice5)
            self.wallpaperPreviewContainerLayout5.addItem(self.wallpaperContentsRadioPush10)
            self.wallpaperPreviewContainerLayout6.addItem(self.wallpaperContentsRadioPush11)
            self.wallpaperPreviewContainerLayout6.addWidget(self.wallpaperChoice6)
            self.wallpaperPreviewContainerLayout6.addItem(self.wallpaperContentsRadioPush12)
            self.wallpaperPreviewContainerLayout7.addItem(self.wallpaperContentsRadioPush13)
            self.wallpaperPreviewContainerLayout7.addWidget(self.wallpaperChoice7)
            self.wallpaperPreviewContainerLayout7.addItem(self.wallpaperContentsRadioPush14)
            self.wallpaperPreviewContainerLayout8.addItem(self.wallpaperContentsRadioPush15)
            self.wallpaperPreviewContainerLayout8.addWidget(self.wallpaperChoice8)
            self.wallpaperPreviewContainerLayout8.addItem(self.wallpaperContentsRadioPush16)
            
            self.wallpaperContentsContainerLayout.addItem(self.wallpaperContentsPush6, 0, 3, 1, 1)
            self.wallpaperContentsContainerLayout.addItem(self.wallpaperContentsPush1, 1, 0, 1, 1)
            self.wallpaperContentsContainerLayout.addWidget(self.wallpaper1, 1, 1, 1, 1)
            self.wallpaperContentsContainerLayout.addItem(self.wallpaperContentsPush2, 1, 2, 1, 1)
            self.wallpaperContentsContainerLayout.addWidget(self.wallpaper2, 1, 3, 1, 1)
            self.wallpaperContentsContainerLayout.addItem(self.wallpaperContentsPush3, 1, 4, 1, 1)
            self.wallpaperContentsContainerLayout.addWidget(self.wallpaper3, 1, 5, 1, 1)
            self.wallpaperContentsContainerLayout.addItem(self.wallpaperContentsPush4, 1, 6, 1, 1)
            self.wallpaperContentsContainerLayout.addWidget(self.wallpaper4, 1, 7, 1, 1)
            self.wallpaperContentsContainerLayout.addItem(self.wallpaperContentsPush5, 1, 8, 1, 1)
            self.wallpaperContentsContainerLayout.addLayout(self.wallpaperPreviewContainerLayout1, 2, 1, 1, 1)
            self.wallpaperContentsContainerLayout.addLayout(self.wallpaperPreviewContainerLayout2, 2, 3, 1, 1)
            self.wallpaperContentsContainerLayout.addLayout(self.wallpaperPreviewContainerLayout3, 2, 5, 1, 1)
            self.wallpaperContentsContainerLayout.addLayout(self.wallpaperPreviewContainerLayout4, 2, 7, 1, 1)
            self.wallpaperContentsContainerLayout.addItem(self.wallpaperContentsPush7, 3, 2, 1, 1)
            self.wallpaperContentsContainerLayout.addWidget(self.wallpaper5, 4, 1, 1, 1)
            self.wallpaperContentsContainerLayout.addWidget(self.wallpaper6, 4, 3, 1, 1)
            self.wallpaperContentsContainerLayout.addWidget(self.wallpaper7, 4, 5, 1, 1)
            self.wallpaperContentsContainerLayout.addWidget(self.wallpaper8, 4, 7, 1, 1)
            self.wallpaperContentsContainerLayout.addLayout(self.wallpaperPreviewContainerLayout5, 5, 1, 1, 1)
            self.wallpaperContentsContainerLayout.addLayout(self.wallpaperPreviewContainerLayout6, 5, 3, 1, 1)
            self.wallpaperContentsContainerLayout.addLayout(self.wallpaperPreviewContainerLayout7, 5, 5, 1, 1)
            self.wallpaperContentsContainerLayout.addLayout(self.wallpaperPreviewContainerLayout8, 5, 7, 1, 1)
            self.wallpaperContentsContainerLayout.addItem(self.wallpaperContentsPush8, 6, 3, 1, 1)
            
            self.wallpaperMenuContainer.setGeometry(QtCore.QRect(20, 83, 511, 50))
            self.wallpaperFooterContainer.setGeometry(QtCore.QRect(15, 567, 830, 51))
            self.wallpaperContentsContainer.setGeometry(QtCore.QRect(10, 230, 840, 340))
            
            self.stackedWidget.addWidget(self.Wallpaper)
            
            #Handles the button clicks
            self.wallpaperCancel.clicked.connect(MainWindow.close)
            self.wallpaperPrevious.clicked.connect(self.handleButtonPrev)
            
            #Checks if you need the verify function yet. Hopefully not, because otherwise you're not on OB or KDE.... ;)
            if not openboxStatus:
                self.wallpaperMenuFinish.clicked.connect(self.handleButtonNextVerify)
                self.wallpaperForward.clicked.connect(self.handleButtonNextVerify)
            else:
                self.wallpaperMenuFinish.clicked.connect(self.handleButtonNext)
                self.wallpaperForward.clicked.connect(self.handleButtonNext)
       
            #Sets text, or translates widgets
            self.wallpaperHeader.setText(_translate("MainWindow", "Wallpapers"))
            self.wallpaperMenu.setText(_translate("MainWindow", "Wallpapers"))
            self.wallpaperDesc.setText(_translate("MainWindow", "Here you can set which wallpaper you want."))
            self.wallpaperPrevious.setText(_translate("MainWindow", "Previous"))
            self.wallpaperForward.setText(_translate("MainWindow", "Forward"))
            self.wallpaperCancel.setText(_translate("MainWindow", "Cancel"))
            self.wallpaperChoice3.setText("Sunset Plane")
            self.wallpaperChoice4.setText("Mountain Lake")
            self.wallpaperChoice5.setText("Space")
            self.wallpaperChoice6.setText("Dark Stairs")
            self.wallpaperChoice7.setText("Cherry Japan")
            self.wallpaperChoice8.setText("Snow Leopard")
        
        
        if openboxStatus:
            #Adds the sixth page.
            self.Packages = QtWidgets.QWidget()
            self.Packages.setObjectName("Packages")
        
            #Creates all the widgets
            createStaticWidgets(self.Packages)
            
            self.packagesHeader = QtWidgets.QLabel(self.Packages)
            self.packagesMenuContainer = QtWidgets.QWidget(self.Packages)
            self.packagesMenuContainerHLayout = QtWidgets.QHBoxLayout(self.packagesMenuContainer)
            self.packagesMenu = QtWidgets.QPushButton(self.packagesMenuContainer)
            self.packagesArrow = QtWidgets.QLabel(self.packagesMenuContainer)
            self.packagesMenuFinish = QtWidgets.QPushButton(self.packagesMenuContainer)
            self.packagesMenuSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.packagesIcon = QtWidgets.QLabel(self.Packages)
            self.packagesDesc = QtWidgets.QLabel(self.Packages)
            self.packagesFooterContainer = QtWidgets.QWidget(self.Packages)
            self.packagesFooterContainerHLayout = QtWidgets.QHBoxLayout(self.packagesFooterContainer)
            self.packagesPrevious = QtWidgets.QPushButton(self.Packages)
            self.packagesForward = QtWidgets.QPushButton(self.Packages)
            self.packagesCancel = QtWidgets.QPushButton(self.Packages)
            self.packagesFooterSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.packagesTabs = QtWidgets.QTabWidget(self.Packages)
            
            self.packagesNetwork = QtWidgets.QWidget()
            self.packagesNetworkBack = QtWidgets.QLabel(self.packagesNetwork)
            self.packagesChromiumPic = QtWidgets.QLabel(self.packagesNetwork)
            self.packagesChromiumCheck = QtWidgets.QCheckBox(self.packagesNetwork)
            self.packagesDelugePic = QtWidgets.QLabel(self.packagesNetwork)
            self.packagesDelugeCheck = QtWidgets.QCheckBox(self.packagesNetwork)
            self.packagesEkigaPic = QtWidgets.QLabel(self.packagesNetwork)
            self.packagesEkigaCheck = QtWidgets.QCheckBox(self.packagesNetwork)
            self.packagesFilezillaPic = QtWidgets.QLabel(self.packagesNetwork)
            self.packagesFilezillaCheck = QtWidgets.QCheckBox(self.packagesNetwork)
            self.packagesFirefoxPic = QtWidgets.QLabel(self.packagesNetwork)
            self.packagesFirefoxCheck = QtWidgets.QCheckBox(self.packagesNetwork)
            self.packagesMidoriPic = QtWidgets.QLabel(self.packagesNetwork)
            self.packagesMidoriCheck = QtWidgets.QCheckBox(self.packagesNetwork)
            self.packagesOperaPic = QtWidgets.QLabel(self.packagesNetwork)
            self.packagesOperaCheck = QtWidgets.QCheckBox(self.packagesNetwork)
            self.packagesQbittorrentPic = QtWidgets.QLabel(self.packagesNetwork)
            self.packagesQbittorrentCheck = QtWidgets.QCheckBox(self.packagesNetwork)
            self.packagesThunderbirdPic = QtWidgets.QLabel(self.packagesNetwork)
            self.packagesThunderbirdCheck = QtWidgets.QCheckBox(self.packagesNetwork)
            self.packagesTransmissionPic = QtWidgets.QLabel(self.packagesNetwork)
            self.packagesTransmissionCheck = QtWidgets.QCheckBox(self.packagesNetwork)
            self.packagesNotActive = QtWidgets.QLabel(self.packagesNetwork)
            
            self.packagesMultimedia = QtWidgets.QWidget()
            self.packagesMultimediaBack = QtWidgets.QLabel(self.packagesMultimedia)
            self.packagesAudaciousPic = QtWidgets.QLabel(self.packagesMultimedia)
            self.packagesAudaciousCheck = QtWidgets.QCheckBox(self.packagesMultimedia)
            self.packagesClemetinePic = QtWidgets.QLabel(self.packagesMultimedia)
            self.packagesClementineCheck = QtWidgets.QCheckBox(self.packagesMultimedia)
            self.packagesDeadbeefPic = QtWidgets.QLabel(self.packagesMultimedia)
            self.packagesDeadbeefCheck = QtWidgets.QCheckBox(self.packagesMultimedia)
            self.packagesSmplayerPic = QtWidgets.QLabel(self.packagesMultimedia)
            self.packagesSmplayerCheck = QtWidgets.QCheckBox(self.packagesMultimedia)
            self.packagesVlcPic = QtWidgets.QLabel(self.packagesMultimedia)
            self.packagesVlcCheck = QtWidgets.QCheckBox(self.packagesMultimedia)
            
            self.packagesGraphics = QtWidgets.QWidget()
            self.packagesGraphicsBack = QtWidgets.QLabel(self.packagesGraphics)
            self.packagesBlenderPic = QtWidgets.QLabel(self.packagesGraphics)
            self.packagesBlenderCheck = QtWidgets.QCheckBox(self.packagesGraphics)
            self.packagesEvincePic = QtWidgets.QLabel(self.packagesGraphics)
            self.packagesEvinceCheck = QtWidgets.QCheckBox(self.packagesGraphics)
            self.packagesGimpPic = QtWidgets.QLabel(self.packagesGraphics)
            self.packagesGimpCheck = QtWidgets.QCheckBox(self.packagesGraphics)
            self.packagesGpicviewPic = QtWidgets.QLabel(self.packagesGraphics)
            self.packagesGpicviewCheck = QtWidgets.QCheckBox(self.packagesGraphics)
            self.packagesPintaPic = QtWidgets.QLabel(self.packagesGraphics)
            self.packagesPintaCheck = QtWidgets.QCheckBox(self.packagesGraphics)
            self.packagesViewniorPic = QtWidgets.QLabel(self.packagesGraphics)
            self.packagesViewniorCheck = QtWidgets.QCheckBox(self.packagesGraphics)
            
            self.packagesAccessories = QtWidgets.QWidget()
            self.packagesAccessoriesBack = QtWidgets.QLabel(self.packagesAccessories)
            self.packagesGeanyPic = QtWidgets.QLabel(self.packagesAccessories)
            self.packagesGeanyCheck = QtWidgets.QCheckBox(self.packagesAccessories)
            self.packagesHexchatPic = QtWidgets.QLabel(self.packagesAccessories)
            self.packagesHexchatCheck = QtWidgets.QCheckBox(self.packagesAccessories)
            self.packagesLeafpadPic = QtWidgets.QLabel(self.packagesAccessories)
            self.packagesLeafpadCheck = QtWidgets.QCheckBox(self.packagesAccessories)
            self.packagesOctopiPic = QtWidgets.QLabel(self.packagesAccessories)
            self.packagesOctopiCheck = QtWidgets.QCheckBox(self.packagesAccessories)
            self.packagesPamacPic = QtWidgets.QLabel(self.packagesAccessories)
            self.packagesPamacCheck = QtWidgets.QCheckBox(self.packagesAccessories)
            self.packagesPcmanfmPic = QtWidgets.QLabel(self.packagesAccessories)
            self.packagesPcmanfmCheck = QtWidgets.QCheckBox(self.packagesAccessories)
            self.packagesSpacefmPic = QtWidgets.QLabel(self.packagesAccessories)
            self.packagesSpacefmCheck = QtWidgets.QCheckBox(self.packagesAccessories)
            self.packagesTerminatorPic = QtWidgets.QLabel(self.packagesAccessories)
            self.packagesTerminatorCheck = QtWidgets.QCheckBox(self.packagesAccessories)
            self.packagesThunarPic = QtWidgets.QLabel(self.packagesAccessories)
            self.packagesThunarCheck = QtWidgets.QCheckBox(self.packagesAccessories)
            
            self.packagesExtras = QtWidgets.QWidget()
            self.packagesExtrasBack = QtWidgets.QLabel(self.packagesExtras)
            self.packagesAurSupportPic = QtWidgets.QLabel(self.packagesExtras)
            self.packagesAurSupportCheck = QtWidgets.QCheckBox(self.packagesExtras)
            self.packagesLibreOfficeInstallerPic = QtWidgets.QLabel(self.packagesExtras)
            self.packagesLibreOfficeInstallerCheck = QtWidgets.QCheckBox(self.packagesExtras)
            self.packagesMultimediaSupportPic = QtWidgets.QLabel(self.packagesExtras)
            self.packagesMultimediaSupportCheck = QtWidgets.QCheckBox(self.packagesExtras)
            self.packagesPrinterSupportPic = QtWidgets.QLabel(self.packagesExtras)
            self.packagesPrinterSupportCheck = QtWidgets.QCheckBox(self.packagesExtras)
            self.packagesCheckConnection = QtWidgets.QPushButton(self.Packages)
        
            #This is set to false by default, but it will changed different later.
            self.internetAccess = False

            #########################################################
            #Coordinates for the 12 different items. Haven't gotten #
            #Around to adding layouts yet, so gots to do it this    #
            #way. :-(                                               #
            #########################################################
            #    #        Picture              Checkmark            #                  
            #  1 #     20, 10, 71, 71       10, 80, 111, 31         #
            #  2 #     140, 10, 71, 71      130, 80, 111, 31        #
            #  3 #     270, 10, 71, 71      260, 80, 111, 31        #   
            #  4 #     400, 10, 71, 71      390, 80, 111, 31        #   
            #  5 #     520, 10, 71, 71      510, 80, 111, 31        #   
            #  6 #     640, 10, 71, 71      630, 80, 111, 31        #   
            #  7 #     20, 110, 71, 71      10, 180, 111, 31        #   
            #  8 #     140, 110, 71, 71     130, 180, 111, 31       #   
            #  9 #     270, 110, 71, 71     260, 180, 111, 31       #   
            # 10 #     400, 110, 71, 71     390, 180, 111, 31       #   
            # 11 #     520, 110, 71, 71     510, 180, 111, 31       #   
            # 12 #     640, 110, 71, 71     630, 180, 111, 31       #   
            #########################################################
            
            fifthPageWidgets = {
                "packagesHeader": [self.packagesHeader, 80, 20, 600, 51, "packagesHeader", None],
                "packagesIcon": [self.packagesIcon, 40, 160, 61, 61, "packagesIcon", "/usr/share/turbulence/images/manjaro-grey/packages/packagesicon.png"],
                "packagesDesc": [self.packagesDesc, 110, 140, 650, 100, "packagesDesc", None],
                "packagesTabs": [self.packagesTabs, 60, 290, 741, 251, "packagesTabs", None],
                
                "packagesNetworkBack": [self.packagesNetworkBack, -14, -7, 761, 241, "packagesNetworkBack", "/usr/share/turbulence/images/manjaro-grey/packages/packages-back.png"],
                "packagesChromiumPic": [self.packagesChromiumPic, 20, 10, 71, 71, "packagesChromiumPic", "/usr/share/turbulence/images/manjaro-grey/packages/network/chromium.png"],
                "packagesChromiumCheck": [self.packagesChromiumCheck, 10, 80, 111, 31, "packagesChromiumCheck", None],
                "packagesDelugePic": [self.packagesDelugePic, 140, 10, 71, 71, "packagesDelugePic", "/usr/share/turbulence/images/manjaro-grey/packages/network/deluge.png"],
                "packagesDelugeCheck": [self.packagesDelugeCheck, 130, 80, 111, 31, "packagesDelugeCheck", None],
                "packagesEkigaPic": [self.packagesEkigaPic, 270, 10, 71, 71, "packagesEkigaPic", "/usr/share/turbulence/images/manjaro-grey/packages/network/ekiga.png"],
                "packagesEkigaCheck": [self.packagesEkigaCheck, 260, 80, 102, 31, "packagesEkigaCheck", None],
                "packagesFilezillaPic": [self.packagesFilezillaPic, 400, 10, 71, 71, "packagesFilezillaPic", "/usr/share/turbulence/images/manjaro-grey/packages/network/filezilla.png"],
                "packagesFilezillaCheck": [self.packagesFilezillaCheck, 390, 80, 111, 31, "packagesFilezillaCheck", None],
                "packagesFirefoxPic": [self.packagesFirefoxPic, 520, 10, 71, 71, "packagesFirefoxPic", "/usr/share/turbulence/images/manjaro-grey/packages/network/firefox.png"],
                "packagesFirefoxCheck": [self.packagesFirefoxCheck, 510, 80, 111, 31, "packagesFirefoxCheck", None],
                "packagesMidoriPic": [self.packagesMidoriPic, 640, 10, 71, 71, "packagesMidoriPic", "/usr/share/turbulence/images/manjaro-grey/packages/network/midori.png"],
                "packagesMidoriCheck": [self.packagesMidoriCheck, 630, 80, 111, 31, "packagesMidoriCheck", None],
                "packagesOperaPic": [self.packagesOperaPic, 20, 110, 71, 71, "packagesOperaPic", "/usr/share/turbulence/images/manjaro-grey/packages/network/opera.png"],
                "packagesOperaCheck": [self.packagesOperaCheck, 10, 180, 111, 31, "packagesOperaCheck", None],
                "packagesQbittorrentPic": [self.packagesQbittorrentPic, 140, 110, 71, 71, "packagesQbittorrentPic", "/usr/share/turbulence/images/manjaro-grey/packages/network/qbittorrent.png"],
                "packagesQbittorrentCheck": [self.packagesQbittorrentCheck, 130, 180, 111, 31, "packagesQbittorrentCheck", None],
                "packagesThunderbirdPic": [self.packagesThunderbirdPic, 270, 110, 71, 71, "packagesThunderbirdPic", "/usr/share/turbulence/images/manjaro-grey/packages/network/thunderbird.png"],
                "packagesThunderbirdCheck": [self.packagesThunderbirdCheck, 260, 180, 120, 31, "packagesThunderbirdCheck", None],
                "packagesTransmissionPic": [self.packagesTransmissionPic, 400, 110, 71, 71, "packagesTransmissionPic", "/usr/share/turbulence/images/manjaro-grey/packages/network/transmission.png"],
                "packagesTransmissionCheck": [self.packagesTransmissionCheck, 390, 180, 121, 31, "packagesTransmissionCheck", None],
                
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
                "packagesPintaPic": [self.packagesPintaPic, 520, 10, 71, 71, "packagesPintaPic", "/usr/share/turbulence/images/manjaro-grey/packages/graphics/pinta.png"],
                "packagesPintaCheck": [self.packagesPintaCheck, 510, 80, 111, 31, "packagesPintaCheck", None],
                "packagesViewniorPic": [self.packagesViewniorPic, 640, 10, 71, 71, "packagesViewniorPic", "/usr/share/turbulence/images/manjaro-grey/packages/graphics/viewnior.png"],
                "packagesViewniorCheck": [self.packagesViewniorCheck, 630, 80, 111, 31, "packagesViewniorCheck", None],
                
                "packagesAccessoriesBack": [self.packagesAccessoriesBack, -20, -10, 761, 241, "packagesAccessoriesBack", "/usr/share/turbulence/images/manjaro-grey/packages/packages-back.png"],
                "packagesGeanyPic": [self.packagesGeanyPic, 20, 10, 71, 71, "packagesGeanyPic", "/usr/share/turbulence/images/manjaro-grey/packages/accessories/geany.png"],
                "packagesGeanyCheck": [self.packagesGeanyCheck, 10, 80, 111, 31, "packagesGeanyCheck", None],
                "packagesHexchatPic": [self.packagesHexchatPic, 140, 10, 71, 71, "packagesHexchatPic", "/usr/share/turbulence/images/manjaro-grey/packages/accessories/hexchat.png"],
                "packagesHexchatCheck": [self.packagesHexchatCheck, 130, 80, 111, 31, "packagesHexchatCheck", None],
                "packagesLeafpadPic": [self.packagesLeafpadPic, 270, 10, 71, 71, "packagesLeafpadPic", "/usr/share/turbulence/images/manjaro-grey/packages/accessories/leafpad.png"],
                "packagesLeafpadCheck": [self.packagesLeafpadCheck, 260, 80, 111, 31, "packagesLeafpadCheck", None],
                "packagesOctopiPic": [self.packagesOctopiPic, 400, 10, 71, 71, "packagesOctopiPic", "/usr/share/turbulence/images/manjaro-grey/packages/accessories/octopi.png"],
                "packagesOctopiCheck": [self.packagesOctopiCheck, 390, 80, 111, 31, "packagesOctopiCheck", None],
                "packagesPamacPic": [self.packagesPamacPic, 520, 10, 71, 71, "packagesPamacPic", "/usr/share/turbulence/images/manjaro-grey/packages/accessories/pamac.png"],
                "packagesPamacCheck": [self.packagesPamacCheck, 510, 80, 111, 31, "packagesPamacCheck", None],
                "packagesPcmanfmPic": [self.packagesPcmanfmPic, 640, 10, 71, 71, "packagesPcmanfmPic", "/usr/share/turbulence/images/manjaro-grey/packages/accessories/pcmanfm.png"],
                "packagesPcmanfmCheck": [self.packagesPcmanfmCheck, 630, 80, 111, 31, "packagesPcmanfmCheck", None],
                "packagesSpacefmPic": [self.packagesSpacefmPic, 20, 110, 71, 71, "packagesSpacefmPic", "/usr/share/turbulence/images/manjaro-grey/packages/accessories/spacefm.png"],
                "packagesSpacefmCheck": [self.packagesSpacefmCheck, 10, 180, 111, 31, "packagesSpacefmCheck", None],
                "packagesTerminatorPic": [self.packagesTerminatorPic, 140, 110, 71, 71, "packagesTerminatorPic", "/usr/share/turbulence/images/manjaro-grey/packages/accessories/terminator.png"],
                "packagesTerminatorCheck": [self.packagesTerminatorCheck, 130, 180, 111, 31, "packagesTerminatorCheck", None],
                "packagesThunarPic": [self.packagesThunarPic, 270, 110, 71, 71, "packagesThunarPic" , "/usr/share/turbulence/images/manjaro-grey/packages/accessories/thunar.png"],
                "packagesThunarCheck": [self.packagesThunarCheck, 260, 180, 111, 31, "packagesThunarCheck", None],
                
                "packagesExtrasBack": [self.packagesExtrasBack, -20, -10, 761, 241, "packagesExtrasBack", "/usr/share/turbulence/images/manjaro-grey/packages/packages-back.png"],
                "packagesAurSupportPic": [self.packagesAurSupportPic, 20, 10, 71, 71, "packagesAurSupportPic" , "/usr/share/turbulence/images/manjaro-grey/packages/extras/aursupport.png"],
                "packagesAurSupportCheck": [self.packagesAurSupportCheck, 10, 90, 111, 41, "packagesAurSupportCheck", None],
                "packagesLibreOfficeInstallerPic": [self.packagesLibreOfficeInstallerPic, 140, 10, 71, 71, "packagesLibreOfficeInstallerPic", "/usr/share/turbulence/images/manjaro-grey/packages/extras/libreofficeinstaller.png"],
                "packagesLibreOfficeInstallerCheck": [self.packagesLibreOfficeInstallerCheck, 130, 90, 111, 41, "packagesLibreOfficeInstallerCheck", None],
                "packagesMultimediaSupportPic": [self.packagesMultimediaSupportPic, 270, 10, 71, 71, "packagesMultimediaSupportPic" , "/usr/share/turbulence/images/manjaro-grey/packages/extras/multimediasupport.png"],
                "packagesMultimediaSupportCheck": [self.packagesMultimediaSupportCheck, 260, 90, 111, 41, "packagesMultimediaSupportCheck", None],
                "packagesPrinterSupportPic": [self.packagesPrinterSupportPic, 400, 10, 71, 71, "packagesPrinterSupportPic" , "/usr/share/turbulence/images/manjaro-grey/packages/extras/printersupport.png"],
                "packagesPrinterSupportCheck": [self.packagesPrinterSupportCheck, 390, 90, 111, 41, "packagesPrinterSupportCheck", None],
                
                "packagesCheckConnection": [self.packagesCheckConnection, 160, 400, 550, 60, "packagesCheckConnection", None] 
            }
            
            fifthPageLayouts = {
                "packagesMenu": [self.packagesMenu, 0, 39, None, None, True, True, False],
                "packagesArrow": [self.packagesArrow, None, None, 21, 500, False, False, "/usr/share/turbulence/images/manjaro-grey/menu-arrow.png"],
                "packagesMenuFinish": [self.packagesMenuFinish, 0, 39, None, None, True, True, False],
                "packagesForward": [self.packagesForward, 0, 34, None, None, True, True, False],
                "packagesPrevious": [self.packagesPrevious, 0, 34, None, None, True, True, False],
                "packagesCancel": [self.packagesCancel, 0, 34, None, None, True, True, False]
            }

            #defines all the widget parameters
            for widgetName, widgetSettings in fifthPageWidgets.items():
                widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
        
            for widgetName, widgetSettings in fifthPageLayouts.items():
                layoutConfigurer(widgetName, widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6], widgetSettings[7])
            
            self.internetAccess = False #This is the default. It will be changed to true if the user has an internet connection

            #Adds any custom widgets.
            self.packagesPrevious.setFlat(True)
            self.packagesForward.setFlat(True)
            self.packagesCancel.setFlat(True)
            self.packagesCheckConnection.setFlat(True)
            
            self.packagesDesc.setWordWrap(True)
        
            self.packagesPrevious.setFocusPolicy(QtCore.Qt.NoFocus)
            self.packagesForward.setFocusPolicy(QtCore.Qt.NoFocus)
            self.packagesCancel.setFocusPolicy(QtCore.Qt.NoFocus)
            self.packagesCheckConnection.setFocusPolicy(QtCore.Qt.NoFocus)
        
            self.packagesPrevious.setIcon(previousIcon)
            self.packagesForward.setIcon(forwardIcon)
            self.packagesCancel.setIcon(cancelIcon)
            self.packagesPrevious.setIconSize(QtCore.QSize(28, 30))
            self.packagesForward.setIconSize(QtCore.QSize(28, 30))
            self.packagesCancel.setIconSize(QtCore.QSize(16, 16))
         
            self.packagesNetwork.setObjectName("Network")
            self.packagesMultimedia.setObjectName("Multimedia")
            self.packagesGraphics.setObjectName("Graphics")
            self.packagesAccessories.setObjectName("Accessories")
            self.packagesExtras.setObjectName("Extras")
        
            self.packagesTabs.addTab(self.packagesNetwork, "")
            self.packagesTabs.addTab(self.packagesMultimedia, "")
            self.packagesTabs.addTab(self.packagesGraphics, "")
            self.packagesTabs.addTab(self.packagesAccessories, "")
            self.packagesTabs.addTab(self.packagesExtras, "")
            
            self.packagesMenuContainerHLayout.addWidget(self.packagesMenu)
            self.packagesMenuContainerHLayout.addWidget(self.packagesArrow)
            self.packagesMenuContainerHLayout.addWidget(self.packagesMenuFinish)
            self.packagesMenuContainerHLayout.addItem(self.packagesMenuSpacer)
            
            self.packagesFooterContainerHLayout.addWidget(self.packagesCancel)
            self.packagesFooterContainerHLayout.addItem(self.packagesFooterSpacer)
            self.packagesFooterContainerHLayout.addWidget(self.packagesPrevious)
            self.packagesFooterContainerHLayout.addWidget(self.packagesForward)
            
            self.packagesMenuContainer.setGeometry(QtCore.QRect(20, 83, 511, 50))
            self.packagesFooterContainer.setGeometry(QtCore.QRect(15, 567, 830, 51))
        
            self.packagesTabs.tabBar().setEnabled(False)
            self.stackedWidget.addWidget(self.Packages)
            
            #Handles button clicks
            self.packagesCancel.clicked.connect(MainWindow.close)
            self.packagesPrevious.clicked.connect(self.handleButtonPrev)
            self.packagesForward.clicked.connect(self.handleButtonNextVerify)
            self.packagesMenuFinish.clicked.connect(self.handleButtonNextVerify)
            self.packagesCheckConnection.clicked.connect(self.checkInternetStatus)
            
            #Fifth page            
            self.packagesHeader.setText(_translate("MainWindow", "Packages"))
            self.packagesMenu.setText(_translate("MainWindow", "Packages"))
            self.packagesMenuFinish.setText(_translate("MainWindow", "Verify"))
            self.packagesDesc.setText(_translate("MainWindow", "Here, you can choose what packages you would like to install. Hover over any of the packages to see a description, and select or deselect any packages you want to add or remove. Packages that are installed will be auto-selected."))
            self.packagesPrevious.setText(_translate("MainWindow", "Previous"))
            self.packagesForward.setText(_translate("MainWindow", "Forward"))
            self.packagesCancel.setText(_translate("MainWindow", "Cancel"))
            self.packagesCheckConnection.setText(_translate("MainWindow", "Check For Internet Connection"))
            
            self.packagesTabs.setTabText(self.packagesTabs.indexOf(self.packagesNetwork), _translate("MainWindow", "Network"))
            self.packagesChromiumPic.setToolTip(_translate("MainWindow", "The open-source project behind Google Chrome, an \n" "attempt at creating a safer, faster, and more stable browser"))
            self.packagesChromiumCheck.setText("Chomium")
            self.packagesDelugePic.setToolTip(_translate("MainWindow", "A BitTorrent client with multiple user interfaces \n" "in a client/server model"))
            self.packagesDelugeCheck.setText("Deluge")
            self.packagesEkigaPic.setToolTip(_translate("MainWindow", "VOIP/Videoconferencing app with full SIP and H.323 support"))
            self.packagesEkigaCheck.setText("Ekiga")
            self.packagesFilezillaPic.setToolTip(_translate("MainWindow", "Fast and reliable FTP, FTPS and SFTP client"))
            self.packagesFilezillaCheck.setText("Filezilla")
            self.packagesFirefoxPic.setToolTip(_translate("MainWindow", "Standalone web browser from mozilla.org"))
            self.packagesFirefoxCheck.setText("Firefox")
            self.packagesMidoriPic.setToolTip(_translate("MainWindow", "Lightweight web browser (GTK2)"))
            self.packagesMidoriCheck.setText("Midori")
            self.packagesOperaPic.setToolTip(_translate("MainWindow", "Fast and secure web browser and Internet suite"))
            self.packagesOperaCheck.setText("Opera")
            self.packagesQbittorrentPic.setToolTip(_translate("MainWindow", "A bittorrent client written in C++ / Qt4 using the good \n" "libtorrent library"))
            self.packagesQbittorrentCheck.setText("QBittorrent")
            self.packagesThunderbirdPic.setToolTip(_translate("MainWindow", "Standalone Mail/News reader"))
            self.packagesThunderbirdCheck.setText("Thunderbird")
            self.packagesTransmissionPic.setToolTip(_translate("MainWindow", "Fast, easy, and free BitTorrent client"))
            self.packagesTransmissionCheck.setText("Transmission")
            
            self.packagesTabs.setTabText(self.packagesTabs.indexOf(self.packagesMultimedia), _translate("MainWindow", "Multimedia"))
            self.packagesAudaciousPic.setToolTip(_translate("MainWindow", "Lightweight, advanced audio player focused on audio quality"))
            self.packagesAudaciousCheck.setText("Audacious")
            self.packagesClemetinePic.setToolTip(_translate("MainWindow", "A music player and library organizer"))
            self.packagesClementineCheck.setText("Clementine")
            self.packagesDeadbeefPic.setToolTip(_translate("MainWindow", "An audio player for GNU/Linux based on GTK2."))
            self.packagesDeadbeefCheck.setText("DeaDBeeF")
            self.packagesSmplayerPic.setToolTip(_translate("MainWindow", "A complete front-end for MPlayer"))
            self.packagesSmplayerCheck.setText("SMPlayer")
            self.packagesVlcPic.setToolTip(_translate("MainWindow", "A multi-platform MPEG, VCD/DVD, and DivX player"))
            self.packagesVlcCheck.setText("VLC")
            
            self.packagesTabs.setTabText(self.packagesTabs.indexOf(self.packagesGraphics), _translate("MainWindow", "Graphics"))
            self.packagesBlenderPic.setToolTip(_translate("MainWindow", "A fully integrated 3D graphics creation suite"))
            self.packagesBlenderCheck.setText("Blender")
            self.packagesEvincePic.setToolTip(_translate("MainWindow", "Simply a document viewer"))
            self.packagesEvinceCheck.setText("Evince")
            self.packagesGimpPic.setToolTip(_translate("MainWindow", "GNU Image Manipulation Program"))
            self.packagesGimpCheck.setText("Gimp")
            self.packagesGpicviewPic.setToolTip(_translate("MainWindow", "Lightweight image viewer"))
            self.packagesGpicviewCheck.setText("GPicView")
            self.packagesPintaPic.setToolTip(_translate("MainWindow", "A drawing/editing program modeled after Paint.NET."))
            self.packagesPintaCheck.setText("Pinta")
            self.packagesViewniorPic.setToolTip(_translate("MainWindow", "A simple, fast and elegant image viewer program"))
            self.packagesViewniorCheck.setText("Viewnior")
            
            self.packagesTabs.setTabText(self.packagesTabs.indexOf(self.packagesAccessories), _translate("MainWindow", "Accessories"))
            self.packagesGeanyPic.setToolTip(_translate("MainWindow", "Fast and lightweight IDE"))
            self.packagesGeanyCheck.setText("Geany")
            self.packagesHexchatPic.setToolTip(_translate("MainWindow", "A popular and easy to use graphical IRC (chat) client"))
            self.packagesHexchatCheck.setText("Hexchat")
            self.packagesLeafpadPic.setToolTip(_translate("MainWindow", "A notepad clone for GTK+ 2.0"))
            self.packagesLeafpadCheck.setText("Leafpad")
            self.packagesOctopiPic.setToolTip(_translate("MainWindow", "A powerful Pacman frontend using Qt libs"))
            self.packagesOctopiCheck.setText("Octopi")
            self.packagesPamacPic.setToolTip(_translate("MainWindow", "A gtk3 frontend for pyalpm"))
            self.packagesPamacCheck.setText("Pamac")
            self.packagesPcmanfmPic.setToolTip(_translate("MainWindow", "An extremely fast and lightweight file manager"))
            self.packagesPcmanfmCheck.setText("PCManFM")
            self.packagesSpacefmPic.setToolTip(_translate("MainWindow", "Multi-panel tabbed file manager"))
            self.packagesSpacefmCheck.setText("SpaceFM")
            self.packagesTerminatorPic.setToolTip(_translate("MainWindow", "Terminal emulator that supports tabs and grids"))
            self.packagesTerminatorCheck.setText("Terminator")
            self.packagesThunarPic.setToolTip(_translate("MainWindow", "Modern file manager for Xfce"))
            self.packagesThunarCheck.setText("Thunar")
            
            self.packagesTabs.setTabText(self.packagesTabs.indexOf(self.packagesExtras), _translate("MainWindow", "Extras"))
            self.packagesAurSupportPic.setToolTip(_translate("MainWindow", "Installs yaourt, and required dependencies to access the AUR"))
            self.packagesAurSupportCheck.setText("Aur \nSupport")
            self.packagesLibreOfficeInstallerPic.setToolTip(_translate("MainWindow", "GUI installer for LibreOffice"))
            self.packagesLibreOfficeInstallerCheck.setText("Libre Office \nInstaller")
            self.packagesMultimediaSupportPic.setToolTip(_translate("MainWindow", "Installs flashplugin, and required codecs for playing media"))
            self.packagesMultimediaSupportCheck.setText("Multimedia \nSupport")
            self.packagesPrinterSupportPic.setToolTip(_translate("MainWindow", "Installs manjaro-printer, and CUPS to enable printers"))
            self.packagesPrinterSupportCheck.setText("Printer \nSupport")
            
        
        #Adds the verify page
        self.Verify = QtWidgets.QWidget()
        self.Verify.setObjectName("Verify")
        
        createStaticWidgets(self.Verify)
        
        self.verifyHeader = QtWidgets.QLabel(self.Verify)
        self.verifyMenuContainer = QtWidgets.QWidget(self.Verify)
        self.verifyMenuContainerHLayout = QtWidgets.QHBoxLayout(self.verifyMenuContainer)
        self.verifyFinishMenu = QtWidgets.QPushButton(self.verifyMenuContainer)
        self.verifyMenu = QtWidgets.QPushButton(self.verifyMenuContainer)
        self.verifyArrow = QtWidgets.QLabel(self.verifyMenuContainer)
        self.verifyMenuSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verifyFooterContainer = QtWidgets.QWidget(self.Verify)
        self.verifyFooterContainerHLayout = QtWidgets.QHBoxLayout(self.verifyFooterContainer)
        self.verifyCancel = QtWidgets.QPushButton(self.verifyFooterContainer)
        self.verifyForward = QtWidgets.QPushButton(self.verifyFooterContainer)
        self.verifyPrevious = QtWidgets.QPushButton(self.verifyFooterContainer)
        self.verifyFooterSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verifyIcon = QtWidgets.QLabel(self.Verify)
        self.verifyDesc = QtWidgets.QLabel(self.Verify)
        self.verifySettings = QtWidgets.QScrollArea(self.Verify)
        self.verifySettingsContents = QtWidgets.QWidget()
        self.verifySettingsLayout = QtWidgets.QGridLayout(self.verifySettingsContents)
        self.verifySpacer5 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding) #Bottom spacer
        self.verifySpacer6 = QtWidgets.QSpacerItem(10, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum) #Left spacer
        self.verifySpacer7 = QtWidgets.QSpacerItem(5, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum) #Right spacer
        self.verifyFolders = QtWidgets.QLabel(self.verifySettingsContents)
        self.verifyFoldersEdit = QtWidgets.QPushButton(self.verifySettingsContents)
        self.verifyFoldersDesktop = QtWidgets.QLabel(self.verifySettingsContents)
        self.verifyFoldersDocuments = QtWidgets.QLabel(self.verifySettingsContents)
        self.verifyFoldersDownloads = QtWidgets.QLabel(self.verifySettingsContents)
        self.verifyFoldersMusic = QtWidgets.QLabel(self.verifySettingsContents)
        self.verifyFoldersPictures = QtWidgets.QLabel(self.verifySettingsContents)
        self.verifyFoldersPublic = QtWidgets.QLabel(self.verifySettingsContents)
        self.verifyFoldersTemplates = QtWidgets.QLabel(self.verifySettingsContents)
        self.verifyFoldersVideo = QtWidgets.QLabel(self.verifySettingsContents)
        
        if kwinStatus:
            self.verifyThemesSpacer = QtWidgets.QSpacerItem(0, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
            self.verifyThemes = QtWidgets.QLabel(self.verifySettingsContents)
            self.verifyThemesEdit = QtWidgets.QPushButton(self.verifySettingsContents)
            self.verifyThemesTheme = QtWidgets.QLabel(self.verifySettingsContents)
            
            self.verifyThemes.setObjectName("verifyThemes")
            self.verifyThemesEdit.setObjectName("verifyThemesEdit")
            self.verifyThemesTheme.setObjectName("verifyThemesTheme")
            
            self.verifyThemesEdit.setFlat(True)
            self.verifyThemesEdit.setFocusPolicy(QtCore.Qt.NoFocus)
            
            self.verifySettingsLayout.addItem(self.verifyThemesSpacer, 9, 3, 1, 1)
            self.verifySettingsLayout.addWidget(self.verifyThemesEdit, 10, 2, 1, 1)
            self.verifySettingsLayout.addWidget(self.verifyThemes, 10, 3, 1, 1)
            self.verifySettingsLayout.addWidget(self.verifyThemesTheme, 11, 3, 1, 1)
            
            self.verifyThemesEdit.setText(_translate("MainWindow", "[Edit]"))
            self.verifyThemes.setText(_translate("MainWindow", "Themes"))
            self.verifyThemesTheme.setText(_translate("MainWindow", "KWIN Theme: "))
            
            self.verifyThemesEdit.clicked.connect(self.handleButtonChangeTwo)
        if tintStatus:
            self.verifyTintSpacer = QtWidgets.QSpacerItem(0, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
            self.verifyTint = QtWidgets.QLabel(self.verifySettingsContents)
            self.verifyTintEdit = QtWidgets.QPushButton(self.verifySettingsContents)
            self.verifyTintPosition = QtWidgets.QLabel(self.verifySettingsContents)
            
            self.verifyTint.setObjectName("verifyTint")
            self.verifyTintEdit.setObjectName("verifyTintEdit")
            self.verifyTintPosition.setObjectName("verifyTintPosition")
            
            self.verifyTintEdit.setFlat(True)
            self.verifyTintEdit.setFocusPolicy(QtCore.Qt.NoFocus)
            
            self.verifySettingsLayout.addItem(self.verifyTintSpacer, 12, 3, 1, 1)
            self.verifySettingsLayout.addWidget(self.verifyTintEdit, 13, 2, 1, 1)
            self.verifySettingsLayout.addWidget(self.verifyTint, 13, 3, 1, 1)
            self.verifySettingsLayout.addWidget(self.verifyTintPosition, 14, 3, 1, 1)
            
            self.verifyTintEdit.setText(_translate("MainWindow", "[Edit]"))
            self.verifyTint.setText(_translate("MainWindow", "Tint"))
            self.verifyTintPosition.setText(_translate("MainWindow", "Position: "))
            
            if kwinStatus:
                self.verifyTintEdit.clicked.connect(self.handleButtonChangeThree)
            else:
                self.verifyTintEdit.clicked.connect(self.handleButtonChangeTwo)
        if nitrogenStatus or plasmaStatus:
            self.verifyWallpaperSpacer = QtWidgets.QSpacerItem(0, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
            self.verifyWallpaper = QtWidgets.QLabel(self.verifySettingsContents)
            self.verifyWallpaperEdit = QtWidgets.QPushButton(self.verifySettingsContents)
            self.verifyWallpaperName = QtWidgets.QLabel(self.verifySettingsContents)
            
            self.verifyWallpaper.setObjectName("verifyWallpaper")
            self.verifyWallpaperEdit.setObjectName("verifyWallpaperEdit")
            self.verifyWallpaperName.setObjectName("verifyWallpaperName")
            
            self.verifyWallpaperEdit.setFlat(True)
            self.verifyWallpaperEdit.setFocusPolicy(QtCore.Qt.NoFocus)
            
            self.verifySettingsLayout.addItem(self.verifyWallpaperSpacer, 15, 3, 1, 1)
            self.verifySettingsLayout.addWidget(self.verifyWallpaperEdit, 16, 2, 1, 1)
            self.verifySettingsLayout.addWidget(self.verifyWallpaper, 16, 3, 1, 1)
            self.verifySettingsLayout.addWidget(self.verifyWallpaperName, 17, 3, 1, 1)
            
            self.verifyWallpaperEdit.setText(_translate("MainWindow", "[Edit]"))
            self.verifyWallpaper.setText(_translate("MainWindow", "Wallpaper"))
            self.verifyWallpaperName.setText(_translate("MainWindow", "Name: "))
            
            if kwinStatus and tintStatus:
                self.verifyWallpaperEdit.clicked.connect(self.handleButtonChangeFour)
            elif kwinStatus or tintStatus:
                self.verifyWallpaperEdit.clicked.connect(self.handleButtonChangeThree)
            else:
                self.verifyWallpaperEdit.clicked.connect(self.handleButtonChangeTwo)
        if openboxStatus:
            self.verifyPackagesSpacer = QtWidgets.QSpacerItem(0, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
            self.verifyPackages = QtWidgets.QLabel(self.verifySettingsContents)
            self.verifyPackagesEdit = QtWidgets.QPushButton(self.verifySettingsContents)
            self.verifyPackagesTBI = QtWidgets.QLabel(self.verifySettingsContents)
            self.verifyPackagesTBR = QtWidgets.QLabel(self.verifySettingsContents)
            
            self.verifyPackages.setObjectName("verifyPackages")
            self.verifyPackagesEdit.setObjectName("verifyPackagesEdit")
            self.verifyPackagesTBI.setObjectName("verifyPackagesTBI")
            self.verifyPackagesTBR.setObjectName("verifyPackagesTBR")
            
            self.verifyPackagesEdit.setFlat(True)
            self.verifyPackagesEdit.setFocusPolicy(QtCore.Qt.NoFocus)
            
            self.verifySettingsLayout.addItem(self.verifyPackagesSpacer, 18, 3, 1, 1)
            self.verifySettingsLayout.addWidget(self.verifyPackagesEdit, 19, 2, 1, 1)
            self.verifySettingsLayout.addWidget(self.verifyPackages, 19, 3, 1, 1)
            self.verifySettingsLayout.addWidget(self.verifyPackagesTBI, 20, 3, 1, 1)
            self.verifySettingsLayout.addWidget(self.verifyPackagesTBR, 21, 3, 1, 1)
            
            self.verifyPackagesEdit.setText(_translate("MainWindow", "[Edit]"))
            self.verifyPackages.setText(_translate("MainWindow", "Packages"))
            self.verifyPackagesTBI.setText(_translate("MainWindow", "To be installed: "))
            self.verifyPackagesTBR.setText(_translate("MainWindow", "To be removed: "))
            
            if nitrogenStatus or plasmaStatus and kwinStatus and tintStatus:
                self.verifyPackagesEdit.clicked.connect(self.handleButtonChangeFive)
            elif nitrogenStatus or plasmaStatus and kwinStatus or tintStatus:
                self.verifyPackagesEdit.clicked.connect(self.handleButtonChangeFour)
            elif nitrogenStatus or plasmaStatus or kwinStatus or tintStatus:
                self.verifyPackagesEdit.clicked.connect(self.handleButtonChangeThree)
            else:
                self.verifyPackagesEdit.clicked.connect(self.handleButtonChangeTwo)
        
        
        verifyPageWidgets = {
            "verifyHeader": [self.verifyHeader, 80, 20, 600, 51, "verifyHeader", None],
            "verifyIcon": [self.verifyIcon, 40, 160, 61, 61, "verifyIcon", "/usr/share/turbulence/images/manjaro-grey/verify/verify.png"],
            "verifyDesc": [self.verifyDesc, 110, 140, 650, 100, "verifyDesc", None],
            "verifySettings": [self.verifySettings, 40, 230, 780, 330, "verifySettings", None],
            "veriySettingsContents": [self.verifySettingsContents, 0, 0, 685, 330, "verifySettingsContents", None]
        }

        verifyPageLayouts = {
            "verifyMenu": [self.verifyMenu, 0, 39, None, None, True, True, False],
            "verifyArrow": [self.verifyArrow, None, None, 21, 500, False, False, "/usr/share/turbulence/images/manjaro-grey/menu-arrow.png"],
            "verifyFinishMenu": [self.verifyFinishMenu, 0, 39, None, None, True, True, False],
            "verifyForward": [self.verifyForward, 0, 34, None, None, True, True, False],
            "verifyPrevious": [self.verifyPrevious, 0, 34, None, None, True, True, False],
            "verifyCancel": [self.verifyCancel, 0, 34, None, None, True, True, False],
            "verifyFolders": [self.verifyFolders, None, None, None, None, False, False, False],
            "verifyFoldersEdit": [self.verifyFoldersEdit, None, None, None, None, True, True, False],
            "verifyFoldersDesktop": [self.verifyFoldersDesktop, None, None, None, None, False, False, False],
            "verifyFoldersDocuments": [self.verifyFoldersDocuments, None, None, None, None, False, False, False],
            "verifyFoldersDownloads": [self.verifyFoldersDownloads, None, None, None, None, False, False, False],
            "verifyFoldersMusic": [self.verifyFoldersMusic, None, None, None, None, False, False, False],
            "verifyFoldersPictures": [self.verifyFoldersPictures, None, None, None, None, False, False, False],
            "verifyFoldersPublic": [self.verifyFoldersPublic, None, None, None, None, False, False, False],
            "verifyFoldersTemplates": [self.verifyFoldersTemplates, None, None, None, None, False, False, False],
            "verifyFoldersVideo": [self.verifyFoldersVideo, None, None, None, None, False, False, False]
        }
        
        #defines all the widget parameters
        for widgetName, widgetSettings in verifyPageWidgets.items():
            widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
        
        for widgetName, widgetSettings in verifyPageLayouts.items():
            layoutConfigurer(widgetName, widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6], widgetSettings[7])
        
        self.verifyDesc.setWordWrap(True)
        
        self.verifySettings.setWidgetResizable(True)
        self.verifySettings.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verifySettings.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        
        self.verifyCancel.setIcon(cancelIcon)
        self.verifyForward.setIcon(finishIcon)
        self.verifyPrevious.setIcon(previousIcon)
        self.verifyForward.setIconSize(QtCore.QSize(16, 18))
        self.verifyPrevious.setIconSize(QtCore.QSize(28, 30))
        self.verifyCancel.setIconSize(QtCore.QSize(16, 16))
        
        self.verifyMenuContainerHLayout.addWidget(self.verifyMenu)
        self.verifyMenuContainerHLayout.addWidget(self.verifyArrow)
        self.verifyMenuContainerHLayout.addWidget(self.verifyFinishMenu)
        self.verifyMenuContainerHLayout.addItem(self.verifyMenuSpacer)
        
        self.verifyFooterContainerHLayout.addWidget(self.verifyCancel)
        self.verifyFooterContainerHLayout.addItem(self.verifyFooterSpacer)
        self.verifyFooterContainerHLayout.addWidget(self.verifyPrevious)
        self.verifyFooterContainerHLayout.addWidget(self.verifyForward)
        
        self.verifySettingsLayout.addItem(self.verifySpacer5, 23, 3, 1, 1)
        self.verifySettingsLayout.addItem(self.verifySpacer6, 0, 0, 1, 1)
        self.verifySettingsLayout.addItem(self.verifySpacer7, 0, 5, 1, 1)
        
        self.verifySettingsLayout.addWidget(self.verifyFolders, 0, 3, 1, 1)
        self.verifySettingsLayout.addWidget(self.verifyFoldersEdit, 0, 2, 1, 1)
        self.verifySettingsLayout.addWidget(self.verifyFoldersDesktop, 1, 3, 1, 1)
        self.verifySettingsLayout.addWidget(self.verifyFoldersDocuments, 2, 3, 1, 1)
        self.verifySettingsLayout.addWidget(self.verifyFoldersDownloads, 3, 3, 1, 1)
        self.verifySettingsLayout.addWidget(self.verifyFoldersMusic, 4, 3, 1, 1)
        self.verifySettingsLayout.addWidget(self.verifyFoldersPictures, 5, 3, 1, 1)
        self.verifySettingsLayout.addWidget(self.verifyFoldersPublic, 6, 3, 1, 1)
        self.verifySettingsLayout.addWidget(self.verifyFoldersTemplates, 7, 3, 1, 1)
        self.verifySettingsLayout.addWidget(self.verifyFoldersVideo,8, 3, 1, 1)
        
        self.verifyMenuContainer.setGeometry(QtCore.QRect(20, 83, 511, 50))
        self.verifyFooterContainer.setGeometry(QtCore.QRect(15, 567, 830, 51))
        
        self.verifySettings.setWidget(self.verifySettingsContents)
        
        self.stackedWidget.addWidget(self.Verify)
        
        #Handles the button click
        self.verifyPrevious.clicked.connect(self.handleButtonPrev)
        self.verifyCancel.clicked.connect(MainWindow.close)
        self.verifyFoldersEdit.clicked.connect(self.handleButtonChangeOne)
        self.verifyForward.clicked.connect(self.handleButtonFinish)
        self.verifyFinishMenu.clicked.connect(self.handleButtonFinish)
        
        #Translates the widgets, or sets text
        self.verifyHeader.setText(_translate("MainWindow", "Verify your settings"))
        self.verifyMenu.setText(_translate("MainWindow", "Verify"))
        self.verifyFinishMenu.setText(_translate("MainWindow", "Finish"))
        self.verifyCancel.setText(_translate("MainWindow", "Cancel"))
        self.verifyForward.setText(_translate("MainWindow", "Verify"))
        self.verifyPrevious.setText(_translate("MainWindow", "Previous"))
        self.verifyDesc.setText(_translate("MainWindow", "Please review your changes now. If you agree, then proceed by clicking verify, otherwise click the edit button next to the setting you would like to change."))
        self.verifyFolders.setText(_translate("MainWindow", "Folders"))
        self.verifyFoldersEdit.setText(_translate("MainWindow", "[Edit]"))
        self.verifyFoldersDesktop.setText(_translate("MainWindow", "Desktop:"))
        self.verifyFoldersDocuments.setText(_translate("MainWindow", "Documents:"))
        self.verifyFoldersDownloads.setText(_translate("MainWindow", "Downloads:"))
        self.verifyFoldersMusic.setText(_translate("MainWindow", "Music:"))
        self.verifyFoldersPictures.setText(_translate("MainWindow", "Pictures:"))
        self.verifyFoldersPublic.setText(_translate("MainWindow", "Public:"))
        self.verifyFoldersTemplates.setText(_translate("MainWindow", "Templates:"))
        self.verifyFoldersVideo.setText(_translate("MainWindow", "Videos:"))
        
        
        #Adds the fifth and final page
        self.Finish = QtWidgets.QWidget()
        self.Finish.setObjectName("Finish")
        
        createStaticWidgets(self.Finish)
        
        self.finishHeader = QtWidgets.QLabel(self.Finish)
        self.finishMenuContainer = QtWidgets.QWidget(self.Finish)
        self.finishMenuContainerHLayout = QtWidgets.QHBoxLayout(self.finishMenuContainer)
        self.finishMenu = QtWidgets.QPushButton(self.finishMenuContainer)
        self.finishMenuSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.finishFooterContainer = QtWidgets.QWidget(self.Finish)
        self.finishFooterContainerHLayout = QtWidgets.QHBoxLayout(self.finishFooterContainer)
        self.finishCancel = QtWidgets.QPushButton(self.finishFooterContainer)
        self.finishForward = QtWidgets.QPushButton(self.finishFooterContainer)
        self.finishFooterSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.finishDesc = QtWidgets.QLabel(self.Finish)
        self.finishSystemSettings = QtWidgets.QLabel(self.Finish)
        self.finishSystemSettingsPic = QtWidgets.QLabel(self.Finish)
        self.finishSystemSettingsDesc = QtWidgets.QLabel(self.Finish)
        self.finishSystemSettingsButton = QtWidgets.QPushButton(self.Finish)
        self.finishHelpHead = QtWidgets.QLabel(self.Finish)
        self.finishHelpPic = QtWidgets.QLabel(self.Finish)
        self.finishHelpDesc = QtWidgets.QLabel(self.Finish)
        self.finishHelpButton = QtWidgets.QPushButton(self.Finish)
         
        finalPageWidgets = {
            "finishHeader": [self.finishHeader, 80, 20, 600, 51, "finishHeader", None],
            "finishDesc": [self.finishDesc, 30, 150, 781, 51, "finishDesc", None],
            "finishSystemSettings": [self.finishSystemSettings, 40, 220, 500, 31, "finishSystemSettings", None],
            "finishSystemSettingsPic": [self.finishSystemSettingsPic, 70, 260, 111, 101, "finishSystemSettingsPic", "/usr/share/turbulence/images/manjaro-grey/finish/preferences-system.png"],
            "finishSystemSettingsDesc": [self.finishSystemSettingsDesc, 200, 280, 390, 31, "finishSystemSettingsDesc", None],
            "finishSystemSettingsButton": [self.finishSystemSettingsButton, 200, 310, 390, 41, "finishSystemSettingsButton", None],
            "finishHelpHead": [self.finishHelpHead, 40, 400, 500, 31, "finishHelpHead", None, None],
            "finishHelpPic": [self.finishHelpPic, 70, 440, 111, 101, "finishHelpPic", "/usr/share/turbulence/images/manjaro-grey/finish/help-icon.png"],
            "finishHelpDesc": [self.finishHelpDesc, 200, 440, 390, 51, "finishHelpDesc", None],
            "finishHelpButton": [self.finishHelpButton, 200, 490, 390, 41, "finishHelpButton", None]
        }

        fifthPageLayouts = {
            "finishMenu": [self.finishMenu, 0, 39, None, None, True, True, False],
            "finishForward": [self.finishForward, 0, 34, None, None, True, True, False],
            "finishCancel": [self.finishCancel, 0, 34, None, None, True, True, False]
        }
	
        #defines all the widget parameters
        for widgetName, widgetSettings in finalPageWidgets.items():
            widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
        
        for widgetName, widgetSettings in fifthPageLayouts.items():
            layoutConfigurer(widgetName, widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6], widgetSettings[7])
            
        #Defines the custom settings
        self.finishSystemSettingsButton.setFlat(True)
        self.finishHelpButton.setFlat(True)
        
        self.finishDesc.setWordWrap(True)
        self.finishSystemSettingsDesc.setWordWrap(True)
        self.finishHelpDesc.setWordWrap(True)
        
        self.finishSystemSettingsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.finishHelpButton.setFocusPolicy(QtCore.Qt.NoFocus)
        
        self.finishCancel.setIcon(cancelIcon)
        self.finishForward.setIcon(finishIcon)
        self.finishForward.setIconSize(QtCore.QSize(16, 18))
        self.finishCancel.setIconSize(QtCore.QSize(16, 16))
        
        self.finishMenuContainerHLayout.addWidget(self.finishMenu)
        self.finishMenuContainerHLayout.addItem(self.finishMenuSpacer)
            
        self.finishFooterContainerHLayout.addWidget(self.finishCancel)
        self.finishFooterContainerHLayout.addItem(self.finishFooterSpacer)
        self.finishFooterContainerHLayout.addWidget(self.finishForward)
            
        self.finishMenuContainer.setGeometry(QtCore.QRect(20, 83, 511, 50))
        self.finishFooterContainer.setGeometry(QtCore.QRect(15, 567, 830, 51))
            
        self.stackedWidget.addWidget(self.Finish)
        
        #Handles the button click
        self.finishHelpButton.clicked.connect(self.handleButtonLaunchHelp)
        self.finishCancel.clicked.connect(MainWindow.close)
        self.finishForward.clicked.connect(MainWindow.close)
        
        #Translates the widgets, or sets text
        self.finishHeader.setText(_translate("MainWindow", "Congratulations!"))
        self.finishMenu.setText(_translate("MainWindow", "Finish"))
        self.finishCancel.setText(_translate("MainWindow", "Cancel"))
        self.finishForward.setText(_translate("MainWindow", "Finish"))
        self.finishDesc.setText(_translate("MainWindow", "All of your settings have been applied. Now, you can start enjoying Manjaro, or look at some of the programs and links below. Also, if you haven\'t already, make sure to join the Manjaro community as well!"))
        self.finishHelpHead.setText(_translate("MainWindow", "Help"))
        self.finishHelpDesc.setText(_translate("MainWindow", "For help and support, you can visit Manjaro.org for access to a terrific forum, wiki, and IRC!"))
        self.finishHelpButton.setText(_translate("MainWindow", "Launch Manjaro.org"))
        
        if kdeStatus:
            self.finishSystemSettings.setText(_translate("MainWindow", "System Settings"))
            self.finishSystemSettingsDesc.setText(_translate("MainWindow", "Control panel to edit various aspects of the KDE desktop, and more."))
            self.finishSystemSettingsButton.setText(_translate("MainWindow", "Launch System Settings"))
            self.finishSystemSettingsButton.clicked.connect(self.handleButtonSystemSettings)
        elif openboxStatus:
            self.finishSystemSettings.setText(_translate("MainWindow", "Customize OpenBox"))
            self.finishSystemSettingsDesc.setText(_translate("MainWindow", "Control panel to edit various aspects of OpenBox"))
            self.finishSystemSettingsButton.setText(_translate("MainWindow", "Launch Customize Look and Feel"))
            self.finishSystemSettingsButton.clicked.connect(self.handleButtonlxappearance)
        
        
        #Configures the window a bit more.
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("Turbulence")
        self.stackedWidget.setCurrentIndex(0) #Sets the index for the stacked widget to 0.
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #sets the current checked boxes and status. It's at the bottom to be out of the way.
        global neededDirs #This needs to be global because it's later used in handleButtonNextVerify
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
        
        global packagesList #Snags the current list of packages.
        packagesList = packages.getCurrentPackages()
        
        
    def handleButtonNextVerify(self):
        checkboxDirectoryPairs = {
            self.folderActive1: ["DESKTOP", "Desktop:", self.verifyFoldersDesktop],
            self.folderActive2: ["DOCUMENTS", "Documents:", self.verifyFoldersDocuments],
            self.folderActive3: ["DOWNLOAD", "Download:", self.verifyFoldersDownloads],
            self.folderActive4: ["MUSIC", "Music:", self.verifyFoldersMusic],
            self.folderActive5: ["PICTURES", "Pictures:", self.verifyFoldersPictures],
            self.folderActive6: ["PUBLICSHARE", "Public:", self.verifyFoldersPublic],
            self.folderActive7: ["TEMPLATES", "Templates:", self.verifyFoldersTemplates],
            self.folderActive8: ["VIDEOS", "Videos:", self.verifyFoldersVideo]
        }
        
        for checkbox, directoryPoint in checkboxDirectoryPairs.items():
            if checkbox.isChecked() and directoryPoint[0] not in neededDirs:
                directoryPoint[2].setText(_translate("MainWindow", directoryPoint[1] + " Create"))
            elif checkbox.isChecked() and directoryPoint[0] in neededDirs:
                directoryPoint[2].setText(_translate("MainWindow", directoryPoint[1] + " Nothing to do"))
            elif not checkbox.isChecked() and directoryPoint[0] in neededDirs:
                directoryPoint[2].setText(_translate("MainWindow", directoryPoint[1] + " Delete"))
            elif not checkbox.isChecked() and directoryPoint[0] not in neededDirs:
                directoryPoint[2].setText(_translate("MainWindow", directoryPoint[1] + " Nothing to do"))
        
        if kwinStatus:
            if self.themeRadio1.isChecked():
                self.verifyThemesTheme.setText(_translate("MainWindow", "KWIN Theme: ") + str(self.themeRadio1.text()))
            elif self.themeRadio2.isChecked():
                self.verifyThemesTheme.setText(_translate("MainWindow", "KWIN Theme: ") + str(self.themeRadio2.text()))
            elif self.themeRadio3.isChecked():
                self.verifyThemesTheme.setText(_translate("MainWindow", "KWIN Theme: ") + str(self.themeRadio3.text()))
            elif self.themeRadio4.isChecked():
                self.verifyThemesTheme.setText(_translate("MainWindow", "KWIN Theme: ") + str(self.themeRadio4.text()))
            else:
                self.verifyThemesTheme.setText(_translate("MainWindow", "KWIN Theme: Nothing to do"))
                
        if tintStatus:
            if self.tintPositionRadio1.isChecked():
                self.verifyTintPosition.setText(_translate("MainWindow", "Position: ") + str(self.tintPositionRadio1.text()))
            elif self.tintPositionRadio2.isChecked():
                self.verifyTintPosition.setText(_translate("MainWindow", "Position: ") + str(self.tintPositionRadio2.text()))
            elif self.tintPositionRadio3.isChecked():
                self.verifyTintPosition.setText(_translate("MainWindow", "Position: ") + str(self.tintPositionRadio3.text()))
            elif self.tintPositionRadio4.isChecked():
                self.verifyTintPosition.setText(_translate("MainWindow", "Position: ") + str(self.tintPositionRadio4.text()))
            else:
                self.verifyTintPosition.setText(_translate("MainWindow", "Position: Nothing to do"))
                
        if nitrogenStatus or plasmaStatus:
            if self.wallpaperChoice1.isChecked():
                self.verifyWallpaperName.setText(_translate("MainWindow", "Name: ") + str(self.wallpaperChoice1.text()))
            elif self.wallpaperChoice2.isChecked():
                self.verifyWallpaperName.setText(_translate("MainWindow", "Name: ") + str(self.wallpaperChoice2.text()))
            elif self.wallpaperChoice3.isChecked():
                self.verifyWallpaperName.setText(_translate("MainWindow", "Name: ") + str(self.wallpaperChoice3.text()))
            elif self.wallpaperChoice4.isChecked():
                self.verifyWallpaperName.setText(_translate("MainWindow", "Name: ") + str(self.wallpaperChoice4.text()))
            elif self.wallpaperChoice5.isChecked():
                self.verifyWallpaperName.setText(_translate("MainWindow", "Name: ") + str(self.wallpaperChoice5.text()))
            elif self.wallpaperChoice6.isChecked():
                self.verifyWallpaperName.setText(_translate("MainWindow", "Name: ") + str(self.wallpaperChoice6.text()))
            elif self.wallpaperChoice7.isChecked():
                self.verifyWallpaperName.setText(_translate("MainWindow", "Name: ") + str(self.wallpaperChoice7.text()))
            elif self.wallpaperChoice8.isChecked():
                self.verifyWallpaperName.setText(_translate("MainWindow", "Name: ") + str(self.wallpaperChoice8.text()))
            else:
                self.verifyWallpaperName.setText(_translate("MainWindow", "Name: Nothing to do"))
                
        if openboxStatus:
                    
            packagesMFI = {
                "chromium": self.packagesChromiumCheck, 
                "deluge": self.packagesDelugeCheck,
                "ekiga": self.packagesEkigaCheck,
                "filezilla": self.packagesFilezillaCheck,
                "firefox": self.packagesFirefoxCheck,
                "midori": self.packagesMidoriCheck,
                "opera": self.packagesOperaCheck, 
                "qbittorrent": self.packagesQbittorrentCheck,
                "thunderbird": self.packagesThunderbirdCheck,
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
                "pinta": self.packagesPintaCheck,
                "viewnior": self.packagesViewniorCheck,
                "geany": self.packagesGeanyCheck,
                "hexchat": self.packagesHexchatCheck,
                "leafpad": self.packagesLeafpadCheck,
                "octopi": self.packagesOctopiCheck,
                "pamac": self.packagesPamacCheck,
                "pcmanfm": self.packagesPcmanfmCheck,
                "spacefm": self.packagesSpacefmCheck,
                "terminator": self.packagesTerminatorCheck,
                "thunar": self.packagesThunarCheck,
                "yaourt": self.packagesAurSupportCheck, #Aur support
                "libreoffice-installer": self.packagesLibreOfficeInstallerCheck, #Libre Office Installer
                "flashplugin": self.packagesMultimediaSupportCheck, #Multimedia support
                "manjaro-printer": self.packagesPrinterSupportCheck #Printing support
            
            }
            packagesTBIList = []
            packagesTBRList = []
            packagesTBIListCleaned = []
            packagesTBNList = []
            packagesTBRListCleaned = []
            for packageName, packageCheck in packagesMFI.items():
                if packageCheck.isChecked():
                    packagesTBIList.append(packageName)
                else:
                    packagesTBRList.append(packageName)
                    
            packagesTBIListCleaned = list(set(packagesTBIList) - set(packagesList)) #Packages to be installed
            packagesTBNList = list(set(packagesList) - set(packagesTBRList)) #Packages that don't need to be removed or installed (neutral).
            packagesTBRListCleaned = list(set(packagesList) - set(packagesTBNList)) #Packages to be removed        
            
            if self.internetAccess:
                if packagesTBIListCleaned:
                    self.verifyPackagesTBI.setText(_translate("MainWindow", "To be installed: ") + ", ".join(str(packageName) for packageName in packagesTBIListCleaned))
                else:
                    self.verifyPackagesTBI.setText(_translate("MainWindow", "To be installed: Nothing to do"))
                if packagesTBRListCleaned:
                    self.verifyPackagesTBR.setText(_translate("MainWindow", "To be removed: ") + ", ".join(str(packageName) for packageName in packagesTBRListCleaned))
                else:
                    self.verifyPackagesTBR.setText(_translate("MainWindow", "To be removed: Nothing to do"))
            else: 
                self.verifyPackagesTBI.setText(_translate("MainWindow", "To be installed: Nothing to do"))
                self.verifyPackagesTBR.setText(_translate("MainWindow", "To be removed: Nothing to do"))
                    
        
        index = self.stackedWidget.currentIndex() + 1
        if index < self.stackedWidget.count():
            self.stackedWidget.setCurrentIndex(index)
            logger.writeLog('proceedToVerify')
                
    
    
    def handleButtonFinish(self):
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
                
        if kwinStatus:
            kwinThemes = {
                "air-black": self.themeRadio1,
                "cupertino-ish": self.themeRadio2,
                "oxygen": self.themeRadio3,
                "plastik": self.themeRadio4,
            }
            
            for themeName, themeRadio in kwinThemes.items():
                if themeRadio.isChecked():
                    themes.kwinThemer(themeName)
                    plasma_control.startKwin()
        
        if tintStatus:    
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
                    
        if nitrogenStatus or plasmaStatus:
            if kdeStatus:
                wallpapersDict = {
                    "manjarostyle": self.wallpaperChoice1,
                    "orangeSplash": self.wallpaperChoice2,
                    "sunsetPlane": self.wallpaperChoice3,
                    "mountainLake": self.wallpaperChoice4,
                    "earthInSpace": self.wallpaperChoice5,
                    "darkStairs": self.wallpaperChoice6,
                    "cherryJapan": self.wallpaperChoice7,
                    "whiteTiger": self.wallpaperChoice8
                }
                edition = "kde"
            elif nitrogenStatus:
                wallpapersDict = {
                    "evodark": self.wallpaperChoice1,
                    "evolight": self.wallpaperChoice2,
                    "sunsetPlane": self.wallpaperChoice3,
                    "mountainLake": self.wallpaperChoice4,
                    "earthInSpace": self.wallpaperChoice5,
                    "darkStairs": self.wallpaperChoice6,
                    "cherryJapan": self.wallpaperChoice7,
                    "whiteTiger": self.wallpaperChoice8
                }
                edition = "openbox"
            else:
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
                edition = "kde"
        
            for wallpaperName, wallpaperRadio in wallpapersDict.items():
                if wallpaperRadio.isChecked():
                    wallpapers.changeWallpaperPlus(wallpaperName, edition)
            
        if openboxStatus and self.internetAccess:
            packagesMFI = {
                "chromium": self.packagesChromiumCheck, 
                "deluge": self.packagesDelugeCheck,
                "ekiga": self.packagesEkigaCheck,
                "filezilla": self.packagesFilezillaCheck,
                "firefox": self.packagesFirefoxCheck,
                "midori": self.packagesMidoriCheck,
                "opera": self.packagesOperaCheck, 
                "qbittorrent": self.packagesQbittorrentCheck,
                "thunderbird": self.packagesThunderbirdCheck,
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
                "pinta": self.packagesPintaCheck,
                "viewnior": self.packagesViewniorCheck,
                "geany": self.packagesGeanyCheck,
                "hexchat": self.packagesHexchatCheck,
                "leafpad": self.packagesLeafpadCheck,
                "octopi": self.packagesOctopiCheck,
                "pamac": self.packagesPamacCheck,
                "pcmanfm": self.packagesPcmanfmCheck,
                "spacefm": self.packagesSpacefmCheck,
                "terminator": self.packagesTerminatorCheck,
                "thunar": self.packagesThunarCheck,
                "yaourt": self.packagesAurSupportCheck, #Aur support
                "libreoffice-installer": self.packagesLibreOfficeInstallerCheck, #Libre Office Installer
                "flashplugin": self.packagesMultimediaSupportCheck, #Multimedia support
                "manjaro-printer": self.packagesPrinterSupportCheck #Printing support
            }
            packagesTBIList = []
            packagesTBRList = []
            for packageName, packageCheck in packagesMFI.items():
                if packageCheck.isChecked():
                    packagesTBIList.append(packageName)
                else:
                    packagesTBRList.append(packageName)
                    
            packages.handlePackages(packagesTBIList, packagesTBRList)
            
        index = self.stackedWidget.currentIndex() + 1
        if index < self.stackedWidget.count():
            self.stackedWidget.setCurrentIndex(index)
            logger.writeLog('proceedToFinal')
    
    
    
    #Moves to next page in the stacked widget.
    def handleButtonNext(self):
        index = self.stackedWidget.currentIndex() + 1
        if index < self.stackedWidget.count():
            self.stackedWidget.setCurrentIndex(index)
            
    def checkInternetStatus(self):
        if packages.checkInternet():
            self.internetAccess = True
            self.packagesTabs.tabBar().setEnabled(True)
            self.packagesCheckConnection.lower()
            self.packagesNotActive.lower()
            logger.writeLog("checkInternetStatusPassed")
        else:
            self.packagesCheckConnection.setText(_translate("MainWindow", "Failed. Please Try Again.", None))
            logger.writeLog("checkInternetStatusFailed")
            self.internetAccess = False
            return 0
        
        packagesMFI = {
                "chromium": self.packagesChromiumCheck, 
                "deluge": self.packagesDelugeCheck,
                "ekiga": self.packagesEkigaCheck,
                "filezilla": self.packagesFilezillaCheck,
                "firefox": self.packagesFirefoxCheck,
                "midori": self.packagesMidoriCheck,
                "opera": self.packagesOperaCheck, 
                "qbittorrent": self.packagesQbittorrentCheck,
                "thunderbird": self.packagesThunderbirdCheck,
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
                "pinta": self.packagesPintaCheck,
                "viewnior": self.packagesViewniorCheck,
                "geany": self.packagesGeanyCheck,
                "hexchat": self.packagesHexchatCheck,
                "leafpad": self.packagesLeafpadCheck,
                "octopi": self.packagesOctopiCheck,
                "pamac": self.packagesPamacCheck,
                "pcmanfm": self.packagesPcmanfmCheck,
                "spacefm": self.packagesSpacefmCheck,
                "terminator": self.packagesTerminatorCheck,
                "thunar": self.packagesThunarCheck,
                "yaourt": self.packagesAurSupportCheck, #Aur support
                "libreoffice-installer": self.packagesLibreOfficeInstallerCheck, #Libre Office Installer
                "flashplugin": self.packagesMultimediaSupportCheck, #Multimedia support
                "manjaro-printer": self.packagesPrinterSupportCheck #Printing support
        }
        packagesAI = set(packagesList).intersection(packagesMFI)
        packagesAIList = list(packagesAI)
        
        for packagesItem in packagesAIList:
            packagesMFI[packagesItem].setChecked(True)
            
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
            
    #Changes to the selected page.
    def handleButtonChangeOne(self):
        self.stackedWidget.setCurrentIndex(1)
    def handleButtonChangeTwo(self):
        self.stackedWidget.setCurrentIndex(2)
    def handleButtonChangeThree(self):
        self.stackedWidget.setCurrentIndex(3)
    def handleButtonChangeFour(self):
        self.stackedWidget.setCurrentIndex(4)
    def handleButtonChangeFive(self):
        self.stackedWidget.setCurrentIndex(5)