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

# app = QtGui.QApplication(sys.argv) # 声明一个application对象

# Step #1 创建一个窗口
# widget = QtGui.QWidget() # 创建一个没有父级对象的组件，也就是窗口
# widget.resize(300,200) # (width, height)改变窗体的大小	
# widget.setWindowTitle('Simple') # 设置窗口的名称
# widget.show() # 显示窗口


# sys.exit(app.exec_())


# Step #2 应用的图标
# class Example(QtGui.QWidget): # 继承QWidget工具组件类
# 	"""docstring for Example"""
# 	def __init__(self):
# 		super(Example, self).__init__()
# 		self.initUI() # 调用自己的方法initUI
# 	# 声明一个initUI方法，用来设置工具组件的属性，包括大小，位置，窗体名字
# 	def initUI(self):
#
# 		self.setGeometry(300, 300, 250, 150) # 设置窗口位置
# 		self.setWindowTitle('eCho') # 设置窗口名字
# 		self.setWindowIcon(QtGui.QIcon('./static/img/logo.png')) # 调用logo并设置
# 		self.show() # 显示这个工具组件
#
# # 声明一个函数main
# def main():
# 	app = QtGui.QApplication(sys.argv) # 创建QApplication对象用于执行Qt Gui 程序
# 	ex = Example() # 实例化Example类
# 	sys.exit(app.exec_()) # 应用程序开始执行，结束时sys类会自动清理
#
# if __name__ == '__main__':
# 	main()


# Step #3 显示提示


class Tooltip(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self,parent)

		self.setGeometry(300,300,250,150)
		self.setWindowTitle('Tooltip') # 设置窗体名字

		self.setToolTip('This is a <b>QWidget</b> widget') # 设置提示内容
		QtGui.QToolTip.setFont(QtGui.QFont('Calibre', 10)) # 设置提示内容的字体和大小
		self.show()


app = QtGui.QApplication(sys.argv)
tooltip = Tooltip() # 实例化Tooltip类
# tooltip.show() # 显示出来
sys.exit(app.exec_())








