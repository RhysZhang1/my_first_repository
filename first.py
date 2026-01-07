#-*- coding: utf-8 -*-
# print("111","222",sep='z',end='a')
# print("444")
#import builtins

# x = 1
# y = x
# z = -3.456
# print(x, y, z,sep='\n')

# a = 2
# print(a)
# a = "!"
# print(a)

# 价格 = 5
# print(价格)

# Azb_a = 30
# Azb_b = 40
# print(Azb_a, Azb_b,sep='\n')

# a = '123'
# print(type(a))

# a = 4+2j
# print(a)

# a = '''aaa
# bbb
# ccc
# ddd
# '''
# print(a)

# a = 1234
# b = 2345
# print("ABCD is %5d,and %2d" % (a,b))

# a = 12345
# print("ABCD is %.5f"%(a))

# a = 234
# b = 9583
# print("I`m %d%%d%d" % (a,b))

# print('AAA{:^6d}'.format(12))

# a = 123
# b = 456
# print(f"zzz{a},zzz{b}")

# a = 1
# b = 1.4
# c = 2.9
# d = b**c
# e = c//b
# f = c%b
# print(d,e,f)

# a = input()
# print(a)

# print("AAA\nBBB")
# print("AAA\tBBB")

# print("AAA\\\\tBBB")
# print("AAA\\\tBBB")
# print("AAA\\tBBB")
# print("AAA\tBBB")

# a = 12345
# print(r"AAA\tBBB\nCCC%d"%(a),r"AAA\nBBB")

# a = float(input())
# if a >= 60 :
#     print("Good")
#     print("Wll")
# else :
#     print("Bad")

# a = float(input())
# print("Good") if a >= 60 else print("Bad")

# a = float(input())
# if a >= 90:
#     print('A')
# elif 80 <= a < 90:
#     print('B')
# elif 70 <= a < 80:
#     print('C')
#     print('CC')
# else :
#     print('D')

# a = float(input())
# if a >= 0:
#     a = a - 9
#     if a >= 0:
#         a = a - 9
#         if a >= 0:
#             a = a - 9
#             if a >= 0:
#                 a = a - 9
#                 if a >= 0:
#                     a = a - 9
#                     if a >= 0:
#                         a = a - 9
#                         if a >= 0:
#                             a = a - 9
#                             if a >= 0:
#                                 a = a - 9
#                                 print(a)
#                             else:
#                                 print(a)
#                         else:
#                             print(a)
#                     else:
#                         print(a)
#                 else:
#                     print(a)
#             else:
#                 print(a)
#         else:
#             print(a)
#     else:
#         print(a)
# else:
#     print(a)

# i = 1
# a = 0
# while i<=100:
#     a = a + i
#     print(a)
#     i = i + 1


# while True:
#     print('好好学习天天向上')

# str = 'HELLOWORLD'
# for i in str:
#     print(i)

# str = '1234'
# for i in str:
#     print(i)

# for i in range(-5,10,2):
#     print(i)

# for i in range(1,10,2):
#     print("12345")

# a = 0
# for i in range(101):
#     a= a + i
# print(a)

# for i in range(10):
#     if i == 9:
#         break
#     print(i)

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# a = 'Hello'
# print(a,type(a))#Hello <class 'str'>
# a1 = a.encode()#编码
# print(a1,type(a1))#b'Hello' <class 'bytes'>
# a2 = a1.decode()#解码
# print(a2,type(a2))

# print("10"+"10")
# print(10+10)

# print("Hello World\n"*10)

# A = 'abcdopg'
# print('a' in A)
# print('e' in A)
# print('e' not in A)
# print('a' not in A)
# print('abd' not in A)
# B = '这是个'
# print('这' in B)

# name='abcdefg'
# print(name[6])
# print(name[-7])
# print(name[1:7:2])
# print(name[-10:5:2])#相当于[0:5:2]
# print(name[-3:5:2]) #相当于[4:5:2]
# print(name[1:7:-1])

