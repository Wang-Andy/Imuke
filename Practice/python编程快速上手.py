#coding=utf-8

'''3.11 实践项目'''
# def collatz(number):
#     if number % 2 !=0:
#         data = number * 3 + 1
#         print(data)
#     else:
#         data = number // 2
#         print(data)
#
#     if data != 1:
#         return collatz(data)
#
# try:
#     A = int(input('Enter number:'))
#     a=collatz(A)
# except ValueError:
#     print('Please enter number!')

'''体会 列表是可变对象，字符串是不可变对象    思考列表与字符串的共同点？不同点？ '''
# spam=[1,8,2,3,9,6,7,5]
# spam.sort() #
# print(spam)

# list=['zaozao','ZAO','panda','PAN','WANG','wangjing','xiaoxia','XIA']
# print(list.sort()) #使用Ascii顺序
# print(list)
# list.sort(reverse=True)
# print(list)
# list.sort(key=str.lower)
# print(list)
# list.sort(key=str.upper)
# print(list)

#list_a=[1,2,3]
# list_b=['a','b','c']
# list_b.extend(list_a)
# print(list_b)

# a='abc'
# b=a.replace('a','A')
# print(a)
# print(b)

'''将可变数据类型赋给变量，，如列表、字典，变量实质上是对他们的引用
   将不可变数据类型赋给变量，如字符串、数字、元组，变量是保存值本身'''

'''什么是方法？ 
   属于list的方法？ list.index(),list.append(),list.insert(i,name),list.remove(),list.pop()
   list与元组类型互换？ list(),tuple()
   '''

'''4.10 实践项目'''
# spam=['apples','banana','tofu','cats']
# def pars(*arg):
#     str=''
'''这个思路很棒！  通过列表下标与列表长度的比较，实现列表遍历与其它操作'''
# for k,v in enumerate(spam):
#     print (str(k)+' '+v)

#     for n in arg:
#         print(arg.index(n))
#         print(len(arg)-1)
#         if arg.index(n) < (len(arg)-1):
#             str= str + n + ','
#         elif arg.index(n) == (len(arg)-1):
#             str = str + 'and' + ',' + n
#         else:
#             break
#         print(str)
#     return str
#
# A=pars(*spam)
# print(A,type(A))  #此处有返回值则打印返回值相应str类型，无返回值则打印None

# grid=[['.','.','.','.'],
#       ['.','0','0','.'],
#       ['0','.','.','0']]
# print(len(grid))
# print(len(grid[0]))
# i=0
# while i < (len(grid)):
#     h=0
#     while h < len(grid[i]):
#         print(grid[i][h],end='')
#         h += 1
#     print('/n')
#     i += 1


'''字典 键-值对的顺序不重要 
    如何获取字典key? dict.keys()
    如何获取字典value值？ dict.values(),dict[name],dict.get(name),dict.get(name,name_value)
    同时获取key、value？ dict.items(),dict.setdefault()
    '''
#字典的2种表达方式
# spam={'name':'wangjing','age':27}
# spam=dict(name='wangjing',age=27)

# print(spam['name'])
# # print(spam['color'])
# print(spam.get('name'))
''' 区分get与update: 函数返回后   新增的值销毁  '''
# print(spam.get('color','red'))
# print(spam)
# bool_result=bool('color' in spam)
# print(bool_result)

'''如何修改字典value值？  如何为字典生成新的key和value？ 如何为字典赋默认值或生成新字典？'''
# spam['color']='red'
# print(spam)

# spam.update(color='red')
# print(spam)

# spam.setdefault('garde','A') #字典是可变类型
# print(spam)

# spam.setdefault('garde',{}) #生成内嵌的字典
# print(spam)

'''漂亮打印'''
# import pprint
# pprint.pprint(spam) #排序后打印

