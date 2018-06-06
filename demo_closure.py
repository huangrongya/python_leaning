# -*- coding:utf-8 -*-
# __author : huangrongya
# @Desc : ================================================
# Life is short I use Python!!!                        ===
# If this runs wrong,don't ask me,I don't know why...  ===
# If this runs right,thank god,and I don't know why... ===
# Maybe the answer,my friend,is blowing in the wind... ===
# ========================================================
# date : 2018/6/6 0006 9:39
# @Project : python_leaning
# @FileName: demo_closure.py

def count():
    fs = []
    for i in range(1, 4):
        def func():
            return i * i

        fs.append(func)
    return fs


f1, f2, f3 = count()

print(f1(), f2(), f3())


def count2():
    fs = []

    def func(i):
        def f():
            return i * i

        return f

    for j in range(1, 4):
        fs.append(func(j))
    return fs


f4, f5, f6 = count2()

print(f4(), f5(), f6())

flag = 1


def printer(flag):
    def inner():
        nonlocal flag
        flag = 0
        print(flag)

    return inner


inner = printer(flag)
inner()
print(flag)


def func2(flag1):
    print(flag1)
    flag1 = 0
    print(flag1)


func2(flag)
print(flag)