# a='abcdefghabcdefgh123'
# print(a.find('def'))
# print(a.find('def',8))
# print(a.rfind('def'))
# print(a.index('def',8))
# print(a.count('def'))
# print(a.replace('df','xyz'))
# print(a.upper())
# print(a.title())
# print(a.swapcase())
# print(a.capitalize())
# print(a.islower())
# print(a.isalnum())
# b='ABCDEFGABCDEFG123'
# print(b.isupper())
# print(b.endswith('123'))
# print(b.strip('ABC'))
# print(b.split('A'))
# c=['A','B','C','D','E','F']
# print('-'.join(c))
# d='aaa'
# print(d.center(2,'b'))
# print(d.center(6))
# print('42'.zfill(5))

# a=[123,234,'a12',323]
# print(a[0:3])
# a.append(456)
# a.extend('asdf')
# a.insert(5,'asdf')
# a[2]=12345
# print(123 in a)
# del a[1]
# print(a)
# a.pop()
# a.remove('a12')
# del a[1:5:2]
# print(a)

# a=[123,234.2,323]
# a.sort()
# print(a)

# a=[]
# for i in range(10):
#     a.append(i)
# print(a)
# [a.append(i) for i in range(10)]
# [a.append(i) for i in range(1, 21) if i % 2 == 1]
# print(a)


# a=[1,2,3,4]
# b=[1,2,3,a]
# print(b[3])

# a=(1,2,3,'a12','3d')
# print(a)

# a={'d':1,'b':2,'c':3}
# print(a['b'])

# a={1,2,5.9,3.4,4.89}
# b={'a','b','c','d',1,2,3}
# print(a|b)

# a=2.9
# print(int(a))

# a=1
# b=a
# print(a,b)
# b=3
# print(a,b)

# a=[1,2,3]
# b=a
# print(a,b)
# b.append(4)
# print(a,b)

# import copy
# a=[1,2,3,[4,5,6]]
# b=copy.copy(a)
# print(a)
# print(b)
# b.append(7)
# print(a,b)
# b[3].append(8)
# print(a,b)

# copy.deepcopy(a)

# def abc():
#     print("abc")
# abc()

# def abc():
#     return 'abc'
# abc() #无结果
# print(abc())

# def zxc(a,b):
#     return a+b
# print(zxc(1.2223,2.5556))

# def sdf(a,b,c=3):
#     print(a,b,c)
# sdf(1,2)
# sdf(1,2,6)

# def abc(*args):
#     for arg in args:
#         print(arg)
# abc(1,2,3,4,5,6,7)

# def abc(**kwargs):
#     print(kwargs)
# abc(a='x',b='y',c='z')

# def 函数():
#     print(123)
# 函数()

# def 计算总和(数字列表):
#     总和 = 0
#     for 数字 in 数字列表:
#         总和 += 数字
#     return 总和
# def 问候(名字):
#     return f"你好，{名字}！"
# 数字列表 = [1, 2, 3, 4, 5]
# 结果 = 计算总和(数字列表)
# print(结果)
# print(问候("小明"))

# a=80
# def abc():
#     global a
#     a=100
#     print(a)
# abc()
# print(a)

# a=5
# def abc():
#     a=10
#     def xyx():
#         nonlocal a
#         a=20
#         print(a)
#     xyx()
#     print(a)
# abc()

# def add(a,b):
#     return a+b
# print(add(1,2))
#
# add = lambda a,b: a+b
# print(add(1,2))

# abc=lambda : 'abc'
# print(abc())

# asd=lambda a,b,c=12:a+b*c
# print(asd(2,3))
# print(asd(1,2,4))

# qwe=lambda **kwargs: kwargs
# print(qwe(q='1',w='2'))

# a=1;b=2
# asd=lambda a,b:'t' if a>b else 'f'
# print(asd(a,b))

# print(min(1,3,5,2.1,-1))
# print(sum([1,3.3,1,5]))

# a=2
# b=9
# c=2.34
# print(min(a,b,c,key=abs))

