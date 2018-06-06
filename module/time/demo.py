# -*- coding:utf-8 -*-
# __author : huangrongya
# @Desc : ================================================
# Life is short I use Python!!!                        ===
# If this runs wrong,don't ask me,I don't know why...  ===
# If this runs right,thank god,and I don't know why... ===
# Maybe the answer,my friend,is blowing in the wind... ===
# ========================================================
# date : 2018/6/6 0006 16:49
# @Project : python_leaning
# @FileName: demo.py

import time

print(time.time())
# time.sleep(1)
print(time.clock())
print(time.gmtime())
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print(time.timezone)
