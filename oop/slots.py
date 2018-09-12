#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leon
# @Version : 2018/9/12 21:59

# 动态语言：可以在运行的过程中，修改代码
# 静态语言：编译时已经确定好代码，运行过程中不能修改


class Person(object):
    __slots__ = ("name", "age")


p = Person()
p.name = "老王"
p.age = 12
p.score = 200

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的


















