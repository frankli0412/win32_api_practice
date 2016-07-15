# -*- coding:utf8 -*-

import win32api
import time
# win32api.Beep(500,2000)

# while True:
#     # win32api.MessageBox(0,'hi','nihao')
#     f = open('conf.txt','r')
#     content = f.read().split('#')
#     if content[0] != '0':
#         win32api.MessageBox(0,content[1],content[2])
#     time.sleep(5)


win32api.ShellExecute(0,'open',r'D:\genshuixue\gsx\bin\gsxclient.exe',' ',' ',1)