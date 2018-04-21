# -*- coding:utf-8 -*-

import urllib2
import urllib
import random
"""
爬虫和反爬虫第一步
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36
"""
ua_headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"
}
url = "http://www.baidu.com/s"

keyword = raw_input("百度一下:")
wd = {"wd" : keyword}
wd = urllib.urlencode(wd)

fullurl = url + "?" + wd

print fullurl
request = urllib2.Request(fullurl,headers = ua_headers)
# 返回类文件对象
# urlopen不支持构造http请求
response = urllib2.urlopen(request)

html = response.read()
print(html)
#返回200 成功,4开头服务器页面问题,5开头服务器问题
#print response.getcode()

#print response.geturl()

#print response.info()
"""
Mosaic 世界第一个浏览器 美国国家计算机应用中心
Netscape-网景 Netscape(支持框架)
微软-Internet explorer

Mozilla基金:Firefox 内核(Gecko内核)

内核:
IE : Trident
KHTML(Linux),lke Gecko
Webkit(Apple),like KHTML
Chrome,like Webkit
Opera,Presto
"""