# -*- coding:utf-8 -*-
# __author : "huangrongya"
# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================
# date : 2018/5/25 0025 12:42
# @Project : demo
# @FileName: login.py

"""
_user = "alex"
_pwd = "123"

for i in range(3):
    username = input("Username: ")
    pwd = input("Password: ")
    if username == _user and pwd == _pwd:
        print("Welcome %s" % username)
        break
    else:
        print("login fail!")
"""

for i in range(1, 100, 2):
    if i <= 50 or i >= 70:
        print(i, end=" ")
