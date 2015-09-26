#!/usr/bin/python
# --coding=utf-8--
# 登录窗口
# author Ningerjohn
# ctime 2015年9月25日10:23:21
# 
# 
# 
from Tkinter import *
import ttk

root = Tk()
# 窗体名字
root.title('eCho')
# 窗口大小和位置
root.geometry('230x300+950+400')
# 设置窗体背景颜色
root['bg'] = '#eeeeee'
# root['bg'] = 'black'

# 延迟显示
# root.after(5000, root.config(background='black'))
# print root.geometry()
# print root.config()
# 
avatarlabel = Label(root, width=20, background='white')
avatarlabel.config(height=20)

avatarlabel.pack() 
# 用户名输入框
usernameEntry = Entry(root, width='20')
usernameEntry.insert(0, 'username') # 从0位置开始插入提示
usernameEntry.pack()
print usernameEntry.config()
# 密码输入框
passwordEntry = ttk.Entry(root)
passwordEntry.config(show='*')
passwordEntry.pack()



root.mainloop()
