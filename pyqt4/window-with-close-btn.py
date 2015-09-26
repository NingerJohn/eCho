# encoding:utf-8
#!/usr/bin/python
# @author NingerJohn
# @ctime 2015年9月25日21:16:09
# 
# 
# 
# 
from PyQt4 import QtGui,QtCore
# from PyQt4. import *
import sys

class demowind(QtGui.QWidget):
	"""docstring for dwmowind"""
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setGeometry(300,300,200,200)
		self.setWindowTitle('Demo Window')
		quit = QtGui.QPushButton('Close',self)
		quit.setGeometry(20,10,70,40) # x,y,width, height
		self.connect(quit, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))

app = QtGui.QApplication(sys.argv)
dw = demowind()
dw.show()
sys.exit(app.exec_())
		



