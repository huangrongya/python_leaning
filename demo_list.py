# -*- coding:utf-8 -*-
# __author : "huangrongya"
# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================
# date : 2018/5/25 0025 13:52
# @Project : demo
# @FileName: demo_list.py

name1 = "Luffy"
name2 = "Zoro"
name3 = "Nami"
name4 = "Sanji"

a = [name1, name2, name3, name4]
print(a[0:])

a.append("Chopper")
print(a[0:])

a.insert(3, "Usoop")
print(a[0:])

a[3] = "Robin"
print(a)

# a.remove(a[0])
b = a.pop(3)
# del a[3]
a.remove(a[1])
print(a)
# print(b)

print(a[1: -1])
print(a[0:-1:1])
print(a[0::2])
print(a[-1::-1])

c = ["to", "be", "or", "not", "to", "be"]
print(c.count('to'))

a.extend(c)
print(a)

print(a.index('Nami'))
print(a.index('to'))

a.reverse()
a.sort()
print(a)

print(a.count("Zoro"))
print('Zoro' in a)

print(type(a) is list)
