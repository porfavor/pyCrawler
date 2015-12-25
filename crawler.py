#!/usr/bin/python
# coding=utf-8
import urllib
import re


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


html = getHtml("http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html")

m = re.search("<tr>.*</tr>", html, re.I | re.M | re.S)

if m:
    print "m.groups() : ", m.groups()
    print "m.group(1) : ", m.group()
    # print "m.group(2) : ", m.group(2)
else:
    print "No match!!"


