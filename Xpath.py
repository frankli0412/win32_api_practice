#!usr/bin/env python
# -*- coding:utf-8 -*-

from lxml import etree
import requests

class JikePythonClass():
# url = 'http://www.jikexueyuan.com/path/python/'
# html = requests.get(url)
    def __init__(self):
        print '开始爬取极客Python体系课程...'
    def getsource(self,url):
        con = requests.get(url)
        return str(con)
    def geteverypart(self,html):
        selector = etree.HTML(html)
        partcontent = selector.xpath('//*[@id="container"]/div/div[6]')
        return partcontent
    def getclass(self):
        pass
    def saveinfo(self):
        pass


if __name__ == '__main__':
    part = []
    classinfo = []
    url = 'http://www.jikexueyuan.com/path/python/'
    jikepython = JikePythonClass()
    html = jikepython.getsource(url)
    # selector = etree.HTML(html)
    # content = selector.xpath()
    part = jikepython.geteverypart(html)
    for i in part:
        print i
    for eachpart in part:
        content = jikepython.getclass(eachpart)
        for eachclass in content:
            classinfo.append(eachclass)

    # for a in classinfo:
    #     print a
    # jikepython.saveinfo(classinfo)