''' 5.6 实践项目 '''
# dict={'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
#
# def displayInventory(inventory):
#     item_total=0
#     for k,v  in inventory.items():
#         print(str(v) + ' ' + k )
#         item_total=item_total+v
#     print('total number of items:' , item_total)
#
# displayInventory(dict)
#
# def addTolnventory(inventory,additerms):
#     count={}
#     for goods in additerms:
#         if goods in inventory.keys():
'''       这种思路非常优秀   将list转化为字典 '''
#             count.setdefault(goods,0)
#             count[goods]=count[goods]+1
#             inventory[goods]=inventory[goods]+1
#     # print(count)
#     # print(inventory)
#     # for k,v in inventory.items():
#     #     print(str(v)+' '+k)
#     return inventory
#

# inv={'gold coin':42,'rope':1}
# loot=['gold coin','gold coin','rope','gold coin','rope','haha']
# add = addTolnventory(inv,loot)
# print(add)
# displayInventory(add)

'''IO 访问路径和文件 读写文件'''

'''抛出异常后记录异常的反向跟踪信息，并利用except优雅的处理该异常'''
# import traceback
# try:
#     raise Exception('This is a error message!')
# # except Exception as e :
# #     print(e)
# except:
#     errorfile=open('errorwarning.txt','w')
#     errorfile.write(traceback.format_exc())
#     errorfile.close()
#     print('the traceback warning is written into errorwarning.txt!')
#
# errorfile=open('errorwarning.txt','r')
# print(errorfile.read())
# errorfile.close()

'''断言 是针对开发的，而不是针对最终的产品'''

'''日志代替print  方便禁用  带时间戳，可计入文件'''
'''思考： 异常、日志、断言、IDLE的调试器各自适用的场景'''
# import logging
'''logging用法'''
# logging.basicConfig(filename='loggingData.txt',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
# logging.disable(level=logging.DEBUG)
#
# import traceback
#
# logging.debug('Start a program!')
# def circus(n):
#     logging.debug('函数开始，传入n值：%s' %n)
#     total=1
#     for i in range(1,n+1):
#         total=total*i
#         logging.debug('i的值：'+str(i)+',total的值'+str(total))
#     logging.debug('函数结束，n值：%s' %n)
#     return total
#
# try:
#     print(circus(c))
'''logging用法'''
# # except Exception as e:
# #     print('traceback报错信息：%s' %e)
# except Exception as e:
#     logging.exception(e)
# except:
'''记录反向追踪信息'''
#     file=open('Exception.txt','a')
#     file.write(traceback.format_exc())
#     file.close()
#     print('Excption信息写入了Exception.txt!')
#
# logging.debug('End the program!')
#
# with open('loggingData.txt','r') as f:
#     print(f.read())
#
# with open('Exception.txt') as g:
#     print(g.read())

# coding=utf-8

'''12.3  EXCEL 读取数据，填充数据，写入文件'''
# import openpyxl
# import pprint
#
# path='C://Users/18521/Desktop/'
# wb=openpyxl.load_workbook(path+'宝宝规划书.xlsx')
# sheet=wb['test']
#
# CountyData={}
# for i in range(2,10):
#     State=sheet['B'+str(i)].value
#     County=sheet['C'+str(i)].value
#     Pop=sheet['D'+str(i)].value
'''很棒的思路  如何生成嵌套的字典？并实现字典value的累加？'''
#     CountyData.setdefault(State,{})
#     CountyData[State].setdefault(County,{'Tracts':0,'pop':0})
#     CountyData[State][County]['Tracts'] +=1
#     CountyData[State][County]['pop'] += int(Pop)
# # print(CountyData)
#
''' 与众不同的思路：
     将返回的数据作存入.py文件，
     接下来作为模块供调用 '''
