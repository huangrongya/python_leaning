# -*- coding:utf-8 -*-
# __author : "huangrongya"
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# date : 2018/5/25 0025 16:57
# @Project : demo
# @FileName: demo_cart.py

_goods = [['iphone 6s', 5800], ['mac book', 9000], ['coffee', 32], ['python book', 80], ['bicycle', 1500]]

cart = []
flag = True
count = 0
while flag:
    salary = input("please input your salary: ")
    if salary.isdigit():
        salary = int(salary)
        while True:
            for i, good in enumerate(_goods, 1):
                print('%s.%s   %s' % (i, good[0], good[1]))
            index = input('enter index to buy [\'quit\' to exit]\n')
            if index.isdigit() and len(_goods) >= int(index) > 0:
                price = _goods[int(index) - 1][1]
                if price <= salary:
                    salary -= price
                    count += 1
                    cart.append(int(index) - 1)
                    print('the %s has put to your cart, you have %d left' % (_goods[int(index) - 1][1], salary))
                else:
                    print('your money is not enough, please choose again or exit, your money: %d' % salary)
            elif index == 'quit':
                flag = False
                print('you have bought: ')
                for i in range(len(cart)):
                    print('%s   %s' % (_goods[cart[i]][0], _goods[cart[i]][1]))
                print('you have %d left' % salary)
                print('welcome next time')
                break
            else:
                print('please choose a number or \'quit\'')
        break
    else:
        print("invalid input")
