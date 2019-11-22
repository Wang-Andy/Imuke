#coding:utf-8

'''访问数据库'''


'''SQLite  特点：轻量级，可嵌入，但不可承受高并发访问，适用与桌面和app'''

'''
import sqlite3

con=sqlite3.connect('test_user.db')
cursor=con.cursor()
# cursor.execute('create table test_user (id varchar(20) primary key, name varchar(20) )')
# cursor.execute('insert into test_user(id,name) values (\'1\',\'wangjing\')')
# cursor.execute('insert into test_user(id,name) values (\'2\',\'panda\')')
# cursor.execute('insert into test_user(id,name) values (\'3\',\'zaozao\')')
# cursor.execute(r"insert into test_user(id,name) values ('4','xiaoxia')")
# cursor.execute('delete from test_user')
print(cursor.rowcount) #没有数据查到是为-1，但多条数据插入为何是1？？？
# print(cursor.fetchall()) #此处fechall()、fetchtmany()、fetchone()皆获取不到数据
cursor.close()
con.commit()
con.close()

con=sqlite3.connect('test_user.db')
cursor=con.cursor()
cursor.execute('select * from test_user  ')
print(cursor.rowcount) #取出的数据数量为什么一直是-1？
# print(cursor.fetchone())
# print(cursor.fetchmany(3))
print(cursor.fetchall()) #fechall()、fetchtmany()、fetchone()同时执行，取出的数据会异常
print(cursor.rowcount)
cursor.close()
# con.commit() 这行多余
con.close()
'''

''' 没解出来的小习题
import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    con=sqlite3.connect(db_file)
    cur=con.cursor()
    cur.execute('select * from user')
    stu_tuples=cur.fetchall()
    print(stu_tuples)
    cur.close()
    con.close()
    l = []
    L=[]
    for i,k,v in stu_tuples:
        print(i,k,v)
        if v >= low and v <= high :
            l.append(v)
    print(l)
    print(sorted(l))
    '''实现了分数顺序排列，如何打印相应name?'''




print(get_score_in(60, 100) )

# 测试:
# assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
# assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
# assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
#
# print('Pass')
'''

'''
import  mysql.connector

con=mysql.connector.connect(user='root',password='password',db='test')
cursor=con.cursor()
cursor.execute('create table user (id varchar(20) primary key ,name varchar(20)')
cursor.execute('insert into user(id,name) values (%s,%s)',['1','wangjing'])
print(cursor.rowcount)
con.commit()
cursor.close()



cursor=con.cursor()
cursor.execute('select * from user')
print(cursor.rowcount)
print(cursor.fetchall())
cursor.close()
con.close()
'''


