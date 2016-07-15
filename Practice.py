#!usr/bin/env python
# -*- coding:utf-8 -*-

import BeautifulSoup
import urllib2


class staGovReport():

    def __init__(self):
        pass

    def getPage(self):
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0"
        headers = {'User-Agent':user_agent}
        url = 'http://www.gov.cn/guowuyuan/2016-03/05/content_5049372.htm'
        try:
            request = urllib2.Request(url=url,headers=headers)
            response = urllib2.urlopen(request)
            # print response.read()
            return response.read().decode('utf-8')

        except urllib2.URLError,e:
            if hasattr(e,'code'):
                print e.code
            if hasattr(e,'reason'):
                print e.reason

    def getContent(self):
        page = str(self.getPage())
        soup = BeautifulSoup(page)
        print soup.p

    def debug(self):
        # self.getPage()
        self.getContent()

GovReport = staGovReport()
GovReport.debug()