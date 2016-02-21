#!/usr/bin/python
# coding=utf-8
import urllib
import re
import traceback
import MySQLdb

global web_address, url, page_num
web_address = 'http://quotes.money.163.com'
uri = '/fund/jzzs_{0}_{1}.html?start={2}&end={3}&sort=TDATE&order=desc'
page_num = 0


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
            r'.*?<td.*?>(?P<date>.+?)</td>\s*?<td.*?>(?P<fund_nuv>.+?)</td>\s*?<td.*?>(?P<fund_nav>.+?)</td>\s*?<td.*?><span class=\"\w*?\">(?P<growth_rate>.+?)%</span></td>.*',
            re.I | re.M | re.S)
    m = pattern.search(sub_text)

    if not m:
        print 'No match!'
        return

    date = m.group('date')
    fund_nuv = m.group('fund_nuv')
    fund_nav = m.group('fund_nav')
    growth_rate = m.group('growth_rate')

    result = {'date': date, 'fund_nuv': fund_nuv, 'fund_nav': fund_nav, 'growth_rate': growth_rate}
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
    url = (web_address + uri).format(162411, page_num, '2011-09-29', '2016-02-20')
    print 'url: ' + url
    html = get_html(url)
    # print html


    records = re.findall(r'<tr>.*?<span.*?</tr>', html, re.I | re.M | re.S)

    for record in records:
        #print record
        recDict = get_record_fields(record)
        # save_to_db(recDict)
        print 'Save record to db: ' + str(recDict)

    # next_page = get_next_page_num(html)
    # if page_num == next_page:
    #     break
    # else:
    #     page_num = next_page

    break

print '========== FINISH PROCESS HTML =========='
