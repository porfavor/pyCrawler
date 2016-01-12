#!/usr/bin/python
# coding=utf-8
import traceback
import random
import MySQLdb


def get_stats(db_table):
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "mysql", "lottery")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 更新语句
    sql = '''
            SELECT number,times, not_appear FROM {0} ORDER BY number asc;
        '''.format(db_table)
    # print 'sql: '
    # print sql

    # 执行SQL语句
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows


def update_mean_diff(rows, db_table):
    num = len(rows)
    sum_times = 0
    sum_np = 0
    for record in rows:
        sum_times += record[1]
        sum_np += record[2]

    mean_times = sum_times/num
    print 'mean_times: ' + str(mean_times)
    mean_np = sum_np/num
    print 'mean_np: ' + str(mean_np)

    # print rec
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "mysql", "lottery")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    for record in rows:
        # SQL 更新语句
        sql = '''
            UPDATE {0}
            SET diff_times = {2}, diff_not_appear = {3}, score = {4}
            WHERE number = {1};
        '''.format(db_table, record[0], mean_times-record[1], record[2]-mean_np, mean_times-record[1] + record[2]-mean_np)
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
            exit()

    # 关闭数据库连接
    db.close()


def get_top_scored_red():
    res = []

    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "mysql", "lottery")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 更新语句
    sql = '''
            SELECT number,score FROM {0} ORDER BY not_appear DESC limit {1};
        '''.format('t_appear_red', 17)
    # print 'sql: '
    # print sql

    # 执行SQL语句
    cursor.execute(sql)

    rows = cursor.fetchall()
    for row in rows:
        if row[1] > rows[0][1]/3:
            # print row
            res.append(row[0])

    #print rows
    return res


def get_top_scored_blue():
    res = []

    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "mysql", "lottery")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 更新语句
    sql = '''
            SELECT number,score FROM {0} ORDER BY not_appear DESC limit {1};
        '''.format('t_appear_blue', 3)
    # print 'sql: '
    # print sql

    # 执行SQL语句
    cursor.execute(sql)

    rows = cursor.fetchall()
    for row in rows:
        # print row
        res.append(row[0])

    #print rows
    return res


# MAIN
# generate red
red_stats = get_stats('t_appear_red')
update_mean_diff(red_stats, 't_appear_red')
blue_stats = get_stats('t_appear_blue')
update_mean_diff(blue_stats, 't_appear_blue')

top_scored_red = get_top_scored_red()
print top_scored_red
top_scored_blue = get_top_scored_blue()
print top_scored_blue

lottery_count = 5
while lottery_count > 0:
    red_final = random.sample(top_scored_red, 6)

    blue_final = random.sample(top_scored_blue, 1)

    print str(sorted(red_final)) + ' : ' + str(blue_final)
    red_final = []
    blue_final = []

    lottery_count -= 1

