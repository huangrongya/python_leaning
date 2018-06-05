# -*- coding:utf-8 -*-
# __author : huangrongya
# @Desc : ================================================
# Life is short I use Python!!!                        ===
# If this runs wrong,don't ask me,I don't know why...  ===
# If this runs right,thank god,and I don't know why... ===
# Maybe the answer,my friend,is blowing in the wind... ===
# ========================================================
# date : 2018/6/5 0005 17:20
# @Project : python_leaning
# @FileName: login.py


def check_login(status):
    def login(func):
        def inner():
            if status is True:
                print("you have already login")
            else:
                data = open("user_info", "r", encoding='utf8')
                dic = {}
                for i in data:
                    print(i.strip())
                    line = i.strip()
                    dic[line.split(":")[0].strip()] = line.split(":")[1].strip()
                choose = input("please choose your way to login: 1.password 2.wechat")
                if choose == 1:
                    username = input("please enter your username: ")
                    password = input("please enter your password: ")
                    if dic['username'] == username and dic['password'] == password:
                        print('welcome! %s' % username)
                        status = True
                    else:
                        print('login failed!')
                        return
                elif choose == 2:
                    token = input('please enter your token: ')
                    if dic['token'] == token:
                        status = True
                        print('login success!!!')
        return inner
    return login


