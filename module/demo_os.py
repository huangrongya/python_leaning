# -*- coding:utf-8 -*-
# __author : huangrongya
# @Desc : ================================================
# Life is short I use Python!!!                        ===
# If this runs wrong,don't ask me,I don't know why...  ===
# If this runs right,thank god,and I don't know why... ===
# Maybe the answer,my friend,is blowing in the wind... ===
# ========================================================
# date : 2018/6/6 0006 17:32
# @Project : python_leaning
# @FileName: demo_os.py

import os

print(os.getcwd())
d = os.getcwd()
# os.makedirs('abc/def')
# os.removedirs('abc/def')
print(os.listdir(d))