#
# print('writing result .....')
# with open('cencus.py','w') as f:
#     f.write('Data='+pprint.pformat(CountyData))
# print('Done!')
#
# # with open('cencus.py') as f:
# #     print(f.read())
#
# import os
# print(os.path.abspath('..'))
# import sys
# sys.path.append('C:/Users/18521/PycharmProjects/imuke/')
# from Study import cencus
#
# # print(data)
# print(cencus.Data)
# print(cencus.Data['ShangHai']['xuhui']['Tracts'])
# print(cencus.Data['ShangHai']['xuhui']['pop'])

''' 12.4 遍历excel数据  修改数据'''

# coding=utf-8

# import openpyxl
# import os
# print(os.path.abspath('wangjing.xlsx'))
# from openpyxl.styles import Font,colors
# ft=Font(name="楷体",size=20,bold=True,italic=True,u='single',color=colors.RED)
#
# wb=openpyxl.load_workbook('C:/Users/18521/PycharmProjects/imuke/Study/wangjing.xlsx')
# # wb.create_sheet(title='test',index=0)
# # wb.remove(wb['wangjing'])
# print(wb.sheetnames)
# sheet=wb.active
# print(sheet)
# wb.save('C:/Users/18521/PycharmProjects/imuke/Study/wangjing.xlsx')
# tricts={'huangpu':99,'wuxi':999}

'''很棒的思路  通过判断是否存在dict的key中变更值  而不是通过if...else..判断'''
# #方法一：常用
# for i in range(2,sheet.max_row+1):
#     for k,v in tricts.items():
#         # print(sheet['B'+str(i)].value)
#         # print(tricts.values())
#         if sheet['C' + str(i)].value == k:
#             sheet['D'+str(i)].value =v
# wb.save('C:/Users/18521/Desktop/宝宝规划书.xlsx')
#
# #方法二：同样精彩
# total=0
# for i in range(2,sheet.max_row+1):
#     name=sheet.cell(row=i,column=3).value
#     for tricts_name in tricts:
#         if name ==tricts_name:
#             sheet.cell(row=i,column=4).value=tricts[tricts_name]
'''如何修改单元格样式？'''
#             sheet.cell(row=i,column=4).font=ft
#             total =sheet.cell(row=i,column=4).value + total
# # sheet.cell(row=sheet.max_row+1,column=4).value = total
# # sheet.cell(row=sheet.max_row+1,column=4).value = '=sum(D4:D9)'
# wb.save('C:/Users/18521/PycharmProjects/imuke/Study/wangjing.xlsx')

''' 第14章 读取CSV数据  分别以list和dict写入header和内容  分析输出'''
# import csv
# header=['haha','heihei','xixi']
# data=[['zaozao','wanwan','dengdeng'],['zaoa','wana','denga']]
# with open('C:/Users/18521/PycharmProjects/imuke/Practice/wangjing.csv','w',newline='',encoding='utf-8') as f:
#     wr=csv.writer(f,delimiter='\t')
#     wr.writerow(header)
#     wr.writerows(data)
# with open('C:/Users/18521/PycharmProjects/imuke/Practice/wangjing.csv','r',encoding='utf-8') as f:
#     re=csv.reader(f,lineterminator='\n\n')
#     header=next(re)
#     print(header)
#     for name in re:
#         print(name)
# #
# header=['name','password','age']
# data=[{'name':'wangjing','password':1,'age':27},
#       {'name':'panda','password':2,'age':33},
#       {'name':'zaozao','password':3,'age':1}]
# data_gradma={'name':'xiaoxia','password':4,'age':18}
# with open('C:/Users/18521/PycharmProjects/imuke/Practice/wang.csv','w',encoding='utf-8',newline='') as f:
#     WR=csv.DictWriter(f,header,delimiter=',')
#     WR.writeheader()
#     WR.writerows(data)
#     WR.writerow(data_gradma)
# with open('C:/Users/18521/PycharmProjects/imuke/Practice/wang.csv','r',encoding='utf-8') as f:
#     RE=csv.reader(f)
#     header=next(RE)
#     print(header)
#     for dict in RE:
#         print(str(RE.line_num)+' '+ str(dict))

