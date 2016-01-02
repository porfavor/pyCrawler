#!/usr/bin/python
# coding=utf-8
import traceback
import random
import MySQLdb


def get_least_appeared_red():
    res = []

    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "mysql", "lottery")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 更新语句
    sql = '''
            SELECT number,times FROM t_appear_red ORDER BY times ASC limit 7;
        '''
    # print 'sql: '
    # print sql

    # 执行SQL语句
    cursor.execute(sql)

    rows = cursor.fetchall()
    for row in rows:
        # print row
        res.append(row[0])

    #print res
    return res


def get_long_not_appeared_red():
    res = []

    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "mysql", "lottery")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 更新语句
    sql = '''
            SELECT number,times FROM t_appear_red ORDER BY not_appear DESC limit 7;
        '''
    # print 'sql: '
    # print sql

    # 执行SQL语句
    cursor.execute(sql)

    rows = cursor.fetchall()
    for row in rows:
        # print row
        res.append(row[0])

    #print res
    return res


def get_least_appeared_blue():
    res = []

    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "mysql", "lottery")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 更新语句
    sql = '''
            SELECT number,times FROM t_appear_blue ORDER BY times ASC limit 2;
        '''
    # print 'sql: '
    # print sql

    # 执行SQL语句
    cursor.execute(sql)

    rows = cursor.fetchall()
    for row in rows:
        # print row
        res.append(row[0])

    #print res
    return res


def get_long_not_appeared_blue():
    res = []

    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "mysql", "lottery")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 更新语句
    sql = '''
            SELECT number,times FROM t_appear_blue ORDER BY not_appear DESC limit 2;
        '''
    # print 'sql: '
    # print sql

    # 执行SQL语句
    cursor.execute(sql)

    rows = cursor.fetchall()
    for row in rows:
        # print row
        res.append(row[0])

    #print res
    return res


# MAIN
# generate red
red_all_num = 6
red_left_num = 0
red_final = []
red_final_left = []
red_final_sure = []
red_least_appear = get_least_appeared_red()
red_long_not_appear = get_long_not_appeared_red()

for element in red_least_appear:
    if element in red_long_not_appear:
        #print element
        red_final_sure.append(element)
        red_long_not_appear.remove(element)
        red_least_appear.remove(element)

red_final_left.extend(red_long_not_appear)
red_final_left.extend(red_least_appear)
#print red_final_left

red_left_num = red_all_num - len(red_final_sure)
#print red_left_num

#red_final.extend(random.sample(red_long_not_appear, red_left_num))

# generate blue
blue_final = []
blue_final_left = []
blue_final_sure = []
blue_least_appear = get_least_appeared_blue()
blue_long_not_appear = get_long_not_appeared_blue()

for element in blue_long_not_appear:
    if element in blue_least_appear:
        # print element
        blue_final_sure.append(element)
        blue_long_not_appear.remove(element)
        blue_least_appear.remove(element)

blue_final_left.extend(blue_long_not_appear)
blue_final_left.extend(blue_least_appear)
blue_final_left.extend(blue_final_sure)
#print blue_final_left

lottery_count = 5
while lottery_count > 0:
    red_final.extend(red_final_sure)
    red_final.extend(random.sample(red_final_left, red_left_num))

    blue_final = random.sample(blue_final_left, 1)

    print str(sorted(red_final)) + ' : ' + str(blue_final)
    red_final = []
    blue_final = []

    lottery_count -= 1



