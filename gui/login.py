# encoding: utf-8
#!/usr/bin/python
# author NingerJohn
# createtime 2015年9月25日19:13:31


# import PyQt4 Module
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
# import system Module
import sys

class MainWindow(QMainWindow):
	"""docstring for MainWindow"""
	
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		
		self.setWindowTitle('eCho') # 设置窗体名字

		# Apply a label widget into window
		label = QLabel(u"欢迎使用eCho")
		label.setAlignment(Qt.AlignCenter)

		self.setCentralWidget(label)
		

app = QApplication(sys.argv) # 调用QApplication类

# window = MainWindow()
# window.show()

# create window
root = QMainWindow()
root.setWindowTitle('Test')
root.show()

# add menu into root window
menu = QMenuBar(parent=root)
menu.addMenu('Test')
menu.show()

# add a button into root window
btn = QPushButton('Hello world!', parent=root)
btn.show()




app.exec_() # 执行exec_方法

















