#! usr/bin/env python
# -*- coding:utf8 -*-
__author__ = 'SJM'

import urllib2
import urllib
import re

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class BDTB():

    def __init__(self,baseUrl,seeLZ,floortag):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
        self.tools = Tools()
        self.defaultTitle = u"百度贴吧"
        self.floor = 1
        self.floorTag = floortag

    def getPage(self,pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'
            headers = {'User-Agent':user_agent}
            request = urllib2.Request(url,headers=headers)
            response = urllib2.urlopen(request)
            # print response.read()
            return response.read().decode('utf-8')
        except urllib2.URLError,e:
            if hasattr(e,'code'):
                print e.code
            if hasattr(e,'reason'):
                print e.reason

    def getTitle(self):
        page = self.getPage(1)
        #print page
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
        result = re.search(pattern,page)
        if result:
            print result.group(1)
            return result.group(1).strip()
        else:
            print 'not find'
            return None
        # result = re.findall(pattern,page)
        # for res in result:
        #     print res
        # if result:
        #     print result
        #     return result
        # else:
        #     print 'not find'
        #     return None

    def getPageNum(self):
        page = self.getPage(1)
        # print page
        # 以下匹配为tuple类型结果，打印时输出unicode类型
        # pattern = re.compile('<span.*?class="red".*?>(.*?)</span>(.*?)<span.*?class="red">(.*?)</span>(.*?)</li>',re.S)
        pattern = re.compile('<span.*?class="red">(.*?)</span>',re.S)
        PageNum = re.findall(pattern,page)
        #### list(PageNum)    ####代表无效语句
        # print PageNum
        # print PageNum[0]
        # print PageNum[1]
        # for Num in PageNum:
        #     #### page.encode('latin1')
        #     #### page.decode('gbk')
        #     ####  page.decode('utf-8')
        #     #### b = Num.decode('unicode_escape')
        #     #### a = b.encode('utf-8')
        #     for element in Num:
        #         print element
        #     # print Num
        if PageNum:
            return PageNum[0]
        else:
            print "You have a mistake in re.findall"

    def getContent(self,page):
        pattern = re.compile('<div.*?id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        # i = 1
        contents = []
        for item in items:
            # print '\n'
            # print "第%d条"%i
            # print '\n'
            # print item
            # print i,'楼-----------------------------------------------------------------------------------------'
            content = '\n' + self.tools.replace(item) + '\n'
            # print content
            # contents.append(content)
            contents.append(content.encode('utf-8'))
            # i = i + 1
        # for con in contents:
        #     print '\n'
        #     print "第%d条"%i
        #     print '\n'
        #     print con
        #     i = i + 1
        # return items
        return contents

    def openFile(self,title):
        if title is not None:
            self.file = open(title + ".txt",'a')
        else:
            self.file = open(self.defaultTitle + ".txt",'a')

    def writeData(self,contents):
        for item in contents:
            if self.floorTag == 'y' or self.floorTag == 'Y':
                floorline = '\n' + str(self.floor) + u'楼-----------------------------------------------'
                self.file.write(floorline)
            self.file.write(item)
            self.floor += 1

    def start(self):

        # print contents
        title = self.getTitle()
        page = self.getPage(1)
        pageNum = self.getPageNum()
        if pageNum is None:
            print 'URL有误，请确认'
            return
        try:
            print '该帖子共有' + str(pageNum) + '页'
            self.openFile(title)
            for i in range(1,int(pageNum)+1):
                print "正在写入第" + str(i) + "页数据"
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeData(contents)
        except IOError,e:
            print "写入异常，原因" + e.message
        finally:
            print "写入完成"

class Tools():
    def __init__(self):
        #去除img标签，
        self.removeImg = re.compile('<img.*?class=.*?>',re.S)
        #将换行符或双换行符替换为\n
        self.removeBR = re.compile('<br></br>|<br>',re.S)
        #去除超链接标签
        self.removeAddr = re.compile('<a.*?href=.*?>|</a>',re.S)

    def replace(self,x):
        x = re.sub(self.removeImg,'',x)
        x = re.sub(self.removeBR,'\n',x)
        x = re.sub(self.removeAddr,'',x)
        return x.strip()


baseURL = 'http://tieba.baidu.com/p/3138733512'
floorTag = raw_input("请输入y确认是否写入楼层信息，是输入y或Y，否输入其他")
bdtb = BDTB(baseURL,1,floorTag)
# bdtb.getPage(1)
# bdtb.getTitle()
# bdtb.getPageNum()
# bdtb.getContent(bdtb.getPage(1))
bdtb.start()


'''
import urllib2
import urllib

class BDTB():

    def __init__(self):
        self.pageadd = "?see_lz&pn=1"
        self.user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0"
        self.headers = {'User-Agent': self.user_agent}

    def getURL(self,pageadd):
        try:
            url = "http://tieba.baidu.com/p/3138733512" + pageadd
            request = urllib2.Request(url, headers=self.headers)
            response = urllib.urlopen(request)
            print response.read()
            content = response.read().decode('utf8')
            return content
        except urllib2.URLError, e:
            if hasattr(e, 'code'):
                print e.code
            if hasattr(e, 'reason'):
                print e.reason

    def getInfo_louzhu(self):
        postfix = "?see_lz&pn=1"
        content = 
'''













