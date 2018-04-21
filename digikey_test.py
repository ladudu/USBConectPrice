# -*- coding:utf-8 -*-
"""
https://www.digikey.com.cn/products/zh/%E8%BF%9E%E6%8E%A5%E5%99%A8-%E4%BA%92%E8%BF%9E%E5%99%A8%E4%BB%B6/USB-DVI-HDMI-%E8%BF%9E%E6%8E%A5%E5%99%A8/312?formName=KeywordSearchForm&pageNumber=1&sort=&sortDescending=&sortType=&qtyRequested=&c=312&keywords=&PV=17422%7C4279299212%7C%E8%A7%84%E6%A0%BC&auto=false
"""
import urllib2
import urllib
import re
def WriteFile(filename,src):
    with open(filename,'w') as f:
        f.write(src)
def ReadFile(filename):
    with open(filename,'r') as f:
        f.read()
ua_headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"
}
url = "https://www.digikey.com.cn/products/zh/%E8%BF%9E%E6%8E%A5%E5%99%A8-%E4%BA%92%E8%BF%9E%E5%99%A8%E4%BB%B6/USB-DVI-HDMI-%E8%BF%9E%E6%8E%A5%E5%99%A8/312?formName=KeywordSearchForm&pageNumber=1&sort=&sortDescending=&sortType=&qtyRequested=&c=312&keywords=&PV=17422%7C4279299212%7C%E8%A7%84%E6%A0%BC&auto=false"

request = urllib2.Request(url,headers = ua_headers)
# 返回类文件对象
# urlopen不支持构造http请求
response = urllib2.urlopen(request)

html = response.read()
WriteFile("data.txt",html)
#ReadFile("data.txt")
pattern = re.compile("")
print response.getcode()