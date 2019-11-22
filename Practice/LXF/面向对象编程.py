#
'''面向对象的程序开发'''

'''类'''
class Student:
    '''属性'''
    def __init__(self,name,score,gender):
        self.name=name
        self.__score=score


    '''方法'''
    def print_score(self):
        print('{}分数是{}'.format(self.name,self.__score))

    def score_garde(self):
        if int(self.__score) >=80:
            return 'A'
        elif int(self.__score)>=60:
            return 'B'
        else:
            return 'C'

    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0< score <100:
            self.__score=score
        else:
            raise ValueError
        return self.__score


'''继承和多态'''
class Animal:
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

'''继承的意义?  子类可以直接拿到父类的功能,只需增加自己特色的方法,或将父类不合理的方法覆盖重写;继承可以是继承树'''
Dog().run()
a=Dog()
b=Animal()
print(isinstance(a,Animal))
print(isinstance(a,Dog))
print(isinstance(b,Animal))
print(isinstance(b,Dog))

'''多态的意义?  
著名的开闭原则:对扩展开放：允许新增Animal子类；
               对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。'''
def run_twice(Animal):
    Animal.run()
    Animal.run()

run_twice(b)
run_twice(a)




'''实例化'''
s=Student('zaozao','90','female')
'''类'''
print(Student)
'''实例化的对象'''
print(s)
'''调用与实例绑定的函数  操作对象数据'''
s.print_score()
s.score_garde()
'''对象暴露的属性'''
print(s.name)
'''对象私有属性   在外部无法直接访问'''
# print(s.__score)
'''如何获取实例对象的私有属性?修改私有属性?
私有属性的意义?不能在外部直接修改属性值,需要在class中定义可修改或返回私有属性的函数'''
print(s.get_score())
print(s.set_score(1))
print(s.get_score())#此处私有属性值变了

'''获取对象信息'''
#方法1:使用type
print(a)
print(type(a))
print(type(a.run))
#方法2:使用instance
#方法3:使用dir
print(dir(list))
'''hasattr  getattr  setattr'''
class MyObject:
    def __init__(self):
        self.x= 9
    def __cheng__(self):
        return self.x * self.x

o=MyObject()
print(hasattr(o,'x'))
print(hasattr(o,'y'))
# print(getattr(o,'y'))
print(getattr(o,'y',None))
setattr(o,'y',99)
print(getattr(o,'y'))
#示例:
class ClassObj:
    classHost='http://www.baidu.com'
    def __init__(self,host,db,**kwargs):
        self.host=host
        self.db=db
        self.update_attr(**kwargs)

    def update_attr(self,**kwargs):
        if kwargs:
            for attribute_name in kwargs.keys():
                setattr(self,attribute_name,kwargs.get(attribute_name))


my = ClassObj('http://www.zaozao.com','db1',key='value')
print(my.host)
print(my.db)
print(my.key)

class UserInfo(ClassObj):
    def __init__(self,name,sex,**kwargs):
        self.__name=name
        self.sex=sex
        super(UserInfo,self).__init__(**kwargs)

    def set_name(self,name):
        if  isinstance(name,str):
            self.__name = name
            return self.__name
        else:
            print('name必须是字符串类型!')

user=UserInfo('zaozao','female',host='http://www.zaozao.com',db='db1',city='ShangHai')
# print(user.__name)
print(user.set_name('zaozao'))
print(user.sex)

