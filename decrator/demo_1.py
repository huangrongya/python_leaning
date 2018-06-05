# -*- coding:utf-8 -*-
# __author : huangrongya
# @Desc : ================================================
# Life is short I use Python!!!                        ===
# If this runs wrong,don't ask me,I don't know why...  ===
# If this runs right,thank god,and I don't know why... ===
# Maybe the answer,my friend,is blowing in the wind... ===
# ========================================================
# date : 2018/6/5 0005 11:22
# @Project : demo
# @FileName: demo_1.py

import time


def show_time(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print("run function takes %s s" % (end - start))

    return inner


@show_time
def foo():
    print("run foo...")
    time.sleep(2)


foo()
