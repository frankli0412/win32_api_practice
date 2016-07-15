#!usr/bin/env python
# -*- coding:utf-8 -*-

import re
import requests
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8'')


#
# # old_url = 'http://www.jikexueyuan.com/course/android/?pageNum=2'
# # total_page = 20
#
# f = open('source_text','r')
# html = f.read()
# f.close()
#
# pic_url = re.findall('img src="(.*?)" class="lessonimg"',html,re.S)
# i = 0
# for each in pic_url:
#     print 'now downloading:'+each
#     pic = requests.get(each)
#     fp = open('pic\\'+str(i)+'.jpg','wb')
#     fp.write(pic.content)
#     fp.close()
#     i = i + 1
#

class JikeSpider():

    def __init__(self):
        print u'开始爬取内容...'
    def getsourse(self,url):
        html = requests.get(url)
        return html.text
    def changepage(self,url,totol_page):
        now_page = int(re.search('pageNum=(\d+)',url,re.S).group(1))
        page_group = []
        for num in range(now_page,totol_page+1):
            link = re.sub('pageNum=\d+','pageNum=%s'%num,url,re.S)
            page_group.append(link)
        return page_group
    def geteveryclass(self,source):
        everyclass = re.findall('<li id=.*?">(.*?)</li>',source,re.S)
        return everyclass
    def getinfo(self,eachclass):
        classinfo = { }
        classinfo['title'] = re.search('<h2 class="lesson-info-h2"><a.*?">(.*?)</a></h2>',eachclass,re.S).group(1)
        classinfo['content'] = re.search('<p.*?">(.*?)</p>',eachclass,re.S).group(1)
        timeandlevel = re.findall('<em>(.*?)</em>',eachclass,re.S)
        classinfo['classtime'] = timeandlevel[0]
        classinfo['level'] = timeandlevel[1]
        classinfo['learnNum'] = re.search('<em class="learn-number">(.*?)</em>',eachclass,re.S).group(1)
        return classinfo
    def saveinfo(self,classinfo):
        f = open('jikeclassinfo.txt','a')
        i = 1
        for each in classinfo:
            f.writelines('课程%s'%i + '\n')
            f.writelines('title:' + each['title'].encode('utf-8') + '\n')
            f.writelines('content:' + each['content'].encode('utf-8').strip() + '\n')
            x = each['classtime'].encode('utf-8').split('\n')
            # print x
            y = ''.join(x)
            a = y.split('\t')
            b = ''.join(a)
            # print b
            f.writelines('classtime:' + b + '\n')
            f.writelines('level:' + each['level'].encode('utf-8') + '\n')
            f.writelines('learnNum:' + each['learnNum'].encode('utf-8') + '\n' + '\n')
            i = i +1
        f.close()

if __name__ == '__main__':
    classinfo = []
    url = 'http://www.jikexueyuan.com/course/?pageNum=1'
    jike = JikeSpider()
    # firstpagehtml = jike.getsourse(url)
    # print firstpagehtml
    # totalpageNum = re.search('<li class="thpoint pagetotal">(.*?)</li>',firstpagehtml,re.S).group(1)
    # print totalpageNum
    all_link = jike.changepage(url,94)
    for link in all_link:
        # print '\n'
        print '正在处理页面...' + link
        html = jike.getsourse(link)
        everyclass = jike.geteveryclass(html)
        for each in everyclass:
            info = jike.getinfo(each)
            classinfo.append(info)
    jike.saveinfo(classinfo)



