#!/usr/bin/python
# coding=utf-8
import urllib
import re


def get_html(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def get_record_fields(rec):
    # 1. remove space and \r\n
    pattern = re.compile(r'>\s*<', re.S)
    sub_text = pattern.sub('><', rec)

    # 2. search for fields in <td></td>
    pattern = re.compile(
            r'.*?<td.*?>(?P<date>.+?)</td>\s*?<td.*?>(?P<number>.+?)</td>\s*?<td.*?>(?P<balls>.+?)</td>\s*?<td.*?>(?P<prize2>.+?)</td>\s*?<td.*?>(?P<prize1>.+?)</td>.*',
            re.I | re.M | re.S)
    m = pattern.search(sub_text)

    date = m.group('date')
    number = m.group('number')
    balls = m.group('balls')
    prize1 = m.group('prize1')
    prize2 = m.group('prize2')
    #print date, number, balls, prize1, prize2

    # 3. search for data in <em></em>
    pattern = re.compile(
            r'<em.*?>(?P<ball1>.+?)</em><em.*?>(?P<ball2>.+?)</em><em.*?>(?P<ball3>.+?)</em><em.*?>(?P<ball4>.+?)</em><em.*?>(?P<ball5>.+?)</em><em.*?>(?P<ball6>.+?)</em><em>(?P<ball7>.+?)</em>',
            re.I | re.M | re.S)
    # print pattern.groupindex
    m2 = pattern.search(balls)
    # print pattern.groups()
    red = m2.group('ball1') + ',' + m2.group('ball2') + ',' + m2.group('ball3') + ',' + m2.group('ball4') + ',' + m2.group('ball5') + ',' + m2.group('ball6')
    blue = m2.group('ball7')

    pattern = re.compile(r'<strong>(?P<prize>.+?)</strong>.*', re.I | re.M | re.S)
    m2 = pattern.search(prize1)
    prize1 = m2.group('prize')

    m2 = pattern.search(prize2)
    prize2 = m2.group('prize')

    result = {'date': date, 'number': number, 'red': red, 'blue': blue, 'prize1': prize1, 'prize2': prize2}
    return result


# main start
html = get_html("http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html")

records = re.findall(r'<tr>.*?<em.*?</tr>', html, re.I | re.M | re.S)

i = 0
for record in records:
    i += 1
    print 'record ' + str(i) + ': ' + str(get_record_fields(record))
