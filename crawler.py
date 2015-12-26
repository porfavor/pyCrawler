#!/usr/bin/python
# coding=utf-8
import urllib
import re


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


# def getInfo(html):


html = getHtml("http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html")

list = re.findall(r'<tr>.*?<em.*?</tr>', html, re.I | re.M | re.S)

i = 0
for val in list:
    i += 1
    # print str(i) + ':'
    print val


# pattern = re.compile(r'(<td.*?>?P<date></td>)\s+(<td.*?>?P<no></td>)\s+.*', re.I)
# m=p.search(s)