# imple.py

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.resize(250, 150)
widget.setWindowTitle('simple')
# widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
widget.show()

sys.exit(app.exec_())

