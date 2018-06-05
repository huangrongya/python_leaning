# -*- coding:utf-8 -*-
# __author : huangrongya
# @Desc : ================================================
# Life is short I use Python!!!                        ===
# If this runs wrong,don't ask me,I don't know why...  ===
# If this runs right,thank god,and I don't know why... ===
# Maybe the answer,my friend,is blowing in the wind... ===
# ========================================================
# date : 2018/5/25 0025 19:45
# @Project : demo
# @FileName: demo_dictionary.py

dic1 = {'name': 'Alex', 'age': 17, 'hobby': 'girl'}
print(dic1['name'])
print(list(dic1.keys()))
print(list(dic1.values()))

dic1['age'] = 18
print(dic1['age'])

a = dic1.setdefault('age', 40)
print(a)
print(dic1)

dic2 = {'1': '111', 'age': '27'}
dic1.update(dic2)
print(dic1)