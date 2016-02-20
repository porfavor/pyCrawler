#!/usr/bin/python
# coding=utf-8

import random

class Utils:
    def __init__(self):
        print 'Init class'

    def pick_up(self, total_list, num):
        i = 0;

        # pick_list = []
        #
        # while num > 0:
        #     element = total_list[i]
        #
        #     i -= 1
        #     if i == num:
        #         break

        return random.sample(total_list, num)


util = Utils()

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice = util.pick_up(list, 5) #从list中随机获取5个元素，作为一个片断返回
print slice
print list #原有序列并没有改变。
