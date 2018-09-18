#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leon
# @Version : 2018/9/13 14:58

# 装饰器

# 定义函数完成数据包装：


def makeBold(func):
    def wrap():
        return "<b>" + func() + "</b>"
    return wrap


def makeItalic(func):
    def wrap():
        return "<i>" + func() + "</i>"
    return wrap


@makeBold
def test01():
    return "Hello world - 01"

@makeItalic
@makeBold
def test02():
    return "Hello world - 02"


# print(test01())
# print(test02())

# 装饰器(decorator)功能
# 引入日志
# 函数执行时间统计
# 执行函数前预备处理
# 执行函数后清理功能
# 权限校验等场景
# 缓存

# 例4:装饰器中的return
from time import ctime, sleep

def time_fun(func):
    def wrapped():
        print("%s called at %s" % (func.__name__, ctime()))
        func()
        # return func()
        # 注意二者的区别： 一个打印None,二个打印“---haha---”
    return wrapped

@time_fun
def test03():
    return "---haha---"

# print(test03())

# 例5:装饰器带参数,在原有装饰器的基础上，设置外部变量
def time_fun_args(pre="hello"):
    def time_fun(func):
        def warpped():
            print("%s called at %s %s" % (func.__name__, ctime(), pre))
            return func()
        return warpped
    return time_fun


@time_fun_args(pre="python")
def test04():
    return "i am happy"


# print(test04())
# 可以理解成：foo()==timefun_arg("itcast")(foo)()

# 例6：类装饰器（扩展，非重点）

class Test(object):
    def __init__(self, func):
        print("---初始化---")
        print("func name is %s" % func.__name__)
        self.__func = func

    def __call__(self, *args, **kwargs):
        print("装饰器中功能")
        self.__func()


# t = Test()
# t()
# 装饰器函数其实是这样一个接口约束，它必须接受一个callable对象作为参数，然后返回一个callable对象。
# 在Python中一般callable对象都是函数，但也有例外。
# 只要某个对象重写了 __call__() 方法，那么这个对象就是callable的。

@Test
def test05():
    print("---test---")

test05()


















