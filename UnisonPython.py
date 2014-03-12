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

class Example(QtGui.QWidget):
    
    
    def __init__(self, parent):
        super(Example, self).__init__()

        self.initUI()
        
    def initUI(self):
    

    
    	self.path1 = "Folder 1"
    	self.path2 = "Folder 3"
    	self.stopthread = threading.Event()
        
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        
        hbox = QtGui.QHBoxLayout(self)
 
        top = QtGui.QFrame(self)
        top.setFrameShape(QtGui.QFrame.StyledPanel)
        
        btn1 = QtGui.QPushButton('Select Client Folder', top)
        btn1.setToolTip('This is a <b>QPushButton</b> widget')
        self.path1 = btn1.clicked.connect(self.selectFirstFolder)
        btn1.resize(btn1.sizeHint())
        btn1.move(210, 40)
        
        
        btn = QtGui.QPushButton('Select Server Folder', top)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.clicked.connect(self.selectSecondFolder)
        btn.resize(btn.sizeHint())
        btn.move(210, 80)

        btn = QtGui.QPushButton('Clear screen', top)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.clicked.connect(self.clearscreen)
        btn.resize(btn.sizeHint())
        btn.move(220, 120)

		# Start sync and stop sync buttons
		
        startsync = QtGui.QPushButton('Start syncing', top)
        startsync.setToolTip('This is a sync initializer')
        startsync.clicked.connect(self.startscript)
        startsync.resize(startsync.sizeHint())
        startsync.move(10, 120)

        stopsync = QtGui.QPushButton('Stop syncing', top)
        stopsync.setToolTip('This is a sync stopper')
        stopsync.clicked.connect(self.stopscript)
        stopsync.resize(stopsync.sizeHint())
        stopsync.move(470, 120)        


#############################################################################################################
        
        bottom = QtGui.QFrame(self)
        bottom.setFrameShape(QtGui.QFrame.StyledPanel)
        
        
        self.reviewEdit = QtGui.QTextEdit(bottom)
        self.reviewEdit.resize(580,400)
        

        splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)       
        splitter2.resize(100,100)
        splitter2.addWidget(top)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))

############################################################################################################
    

    def clearscreen(self):
        self.reviewEdit.clear()


    def doit(self):
    	print "Opening a new popup window..."
    	self.w = MyPopup()
    	self.w.setGeometry(QRect(100, 100, 400, 200))
    	self.w.show()  	
        
    def selectFirstFolder(self):
    	
    	self.path1 = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.path1 = self.path1.replace(" ","\ ")
    	self.reviewEdit.insertPlainText("The folder "+self.path1+"has been selected to sync\n")        
    	
    def selectSecondFolder(self):
    
    	self.path2 = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.path2 = self.path2.replace(" ","\ ")
    	self.reviewEdit.insertPlainText("The server side folder to sync into is selected as "+self.path2+"\n")

    	
    def internet_on():
    	try:
    		response=urllib2.urlopen('http://74.125.228.100',timeout=1)
    		return True
    	except urllib2.URLError as err: pass
    	return False

    def startscript(self):
		self.stopthread = threading.Event()
		t1 = threading.Thread(target=self.localLoop).start()
		self.reviewEdit.insertPlainText("The syncing started\n")
			
    def stopscript(self):
    	self.stopthread.set()
    	self.reviewEdit.insertPlainText("The syncing has been stopped\n")

    def localLoop(self): 

        while (not self.stopthread.is_set()):
            p = subprocess.Popen(["unison "+self.path1+" "+self.path2+" -ui text -batch -terse -copythreshold 10240 -copyprogrest rsync -contactquietly"], shell = True, stdout = subprocess.PIPE)
            stdout, stderr = p.communicate()
            self.reviewEdit.insertPlainText("....SYNCING....\n")
            self.reviewEdit.insertPlainText(stdout)
            self.show()
            time.sleep(3)


###################################################################################################################
#################################################ANOTHER CLASS#####################################################
###################################################################################################################
        
class MyPopup(QtGui.QWidget):
	def __init__(self):
		super(MyPopup, self).__init__()
		self.host = QtGui.QLineEdit(self)
		self.host.move(140, 30)
		self.passw = QtGui.QLineEdit(self)
		self.passw.move(140, 60)
		self.passw.setEchoMode(QLineEdit.Password)
		self.enter = QtGui.QPushButton('Enter', self)
		self.enter.clicked.connect(self.handleEnter)
		self.enter.move(140, 110)

        def handleEnter(self):
			hostname1 = self.host.text()
			passwd1 = self.passw.text()
			print hostname1
			print passwd1
 

class Example1(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example1, self).__init__()
        self.form_widget = Example(self)
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
        
        self.setFixedSize(600, 400)
        #self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Tooltips')    
        self.show()

    def quitAction(self):
    	QtCore.QCoreApplication.instance().quit
    	runscript = False


def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example1()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

