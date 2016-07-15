# -*-coding:utf-8-*-

# def verify(num):
#     if num > 0:
#         print "正数"
#     if num < 0:
#         print "负数"
#     if num == 0:
#         print "零"
# num = float(raw_input("请输入一个数："))
# verify(num)

# list = [2,7,6,8,10]
# print sum(list)
# avg = float(sum(list))/float(len(list))
# print avg

# list = []
# try:
#     num = raw_input("请输入5个数字，以逗号隔开：")
#     for i in num.split(','):
#         list.append(float(i))
#     avg = float(sum(list))/float(len(list))
#     print avg
# except:
#     print "输入有误"

# a = raw_input("请输入一个字符串：")
# # for i in a:
# #     print i
# i = 0
# while i < len(a):
#     print a[i]
#     i = i + 1

# while True:
#     num = raw_input("请输入一个0到100的数：")
#     try:
#         if float(num) > 0 and float(num) < 100:
#             print "OK"
#             break
#         else:
#             print "输入的数错误，请重新输入"
#     except :
#         print "输入的不是数字"

#
# stack = []  #定义堆栈列表
#
# def pushit():
#     stack.append(raw_input('Enter new string:').strip())
#
# def popit():
#     if len(stack) == 0:
#         print 'Cannot pop from an empty stack!'
#     else:
#         print 'Removed [','stack.pop()',']'
#
# def viewstack():
#     print stack
#
# CMDs = {'u':pushit,'o':popit,'v':viewstack}
# def showmenu():
#     pr = """
# p(U)sh
# p(O)p
# (V)iew
# (Q)uit
# Enter choice:
#     """
#     while True:
#         while True:
#             try:
#                 choice = raw_input(pr).strip()[0].lower()
#             except (EOFError,KeyboardInterrupt,IndexError):
#                 choice = 'q'
#             print '\nYou picked:[%s]' % choice
#             if choice not in 'uovq':
#                 print 'Invalid option,try again'
#             else:
#                 break
#
#         if choice == 'q':
#             break
#
#         CMDs[choice]()
#
# if __name__ == '__main__':
#     showmenu()


# db = {}
#
# def newuser():
#     prompt = 'login desired:'
#     while True:
#         name = raw_input(prompt)
#         if name in db.keys():
#             prompt = "name taken,try another:"
#             continue
#         else:
#             break
#     pwd = raw_input("passwd:")
#     db[name]=pwd
#
# def olduser():
#     name = raw_input("login:")
#     pwd = raw_input("passwd:")
#     passwd = db.get(name)
#     if passwd == pwd:
#         print 'welcome back ',name
#     else:
#         print "login incorrect"
#
# def showmenu():
#     prompt = """
#     (N)ew User Login
#     (E)xisting User Login
#     (Q)uit
#     Enter choice:
#         """
#     done = False
#     while not done:
#         chosen = False
#         while not chosen:
#             try:
#                 choice = raw_input(prompt).strip()[0].lower()
#             except (EOFError,KeyboardInterrupt):
#                 choice = 'q'
#             print '\nYou picked:[%s]' % choice
#             if choice not in 'neq':
#                 print 'invalid option,try again'
#             else:
#                 chosen = True
#                 done = True
#
# newuser()
# olduser()
# if __name__ == "__main__":
#     showmenu()

# #float_v1.0
# def safe_float(obj):
#     try:
#         return float(obj)
#     except ValueError:
#         pass

#float_v1.1
# def safe_float(obj):
#     try:
#         retval = float(obj)
#     except ValueError:
#         retval = "could not convert non-number to float"
#     except TypeError:
#         retval = "object type cannot be converted to float"
#     return retval
#
# aaa = safe_float([111,222])
# print aaa


# import xlrd
# log = open('logfile.txt','w')
# try:
#     xlrd.function()
# except:
#     log.write("*** caught exception in module\n")
# else:
#     log.write("*** no exceptions caught\n")
# log.close()



# from time import ctime,sleep
# def tsfunc(func):
#     def wrappedFunc():
#         print "[%s] %s() called" % (ctime(),func.__name__)
#         return func()
#     return wrappedFunc
# @tsfunc
# def foo():
#     pass
# foo()
# sleep(4)
# for i in range(2):
#     sleep(1)
#     foo()



# def convert(func,seq):
#     "conv.sequence of numbers to same type"
#     return [func(eachNum) for eachNum in seq]
# myseq = (123,45.67,-6.2e8,9999999L)
# print convert(int,myseq)
# print convert(long,myseq)
# print convert(float,myseq)


# def \
#     taxMe(cost,rate = 0.0825):
#     return cost + (cost * rate)
# print taxMe(100)
# print taxMe(100,0.05)



# from urllib import urlretrieve
# def firstNonBlank(lines):
#     for eachLine in lines:
#         if not eachLine.strip():
#             continue
#         else:
#             return eachLine
#
# def firstLast(webpage):
#     f = open(webpage)
#     lines = f.readlines()
#     f.close()
#     print firstNonBlank(lines)
#     lines.reverse()
#     print firstNonBlank(lines)
#
# def download(url = 'http://www.baidu.com',process = firstLast):
#     try:
#         retval = urlretrieve(url)[0]
#     except IOError:
#         retval = None
#     if retval:
#         process(retval)
# if __name__ == '__main__':
#     download()


# #GUI小例
# from functools import partial
# import Tkinter
# root = Tkinter.Tk()
# MyButton = partial(Tkinter.Button,root,fg='white',bg='blue')
# b1 = MyButton(text='Button 1')
# b2 = MyButton(text='Button 2')
# qb = MyButton(text='Quit',bg='red',command=root.quit)
# b1.pack()
# b2.pack()
# qb.pack(fill=Tkinter.X,expand=True)
# root.title('PFAs!')
# root.mainloop()



