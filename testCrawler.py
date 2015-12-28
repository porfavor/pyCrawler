#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
import re

html = """
        <tr>
          <td align="center">2015-11-10</td>
          <td align="center">2015132</td>
          <td align="center" style="padding-left:10px;">

          <em class="rr">03</em>

          <em class="rr">05</em>

          <em class="rr">11</em>

          <em class="rr">28</em>

          <em class="rr">30</em>

          <em class="rr">33</em>

          <em>01</em></td>
          <td><strong>324,697,916</strong></td>
          <td align="left" style="color:#999;"><strong>7</strong>
          (冀 蒙 黑 皖..)
          </td>
          <td align="center"><strong class="rc">72</strong></td>
          <td align="center">
          <a href="http://www.zhcw.com/ssq/kjgg/" target="_blank"><img src="http://images.zhcw.com/zhcw2010/kaijiang/zhcw/ssqpd_42.jpg" width="16" height="16" align="absmiddle" title="详细信息"/></a>
          <a href="http://www.zhcw.com/video/kaijiangshipin/" target="_blank"><img src="http://images.zhcw.com/zhcw2010/kaijiang/zhcw/ssqpd_43.jpg" width="16" height="16" align="absmiddle" title="开奖视频"/></a>
          </td>
        </tr>
"""

# html.replace('\n', '')

dr = re.compile(r'>\s*<', re.S)
dd = dr.sub('><', html)
print dd
# print html


# pattern = re.compile(r'<em.*?</em>', re.I | re.M | re.S)
# m = pattern.findall(html)
#
# i=0
# for val in m:
#     i += 1
#     #print i
#     print "String[" + str(i) + "]: " + val


# p = re.compile(r'(?P<name>[a-z]+)\s+(?P<age>\d+)\s+(?P<tel>\d+).*', re.I)

p = re.compile(
        r'.*?<td.*?>(?P<date>.+?)</td>\s*?<td.*?>(?P<id>.+?)</td>\s*?<td.*?>(?P<balls>.+?)</td>\s*?<td.*?>(?P<prize1>.+?)</td>\s*?<td.*?>(?P<prize2>.+?)</td>.*',
        re.I | re.M | re.S)
# print p.groupindex

m = p.search(dd)
# print m.groups()

# balls = re.sub(r'>\s*<', '><', m.group('balls'), re.S)
# balls = re.sub(r'\s*', '', balls, re.S)

date = m.group('date')
id = m.group('id')
balls = m.group('balls')

p2 = re.compile(
    r'<em.*?>(?P<ball1>.+?)</em><em.*?>(?P<ball2>.+?)</em><em.*?>(?P<ball3>.+?)</em><em.*?>(?P<ball4>.+?)</em><em.*?>(?P<ball5>.+?)</em><em.*?>(?P<ball6>.+?)</em><em>(?P<ball7>.+?)</em>',
    re.I)
#print p2.groupindex
m2 = p2.search(m.group('balls'))
#print m2.groups()
red = m2.group('ball1') + ',' + m2.group('ball2') + ',' + m2.group('ball3') + ',' + m2.group('ball4') + ',' + m2.group('ball5') + ',' + m2.group('ball6')
blue = m2.group('ball7')

p2 = re.compile(r'<strong>(?P<prize>.+)</strong>')
m2 = p2.search(m.group('prize1'))
prize1 = m2.group('prize')

m2 = p2.search(m.group('prize2'))
prize2 = m2.group('prize')

print 'date: ' + date
print 'id: ' + id
print 'red: ' + red
print 'blue: ' + blue
print 'prize1: ' + prize1
print 'prize2: ' + prize2
