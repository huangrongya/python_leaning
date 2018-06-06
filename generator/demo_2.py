# -*- coding:utf-8 -*-
# __author : huangrongya
# @Desc : ================================================
# Life is short I use Python!!!                        ===
# If this runs wrong,don't ask me,I don't know why...  ===
# If this runs right,thank god,and I don't know why... ===
# Maybe the answer,my friend,is blowing in the wind... ===
# ========================================================
# date : 2018/6/6 0006 15:02
# @Project : python_leaning
# @FileName: demo_2.py

def fib(m):
    n, before, after = 0, 0, 1
    while n <= m:
        yield before
        n += 1
        before, after = after, before + after


ret = fib(20)
for i in ret:
    print(i, end=' ')
print()


def f():
    print('1111')
    count = yield 2
    print(count)
    yield 3


g = f()
g.send(None)
g.send('44444')
