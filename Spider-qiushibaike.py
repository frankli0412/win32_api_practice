#!usr/bin/env python
# -*- coding:utf8 -*-

import urllib2
import urllib
import re
import os

#解决报错：UnicodeEncodeError ----- 'ascii' codec can't encode characters in position问题
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )



class QSBK():
    #初始化方法，定义一些变量
    def __init__(self):
        self.pageNum = 5  #用于循环获取指定页数的内容
        self.pageIndex = 1  #指定第一页
        self.usr_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0"
        self.headers = {'User-Agent':self.usr_agent}
        self.stories = []
        self.enable = False

    #输入某一页的索引获得页面内容
    def getPage(self,pageIndex):
        try:
            url = "http://www.qiushibaike.com/hot/page/" + str(pageIndex)
            request = urllib2.Request(url,headers=self.headers)
            response = urllib2.urlopen(request)
            #print response.read()
            content = response.read().decode('utf-8')
            return content

        except urllib2.URLError,e:
                if hasattr(e,'code'):
                    print e.code
                if hasattr(e,'reason'):
                    print e.reason

    #输入某一页内容，获得该页的作者和文字段子
    def getPageItems(self,filen,):
        while self.pageIndex <= self.pageNum:
            content=self.getPage(self.pageIndex)
            pattern = re.compile('<h2>(.*?)</h2>.*?<div.*?class="content">(.*?)</div>',re.S)
            items = re.findall(pattern,content)
            filen.write('\n'*6 +"第"+str(self.pageIndex)+"页"+'\n'*6 )
            #print items
            for item in items:
                print item[0],item[1]
                filen.write(item[0])
                filen.write(item[1])
            self.pageIndex = self.pageIndex + 1


    #获取数据并输入txt文件中
    def start(self):
        f = open("python-qiushibiake.txt",'a')
        self.getPageItems(f)

        f.close()

spider = QSBK()
spider.start()







'''
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class'+
                         '="content".*?title="(.*?)">(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        haveImg = re.search("img",item[3])
        if not haveImg:
            print item[0],item[1],item[2],item[4]
            print 'ok11'
        print 'ok22'
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
'''





