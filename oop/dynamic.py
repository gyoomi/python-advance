#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leon
# @Version : 2018/9/11 17:22

# 1.python是动态语言


class Person(object):
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def eat(self):
        print("eat food")


# 运行的过程中给对象绑定(添加)属性
# p = Person("tom", 23)
# p.sex = None
# print(p.sex)

# 运行的过程中给类绑定(添加)属性
# Person.sex = 11
# p = Person("tom", 23)
# print(p.sex)

# 运行的过程中给类绑定(添加)方法

def run(self, speed):
    print("%s在以%d速度移动" %(self.name, speed))


p = Person("tom", 23)
import types

p.run = types.MethodType(run, p)
p.run(99)