# asd=[1,2,3,4]
# zxc=['q','s','x','d']
# print(list(zip(asd,zxc)))

# qwe=[1,3,8,4,9]
# def asdfg(x):
#     return (x*2)+1
# asd=map(asdfg,qwe)
# print(list(asd))

# from functools import reduce
# asd=[1,2,3,4,5,6]
# def qwerr(a,b):
#     return a+b
# zxc=reduce(qwerr,asd)
# print(zxc)

# qwe=(1,2,3,4,5,6,7,8)
# a,b,c,d,e,f,g,h=qwe
# print(a,b,c,d,e,f,g,h)
# i,j,k,*op = qwe
# print(i,j,k,*op,type(op))

# def asd(a,b):
#     if a==1:
#         raise Exception('F')
#     else:
#         return a+b
# print(asd(2,2))

# import ceshi
# ceshi.asd()
# ceshi.qwe()

# from ceshi import qwe
# qwe()

# import time
# print(time.time())

# from fir import *
# qwe.rty()

# from fir import *
# qwe.rty()

# def add(n):
#     if n==1:
#         return n
#     return n+add(n-1)
# print(add(100))

# def fbnq(n):
#     if n<=0:
#         return 0
#     if n==1 or n==2:
#         return 1
#     return fbnq(n-1)+fbnq(n-2)
# for i in range(101):
#     print(fbnq(i))

# def add(m):
#     n=10
#     def zxc(p):
#         print(n*m*p)
#     return zxc
# add(33)(89)
#
# asd=add(33)
# asd(89)

# def abc(fn):
#     print(123)
#     print(456)
#     fn()
# def abcg():
#     print(789)
# abc(abcg)

# def csd():
#     print(123)
#
# def abc(fn):
#     def ghl():
#         #
#         fn()
#         #
#     return ghl
#
# ot=abc(csd)
# ot()

# def abc(fn):
#     def xyz(a):
#         print(a+45)
#         print("xyz")
#         fn()
#     return xyz
#
# @abc
# def asd():
#     print(1234)
#
# for x in range(10):
#     asd(x)

# def abs(fn):
#     def xyz(*a):
#         fn(*a)
#         for i in a:
#             print(i+1)
#     return xyz
# @abs
# def seed(*args):
#     print(args)
# seed(1,2,3,4)

# def qwe(fn):
#     def asd():
#         fn()
#         print(123)
#     return asd
# def qwe2(fn):
#     def asd2():
#         fn()
#         print(456)
#     return asd2
# @qwe2
# @qwe
# def seed():
#     print(123456)
#
# seed()

# a={'a':1,'b':2,'c':3}
# a='qwertyuio'
# for i in a:
#     print(i)

# import builtins
# print(dir(builtins))

# a=int(input())
# if a==1:
#     raise Exception('异常')
# else:
#     print(a)

# a=0.1
# b=0.2
# print(a+b)

# class person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show(self):
#         print(f'{self.name}的年龄是{self.age}')
# zyh=person('zyh',18)
# zyh.show()

# class Person:
#     name='zzz'
#     __age=18
# aaa=Person()

# class 类1:
#     obj=None
#     def __new__(cls,*args,**kargs):
#         print(1)
#         if cls.obj==None:
#             cls.obj=super().__new__(cls)
#         return cls.obj
# a=类1()
# print(a)
# a1=类1()
# print(a1)

# class aaa(object):
#     '''aaaaaaaaaaaaaaxaxaxaxx
#     axaxsxawxawxawdacawadwdawxdawx'''
#     '''bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'''
#     #cccccccccccccccccccccccccccccccccccccccccccccccccc
#     pass
# print(aaa.__doc__)

# class 类1:
#     def __str__(self):
#         return '字符串'
# 对象1=类1()
# 参1=对象1
# print(参1)

# aaa=open('12345.txt', encoding='utf-8')
# print(aaa.read(500))
# aaa.close()

# aaa=open('12345.txt','r',encoding='utf-8')
# aaa.write('aaa')
# aaa.close()