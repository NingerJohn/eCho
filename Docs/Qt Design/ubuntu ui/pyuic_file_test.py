from PyQt4 import *
from echo import *
import sys
if __name__ == "__main__":
		app = QtGui.QApplication(sys.argv)
		f = Ui_mainWindow()
		f.setupUi()
		app.setMainWidget(f)
		app.exec_loop()
