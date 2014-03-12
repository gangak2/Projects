#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
author: Gangaprasad Koturwar
website: www.iitk.ac.in/~users/koturwar (internal site)
last edited: TMar 12, 2014
"""

import sys
import threading
import subprocess
import time
import urllib2
from PyQt4 import QtGui, QtCore
from PyQt4.Qt import *

hostname1 = None
passwd1 = None

class Secondary_Window(QtGui.QWidget):
    
    
    def __init__(self, parent):
        super(Secondary_Window, self).__init__()

        self.initUI()
        
    def initUI(self):
    

    
    	self.path1 = "Folder\ 1"
    	self.path2 = "Folder\ 3"
    	self.usr = ""
    	self.hst = ""
    	self.dirt = ""
    	self.stopthread = threading.Event()
        
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
 
        top = QtGui.QFrame(self)
        top.setFrameShape(QtGui.QFrame.StyledPanel)

        self.host = QtGui.QLabel('HostName')
        self.user = QtGui.QLabel('User')

        self.hostname = QtGui.QLineEdit(top)
        self.hostname.move(200, 110)
        self.hostname.setPlaceholderText("eg: 192.160.0.107")
        self.username = QtGui.QLineEdit(top)
        self.username.move(200, 160)
        self.username.setPlaceholderText("eg: gangaprasad")
        self.dirname = QtGui.QLineEdit(top)
        self.dirname.move(200, 200)
        self.dirname.setPlaceholderText("eg: /home/prasad")

        self.hostname.setObjectName("Hostname")
        self.username.setObjectName("User")

        self.hosttext = QtGui.QLabel("hostname",top)
        self.hosttext.move(100, 110)
        self.usertext = QtGui.QLabel("username",top)
        self.usertext.move(100, 160)
        self.dirtext = QtGui.QLabel("directory",top)
        self.dirtext.move(100, 200)

        hbox = QtGui.QHBoxLayout()

        self.setLayout(hbox)   

        btn1 = QtGui.QPushButton('Select Folder to Sync', top)
        btn1.setToolTip('This is a <b>QPushButton</b> widget')
        self.path1 = btn1.clicked.connect(self.showDialog)
        btn1.resize(btn1.sizeHint())
        btn1.move(180, 40)




        startsync = QtGui.QPushButton('Start syncing', top)
        startsync.setToolTip('This is a sync initializer')
        startsync.clicked.connect(self.startscript)
        startsync.resize(startsync.sizeHint())
        startsync.move(10, 250)

        stopsync = QtGui.QPushButton('Stop syncing', top)
        stopsync.setToolTip('This is a sync stopper')
        stopsync.clicked.connect(self.stopscript)
        stopsync.resize(stopsync.sizeHint())
        stopsync.move(470, 250)


        stopsync = QtGui.QPushButton('Clear', top)
        stopsync.setToolTip('Clear')
        stopsync.clicked.connect(self.clearscreen)
        stopsync.resize(stopsync.sizeHint())
        stopsync.move(250, 250)         


        bottom = QtGui.QFrame(self)
        bottom.setFrameShape(QtGui.QFrame.StyledPanel)
        
        
        self.reviewEdit = QtGui.QTextEdit(bottom)
        self.reviewEdit.resize(580,500)
        self.reviewEdit.insertPlainText("Steps to follow:\n\n")
        self.reviewEdit.insertPlainText("1. Select the local folder to sync\n")
        self.reviewEdit.insertPlainText("2. Enter the host address (eg. 192.168.0.107)\n")
        self.reviewEdit.insertPlainText("3. Enter username\n")
        self.reviewEdit.insertPlainText("4. Enter the path to the remote directory. The initial value is root directory\n\n\n")
        
        
        

        splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(top)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))




 
    def clearscreen(self):
        self.reviewEdit.clear()    	
    	

    def testLoop(self):


        while (not self.stopthread.is_set()):
		    p = subprocess.Popen(["unison "+self.path1+" "+"ssh://"+self.usr+"@"+self.hst+"/"+self.dirt+" -ui text -batch -terse -copythreshold 10240 -copyprogrest rsync -contactquietly"], shell = True, stdout = subprocess.PIPE)
		    # print self.path1+" "+"ssh://"+self.usr+"@"+self.hst+"/"+self.dirt
		    stdout, stderr = p.communicate()
		    self.reviewEdit.insertPlainText("....SYNCING....\n")
		    self.reviewEdit.insertPlainText(stdout)

		    self.show()
		    time.sleep(3)



        
        
        
    def showDialog(self):
    	
    	self.path1 = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
    	self.path1 = self.path1.replace(" ","\ ")
    	self.reviewEdit.insertPlainText("The folder "+self.path1+"has been selected to sync\n")


    def startscript(self):
    
		self.usr = self.username.text()
		self.hst = self.hostname.text()
		self.dirt = self.dirname.text()


		self.stopthread = threading.Event()
		t1 = threading.Thread(target=self.testLoop).start()
		self.reviewEdit.insertPlainText("The syncing started\n")
			

    def stopscript(self):
    	self.stopthread.set()
    	self.reviewEdit.insertPlainText("The syncing has been stopped\n")
     


class Main_Window(QtGui.QMainWindow):
    
    def __init__(self):
        super(Main_Window, self).__init__()
        self.form_widget = Secondary_Window(self)
        self.setCentralWidget(self.form_widget)
 
        self.setToolTip('This is a <b>QWidget</b> widget')

        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)  
        
        self.setFixedSize(600, 700)
        #self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('SSH sync')    
        self.show()

    def quitAction(self):
    	QtCore.QCoreApplication.instance().quit
    	runscript = False


def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Main_Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