# def countToFour1():
#     for eachNum in range(5):
#         print eachNum
#
# def countToFour2(n):
#     for eachNum in range(n,5):
#         print eachNum
#
# def countToFour3(n=1):
#     for eachNum in range(n,5):
#         print eachNum
#
# # countToFour1()
# countToFour2(5)
# countToFour3(5)



# a = map(None,[1,2,3],['abc','edf','bbb','ddd'])
# print a


# #调用sys.exit()退出
# import sys
# def usage():
#     print 'At Least 2 arguments (inc1.cmd name).'
#     print 'usage:args.py arg1 arg2 [arg3...]'
#     sys.exit(1)
#
# argc = len(sys.argv)
# if argc<3:
#     usage()
#     print "number of args entered:",argc
#     print "args (inc1.cmd name) were:".sys.argv


# import sys
# prev_exit_func = getattr(sys,'exitfunc',None)
# def my_exit_func(old_exit = prev_exit_func):
#     #perform cleanup 进行清理
#     if old_exit is not None and callable(old_exit):
#         old_exit()
#
# sys.exitfunc = my_exit_func()


#单线程例子
# from time import sleep,ctime
#
# def loop0():
#     print 'start loop0 at:',ctime()
#     sleep(4)
#     print 'loop0 done at:',ctime()
#
# def loop1():
#     print 'start loop1 at:',ctime()
#     sleep(2)
#     print 'loop1 done at:',ctime()
#
# def main():
#     print 'starting at:',ctime()
#     loop0()
#     loop1()
#     print 'all DONE at :',ctime()
#
# if __name__ == '__main__':
#     main()

# 多线程例子
# import thread
# from time import sleep,ctime
#
# def loop():
#     print 'start loop0 at:',ctime()
#     sleep(4)
#     print 'loop0 done at:',ctime()
#
# def loop1():
#     print 'start loop1 at:',ctime()
#     sleep(2)
#     print 'loop1 done at:',ctime()
#
# def main():
#     print 'starting at:', ctime()
#     thread.start_new_thread(loop(), ())
#     thread.start_new_thread(loop1(), ())
#     sleep(6)
#     print 'all Done at:', ctime()
#
# if __name__ == '__main__':
#     main()

# import thread
# from time import sleep,ctime
#
# loops = [4,2]
#
# def loop(nloop,nsec,lock):
#     print 'start loop',nloop,'at:',ctime()
#     sleep(nsec)
#     print 'loop',nloop,'done at:',ctime()
#     lock.release()
#
# def main():
#     print 'starting at:',ctime()
#     locks = []
#     nloops = range(len(loops))
#
#     for i in loops:
#         lock = thread.allocate_lock()
#         lock.acquire()
#         locks.append(lock)
#
#     for i in nloops:
#         thread.start_new_thread(loop,(i,loops[i],locks[i]))
#
#     for i in nloops:
#         while locks[i].locked():
#             pass
#
#     print 'all DONE at:',ctime()
#
# if __name__ == '__main__':
#     main()



# import Tkinter
# label = Tkinter.Label(top,text = 'Hello World !')
# label.pack()
#
# quit = Tkinter.Button(top,text = 'Quit',command = top.quit,bg = 'red',fg = 'blue')
# quit.pack(fill = Tkinter.X,expand = 1)


# from Tkinter import *
# def resize(ev = None):
#     label.config(font = 'Helvetica -%d bold' % scale.get())
# top = Tk()
# top.geometry('250x250')
# label = Label(top,text = '孟庆秀',font = 'Helvetica -12 bold')
# label.pack(fill = Y,expand = 1)
#
# scale = Scale(top,from_ = 10,to = 40,orient = HORIZONTAL,command = resize)
# scale.set(12)
# scale.pack(fill = X,expand = 1)
#
# quit = Button(top,text = "Quit",command = top.quit,activeforeground = 'white',activebackground = 'red')
# quit.pack()
#
#
# mainloop()


# def sum_jc(n):
#     sum_n = 0
#     for i in range(n):
#         jc = 1
#         for j in range(i+1):
#             jc = jc*(j+1)
#         sum_n = sum_n + jc
#     return sum_n
# if __name__ == '__main__':
#     m = sum_jc(20)
#     print m

# def get_num(a):
#     list = []
#     no = 0
#     for i in a:
#         for j in a:
#             for m in a:
#                 sum = i*100 + j *10 + m
#                 list.append(sum)
#                 # print sum
#                 no = no + 1
#     return list,no
# if __name__ == '__main__':
#     list = [1,2,3,4]
#     res,no = get_num(list)
#     print no
#     print res
#     # for i in res:
#     #     print i

# def reward(profit):
#     if profit*10000<=100000:
#         res = profit*10000*0.1
#     if 100000<profit*10000<200000:
#         res = 100000*0.1 + (profit*10000-100000)*0.075
#     if

# import math
# i = 1
# while True:
#     i = i + 1
#     if int(sqrt())

import re

secret_code = 'honohoihbpihbxxIxx112dsfowjfn2oxxlovexx9ohhdfwxxyouxxjph23h'

# .的使用举例
# a = 'xy123'
# b = re.findall('x.',a)
# print b

# *的使用举例
# a = 'xxyx1x23'
# b = re.findall('x*',a)
# print b

# ?的使用举例
# a = 'xxyx12x3'
# b = re.findall('x?',a)
# print b

# .*的使用举例
b = re.findall('xx.*xx',secret_code)
print b

c = re.findall('xx.*?xx',secret_code)
print c

d = re.findall('xx(.*?)xx',secret_code)
print d


