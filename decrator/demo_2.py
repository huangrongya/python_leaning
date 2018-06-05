# -*- coding:utf-8 -*-
# __author : huangrongya
# @Desc : ================================================
# Life is short I use Python!!!                        ===
# If this runs wrong,don't ask me,I don't know why...  ===
# If this runs right,thank god,and I don't know why... ===
# Maybe the answer,my friend,is blowing in the wind... ===
# ========================================================
# date : 2018/6/5 0005 15:45
# @Project : demo
# @FileName: demo_2.py

import time


def logger(flag=True):
    def show_time(func):
        def inner(a):
            start = time.time()
            func(a)
            end = time.time()
            print("spend %s" % (end - start))
            if flag:
                print("日志记录")
        return inner
    return show_time


@logger(False)
def add(a):
    total = 0
    for j in a:
        total += j
    print(total)


i = 1000
li = []
while i > 0:
    li.append(i)
    i -= 1

add(li)
