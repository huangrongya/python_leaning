# -*- coding:utf-8 -*-
# __author : huangrongya
# @Desc : ================================================
# Life is short I use Python!!!                        ===
# If this runs wrong,don't ask me,I don't know why...  ===
# If this runs right,thank god,and I don't know why... ===
# Maybe the answer,my friend,is blowing in the wind... ===
# ========================================================
# date : 2018/6/6 0006 17:11
# @Project : python_leaning
# @FileName: demo_random.py
import random


# print(random.random())
# print(random.randint(1, 10))
# print(random.choice((1, 3, [1, 2], 'hello')))

def v_code():
    code = ''
    for i in range(5):
        code += random.choice([chr(random.randrange(65, 91)), str(random.randrange(0, 10))])
    print(code)


v_code()
