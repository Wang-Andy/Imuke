#coding=utf-8

# #函数参数顺序：位置参数，默认参数，可变参数，命名关键字参数和关键字参数，5种参数可组合使用
#
# '''可变参数  可传入list或tuple，组装为tuple'''
# def calc(*number):
#     sum=0
#     for n in number:
#         sum=sum+n*n
#     return sum
#
# number1=[1,2,3,4,5]
# print(calc(*number1))
#
# number2=(1,3,5)
# print(calc(*number2))
#
# '''关键字参数 接收dict'''
# def person(name,age,**kwargs):
#     print(name,age,kwargs)
#
# person('wangjing',18,city='shanghai',sex='female')
# dict=dict(city='shanghai',sex='female',interest='reading')
# person('wangjing',18,**dict)
#
# '''命名关键字参数 接收dict'''
# def person(name,age,*,city,job):
#     print(name,age,city,job)
#
# person('wangjing',18,city='ShangHai',job='developer enginner')
#
# def person(name,age,*,city='Shanghai',job):
#     return name,age,city,job
#
# print(person('wnagjing',18,job='enginner'))
#
# def person(name,age,*args,city='Sanghai',job):
#     return  (name,age,args,city,job)
#
# print(person('wangjing','18',*number1,job='enginner'))









