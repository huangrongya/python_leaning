# _*coding:utf-8*
# __author : "huangrongya"
# date : 2018/5/25 0025 10:47

name = "huangrongya"
age = "27"
country = "China"

msg = '''
----------INFO----------
name: %s
age: %s
country: %s
You will be retailed in %s years
-----------------------
''' % (name, age, country, 60-int(age))
print(msg)

print("my name is %s , and I am %d years old" %(name, int(age)))
