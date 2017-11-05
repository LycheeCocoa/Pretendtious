# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        mode = 0;
        Dialog.setObjectName("Dialog")
        Dialog.resize(599, 402)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(250, 370, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.TabContainer = QtWidgets.QTabWidget(Dialog)
        self.TabContainer.setEnabled(True)
        self.TabContainer.setGeometry(QtCore.QRect(10, 10, 571, 351))
        self.TabContainer.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.TabContainer.setAcceptDrops(False)
        self.TabContainer.setTabPosition(QtWidgets.QTabWidget.North)
        self.TabContainer.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.TabContainer.setElideMode(QtCore.Qt.ElideNone)
        self.TabContainer.setUsesScrollButtons(False)
        self.TabContainer.setObjectName("TabContainer")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 411, 51))
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setObjectName("textEdit")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 70, 86, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Pretendtious = QtWidgets.QRadioButton(self.layoutWidget)
        self.Pretendtious.setObjectName("Pretendtious")
        self.verticalLayout.addWidget(self.Pretendtious)
        self.Work = QtWidgets.QRadioButton(self.layoutWidget)
        self.Work.setObjectName("Work")
        self.verticalLayout.addWidget(self.Work)
        self.Boring = QtWidgets.QRadioButton(self.layoutWidget)
        self.Boring.setObjectName("Boring")
        self.verticalLayout.addWidget(self.Boring)
        self.Boring.hide()
        self.Degenerator = QtWidgets.QRadioButton(self.layoutWidget)
        self.Degenerator.setObjectName("Degenerator")
        self.verticalLayout.addWidget(self.Degenerator)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(110, 70, 131, 21))
        self.textBrowser.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textBrowser.setAcceptDrops(False)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")
        self.InputPhoneNumber = QtWidgets.QTextEdit(self.tab)
        self.InputPhoneNumber.setGeometry(QtCore.QRect(110, 100, 141, 21))
        self.InputPhoneNumber.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.InputPhoneNumber.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.InputPhoneNumber.setObjectName("InputPhoneNumber")
        self.textEdit.raise_()
        self.layoutWidget.raise_()
        self.Boring.raise_()
        self.Boring.raise_()
        self.Pretendtious.raise_()
        self.textBrowser.raise_()
        self.InputPhoneNumber.raise_()
        self.TabContainer.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.AddMusic = QtWidgets.QTextEdit(self.tab_3)
        self.AddMusic.setGeometry(QtCore.QRect(10, 220, 141, 21))
        self.AddMusic.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.AddMusic.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.AddMusic.setObjectName("AddMusic")
        self.AddMusicButton = QtWidgets.QPushButton(self.tab_3)
        self.AddMusicButton.setGeometry(QtCore.QRect(160, 220, 75, 23))
        self.AddMusicButton.setObjectName("AddMusicButton")
        self.RemoveMusicButton = QtWidgets.QPushButton(self.tab_3)
        self.RemoveMusicButton.setGeometry(QtCore.QRect(450, 220, 101, 23))
        self.RemoveMusicButton.setObjectName("RemoveMusicButton")
        self.MusicTable = QtWidgets.QTableWidget(self.tab_3)
        self.MusicTable.setGeometry(QtCore.QRect(10, 10, 541, 192))
        self.MusicTable.setRowCount(0)
        self.MusicTable.setColumnCount(1)
        self.MusicTable.setObjectName("MusicTable")
        self.MusicTable.horizontalHeader().setVisible(False)
        self.MusicTable.horizontalHeader().setStretchLastSection(True)
        self.MusicTable.verticalHeader().setStretchLastSection(False)
        self.TabContainer.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.AddWebsite = QtWidgets.QTextEdit(self.tab_4)
        self.AddWebsite.setGeometry(QtCore.QRect(10, 220, 141, 21))
        self.AddWebsite.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.AddWebsite.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.AddWebsite.setObjectName("AddWebsite")
        self.AddWebsiteButton = QtWidgets.QPushButton(self.tab_4)
        self.AddWebsiteButton.setGeometry(QtCore.QRect(160, 220, 75, 23))
        self.AddWebsiteButton.setObjectName("AddWebsiteButton")
        self.RemoveWebsiteButton = QtWidgets.QPushButton(self.tab_4)
        self.RemoveWebsiteButton.setGeometry(QtCore.QRect(450, 220, 101, 23))
        self.RemoveWebsiteButton.setObjectName("RemoveWebsiteButton")
        self.WebSiteTable = QtWidgets.QTableWidget(self.tab_4)
        self.WebSiteTable.setGeometry(QtCore.QRect(10, 10, 541, 192))
        self.WebSiteTable.setRowCount(0)
        self.WebSiteTable.setColumnCount(1)
        self.WebSiteTable.setObjectName("WebSiteTable")
        self.WebSiteTable.horizontalHeader().setVisible(False)
        self.WebSiteTable.horizontalHeader().setStretchLastSection(True)
        self.WebSiteTable.verticalHeader().setStretchLastSection(False)
        self.TabContainer.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.AddWallpaper = QtWidgets.QTextEdit(self.tab_2)
        self.AddWallpaper.setGeometry(QtCore.QRect(10, 220, 141, 21))
        self.AddWallpaper.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.AddWallpaper.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.AddWallpaper.setObjectName("AddWallpaper")
        self.AddWallpaperButton = QtWidgets.QPushButton(self.tab_2)
        self.AddWallpaperButton.setGeometry(QtCore.QRect(160, 220, 81, 23))
        self.AddWallpaperButton.setObjectName("AddWallpaperButton")
        self.RemoveWallpaperButton = QtWidgets.QPushButton(self.tab_2)
        self.RemoveWallpaperButton.setGeometry(QtCore.QRect(450, 220, 101, 23))
        self.RemoveWallpaperButton.setObjectName("RemoveWallpaperButton")
        self.WallPaperTable = QtWidgets.QTableWidget(self.tab_2)
        self.WallPaperTable.setGeometry(QtCore.QRect(10, 10, 541, 192))
        self.WallPaperTable.setRowCount(0)
        self.WallPaperTable.setColumnCount(1)
        self.WallPaperTable.setObjectName("WallPaperTable")
        self.WallPaperTable.horizontalHeader().setVisible(False)
        self.WallPaperTable.horizontalHeader().setStretchLastSection(True)
        self.WallPaperTable.verticalHeader().setStretchLastSection(False)
        self.TabContainer.addTab(self.tab_2, "")
        self.TabContainer.raise_()
        self.buttonBox.raise_()

        self.retranslateUi(Dialog)
        self.TabContainer.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.Pretendtious.toggled.connect(self.isPretendtious)
        #self.Pretendtious.toggled.connect()  
  
        self.Boring.toggled.connect(self.isBoring)  
        self.Work.toggled.connect(self.isWork)  
        self.Degenerator.toggled.connect(self.isDegenerator)  

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The next time you launch the Pretendtious App the following settings will be applied. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pick the profile you\'d like to use and/or edit.</p></body></html>"))
        self.Pretendtious.setText(_translate("Dialog", "Pretendtious"))
        self.Work.setText(_translate("Dialog", "Work"))
        self.Boring.setText(_translate("Dialog", "Boring"))
        self.Degenerator.setText(_translate("Dialog", "Degenerator"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Input Phone Number</p></body></html>"))
        self.TabContainer.setTabText(self.TabContainer.indexOf(self.tab), _translate("Dialog", "Profiles"))
        self.AddMusicButton.setText(_translate("Dialog", "Add Music"))
        self.RemoveMusicButton.setText(_translate("Dialog", "Remove Music"))
        self.TabContainer.setTabText(self.TabContainer.indexOf(self.tab_3), _translate("Dialog", "Music"))
        self.AddWebsiteButton.setText(_translate("Dialog", "Add Websites"))
        self.RemoveWebsiteButton.setText(_translate("Dialog", "Remove Website"))
        self.TabContainer.setTabText(self.TabContainer.indexOf(self.tab_4), _translate("Dialog", "Websites"))
        self.AddWallpaperButton.setText(_translate("Dialog", "Add Wallpaper"))
        self.RemoveWallpaperButton.setText(_translate("Dialog", "Remove Wallpaper"))
        self.TabContainer.setTabText(self.TabContainer.indexOf(self.tab_2), _translate("Dialog", "Wallpaper"))


        
    def isPretendtious(self):
        if self.Pretendtious.isChecked():
            #self.Pretendtious.setText("0")
            #type_string = "Pretendtious"
            file = open('mode.txt','w')
            mode = 0
            file.write("0")
            self.populateMusic(0)

    def isBoring(self):
        if self.Boring.isChecked():
            #self.Boring.setText("1")
            #type_string = "Boring"
            file = open('mode.txt','w')
            mode = 2 
            file.write("2")

    def isWork(self):
        if self.Work.isChecked():
            #self.Work.setText("2")
            #type_string = "Work"
            file = open('mode.txt','w') 
            mode = 1
            file.write("1")
    
    def isDegenerator(self):
        if self.Degenerator.isChecked():
            #self.Degenerator.setText("3")
            #type_string = "Degenerator"
            file = open('mode.txt','w') 
            mode = 3
            file.write("3")

    def populateMusic(self, mode):
        profile_type = ""
        if(mode == 0):
            profile_type = "pretendtious"        
        elif(mode == 1):
            profile_type = "work"
        elif(mode == 2):
            profile_type = "boring"
        elif(mode == 3):
            profile_type = "degenerator"
        file = open(profile_type + "/music.txt")
        arr = []
        for aline in file.readlines():
            # values = aline.splitlines()
            arr.append(aline)

        self.MusicTable.setRowCount(len(arr))
        self.MusicTable.setColumnCount(1)

        for count, i in enumerate(arr):
            music = QTableWidgetItem(str(i))
            music.setFlags(QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled)
            self.MusicTable.setItem(count,0, music)
        file.close()

    def populateWallpaper(profile):
        profile_type = ""
        if(mode == 0):
            profile_type = "pretendtious"        
        elif(mode == 1):
            profile_type = "work"
        elif(mode == 2):
            profile_type = "boring"
        elif(mode == 3):
            profile_type = "degenerator"
        file = open(profile_type + "/wallpaper.txt")
        arr = []
        for aline in file.readlines():
            arr.append(aline)

        self.WallPaperTable.setRowCount(len(arr))
        self.WallPaperTable.setColumnCount(1)

        for count, i in enumerate(arr):
            wall = QTableWidgetItem(str(i))
            wall.setFlags(QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled)
            self.WallPaperTable.setItem(count,0, wall)
        file.close()

    def populateWebsite(profile):
        profile_type = ""
        if(mode == 0):
            profile_type = "pretendtious"        
        elif(mode == 1):
            profile_type = "work"
        elif(mode == 2):
            profile_type = "boring"
        elif(mode == 3):
            profile_type = "degenerator"
        file = open(profile_type + "/website.txt")
        arr = []
        for aline in file.readlines():
            arr.append(aline)

        self.WebSiteTable.setRowCount(len(arr))
        self.WebSiteTable.setColumnCount(1)

        for count, i in enumerate(arr):
            web = QTableWidgetItem(str(i))
            web.setFlags(QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled)
            self.WebSiteTable.setItem(count,0, web)
        file.close()
    #def addWebsiteTo(website_link, profile):

    #def removeWebsiteFrom(website_link, profile):

    #def addMusicTo(website_link, profile):

    #def removeMusicFrom(website_link, profile):

    #def addWallpaperTo(website_link, profile):

    #def RemoveWallpaperFrom(website_link, profile):

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

