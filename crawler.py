#!/usr/bin/python
# coding=utf-8
import urllib
import re
import traceback
import MySQLdb

global web_address, url, page_num
web_address = 'http://kaijiang.zhcw.com'
url = '/zhcw/inc/ssq/ssq_wqhg.jsp?pageNum='
page_num = 1


def get_html(url):
    page = urllib.urlopen(url)
    text = page.read()
    return text


def get_record_fields(rec):
    # 1. remove space and \r\n
    pattern = re.compile(r'>\s*<', re.S)
    sub_text = pattern.sub('><', rec)

    # 2. search for fields in <td></td>
    pattern = re.compile(
            r'.*?<td.*?>(?P<date>.+?)</td>\s*?<td.*?>(?P<number>.+?)</td>\s*?<td.*?>(?P<balls>.+?)</td>\s*?<td.*?>(?P<prize2>.+?)</td>\s*?<td.*?>(?P<prize1>.+?)</td>.*',
            re.I | re.M | re.S)
    m = pattern.search(sub_text)

    if not m:
        print 'No match!'
        return

    date = m.group('date')
    number = m.group('number')
    balls = m.group('balls')
    prize1 = m.group('prize1')
    prize2 = m.group('prize2')
    # print date, number, balls, prize1, prize2

    # 3. search for data in <em></em>
    pattern = re.compile(
            r'<em.*?>(?P<ball1>.+?)</em><em.*?>(?P<ball2>.+?)</em><em.*?>(?P<ball3>.+?)</em><em.*?>(?P<ball4>.+?)</em><em.*?>(?P<ball5>.+?)</em><em.*?>(?P<ball6>.+?)</em><em>(?P<ball7>.+?)</em>',
            re.I | re.M | re.S)
    # print pattern.groupindex
    m2 = pattern.search(balls)
    if not m2:
        print 'No match!'
        return

    # print pattern.groups()
    red = m2.group('ball1') + ',' + m2.group('ball2') + ',' + m2.group('ball3') + ',' + m2.group(
            'ball4') + ',' + m2.group('ball5') + ',' + m2.group('ball6')
    blue = m2.group('ball7')

    pattern = re.compile(r'<strong>(?P<prize>.+?)</strong>.*', re.I | re.M | re.S)
    m2 = pattern.search(prize1)
    if not m2:
        print 'No match!'
        return
    prize1 = m2.group('prize')

    m2 = pattern.search(prize2)
    if not m2:
        print 'No match!'
        return
    prize2 = m2.group('prize').replace(',', '')

    result = {'date': date, 'number': number, 'red': red, 'blue': blue, 'prize1': prize1, 'prize2': prize2}
    return result


def save_to_db(rec):
    # print rec
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "mysql", "lottery")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 更新语句
    sql = '''
        INSERT INTO t_two_color (id, open_date, red, blue, prize1, prize2)
        SELECT {0}, '{1}', '{2}', '{3}', {4}, {5}
        FROM DUAL
        WHERE NOT EXISTS(
        SELECT 1
        FROM t_two_color
        WHERE id = {0});
    '''.format(rec['number'], rec['date'], rec['red'], rec['blue'], rec['prize1'], rec['prize2'])
    # print 'sql: '
    # print sql

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        traceback.print_exc()
        # 发生错误时回滚
        db.rollback()
    # 关闭数据库连接
    db.close()


# \u4e0b\u4e00\u9875
def get_next_page_num(text):
    # m = pattern.findall(text.decode('utf-8'))
    # m = pattern.search(text.decode('utf-8'))
    # m = re.findall(u'<a.*?>[\u4e00-\u9fa5]{2,3}</a>',
    m = re.findall(u'<a href="/zhcw/inc/ssq/ssq_wqhg.jsp\?pageNum=\d+">\u4e0b\u4e00\u9875</a>',
                   text.decode('utf-8'),
                   re.I)
    if not m:
        print 'Func get_next_page_num: Link No match!'
        return

    if len(m) != 1:
        print 'Get next page number error!'
        return -1

    link = m[0]
    # print link

    # pattern = re.compile(
    #         u'.*pageNum=?P<pnum>\d+?".*',
    #         re.I | re.M | re.S)
    m = re.search(r'.*pageNum=(?P<pnum>\d+).*', link, re.I)
    if not m:
        print 'Func get_next_page_num: Link No Match '
        return

    #print m.group('pnum')
    return m.group('pnum')


# # temp = source.decode('utf8')
# source = "s2f程序员杂志一2d3程序员杂志二2d3程序员杂志三2d3程序员杂志四2d3"
# pattern = re.compile(u"[\u4e00-\u9fa5]+")
# #pattern = re.compile(xx)
# results = pattern.findall(source.decode('utf8'))
# for result in results :
#     print result


# html = get_html(web_address + url + str(page_num))
# get_next_page_num(html)

# main start
while True:
    print 'Process page [' + str(page_num) + ']: '
    html = get_html(web_address + url + str(page_num))
    records = re.findall(r'<tr>.*?<em.*?</tr>', html, re.I | re.M | re.S)

    for record in records:
        recDict = get_record_fields(record)
        save_to_db(recDict)
        print 'Save record to db: ' + str(recDict)

    next_page = get_next_page_num(html)
    if page_num == next_page:
        break
    else:
        page_num = next_page

print '========== FINISH PROCESS HTML =========='
