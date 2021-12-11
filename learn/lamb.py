#!/usr/bin/python3

"""这里使用的模块是tkinter
    后面可以尝试使用curses模块——基于屏幕文本编辑，来编写代码"""

__author__ = 'liushuai'
__version__ = '0.0.1'
# from tkinter import *
# top = Tk()
#
# li = ['C', 'python', 'php', 'html', 'SQL', 'java']
# movie = ['CSS', 'jQuery', 'Bootstrap']
# listb = Listbox(top)  # 创建两个列表组件
# listb2 = Listbox(top)
# for item in li:  # 第一个小部件插入数据
#     listb.insert(0, item)
#
# for item in movie:  # 第二个小部件插入数据
#     listb2.insert(0, item)
#
# listb.pack(side='left')  # 将小部件放置到主窗口中
# listb2.pack(side='right')
# # 进入消息循环
# top.mainloop()

import os
import tkinter
from tkinter.scrolledtext import ScrolledText

def do_open():
    # 打开文件
    file_path = entry_file.get()  # 获取文本框的内容
    with open(file_path) as fr:
        # 打开文件
        content = fr.read()  # 一次性读取文件内容，对大文件不宜使用
        text.delete(0.0, tkinter.END)  # 清空文本框内容
        text.insert(tkinter.END, content)  # 在光标后插入内容


def do_save():
    # 保存文件
    content = text.get(0.0, tkinter.END)  # 获取文本框内容
    file_path = entry_file.get()  # 文件路径
    with open(file_path, 'w') as fw:
        fw.write(content)


def create_file_and_edit():
    '''makeTextFile.py -- create text file'''
    while True:
        fname = entry_file.get()  # 获取文本框的内容
        if os.path.exists(fname):
            text.insert(tkinter.END, "ERROR: '%s' already exists" % fname)
        else:
            text.delete(0.0, tkinter.END)  # 清空文本框内容
            break
    text.insert(tkinter.END, "DONE,and start to edit:>%s".format(os.linesep))


def cancel():
    do_open()


if __name__ == '__main__':
    win = tkinter.Tk()  # 创建窗口
    win.title('文本编辑器')  # 设置标题
    win.geometry('800x600')  # 设置窗口大小

    entry_file = tkinter.Entry(win)  # 创建一个文本输入框
    entry_file.pack(side='left')  # 放置该输入框

    # text = tkinter.Text(win)  # 创建多行文本框，用于编辑文件
    text = ScrolledText()

    btn_open = tkinter.Button(win, text='open', command=do_open)  # 创建按钮用于打开文件
    btn_save = tkinter.Button(win, text='save', command=do_save)  # 创建按钮用于保存文件
    btn_create = tkinter.Button(win, text='create', command=create_file_and_edit)
    btn_cancel = tkinter.Button(win, text='cancel', command=do_open)  # 创建按钮用于取消新建的内容（重新打开文件）

    btn_open.pack(side='top', expand=False)
    btn_save.pack(side='top')
    btn_create.pack(side='top')
    btn_cancel.pack(side='top')
    # text.pack(side='bottom')
    text.pack(side='bottom', expand=True, fill='y')

    win.mainloop()  # 进入消息循环