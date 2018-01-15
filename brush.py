#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8
#Filename:urllib2-header.py
  
import urllib2
import sys
import time

import random

def random_ip():
    a = random.randint(1, 255)
    b = random.randint(1, 255)
    c = random.randint(1, 255)
    d = random.randint(1, 255)
    return "%d.%d.%d.%d" % (a, b, c, d)

def task(ip):
    #抓取网页内容-发送报头-1
    url= "http://baidu.com?x=131089"
    #ip = "61.135.45.20"
    send_headers = {
      'Host':'www.baidu.com',
      'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
      'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Connection':'keep-alive',
      "X-Forwarded-For": ip,
    }
          
    req = urllib2.Request(url,headers=send_headers)
    r = urllib2.urlopen(req)
      
    html = r.read()        #返回网页内容
    receive_header = r.info()     #返回的报头信息
      
    # sys.getfilesystemencoding() 
    #html = html.decode('utf-8','replace').encode(sys.getfilesystemencoding()) #转码:避免输出出现乱码 
      
    print receive_header
    # print '####################################'
    #print html

for i in range(50):
    ip = random_ip()
    print "cur:%d, %s" % (i, ip)
    task(ip)

    time.sleep(random.randint(1, 10))
