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

#html.replace('\n', '')

dr = re.compile(r'>\s*<',re.S)
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
print p.groupindex

m = p.search(html)

# print m.groups()
print 'date: ' + m.group('date')
print 'id: ' + m.group('id')
print 'balls: ' + m.group('balls')
print 'prize1: ' + m.group('prize1')
print 'prize2: ' + m.group('prize2')
