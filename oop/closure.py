#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leon
# @Version : 2018/9/13 14:12

# 1.闭包


def test1():
    print("----in test1 func-----")


# test1()

rt = test1
print(id(test1))
print(id(rt))
# 通过引用调用函数
# rt()


# 2.什么是闭包
def test(number):
    def test_in(number_in):
        print("test_in 函数参数是：%d" % number_in)
        return number + number_in
    return test_in


rt = test(10)
# print(rt(100))
# print(rt(200))

# 3.闭包再理解
#   内部函数对外部函数作用域里变量的引用（非全局变量），则称内部函数为闭包。


# def counter(start=0):
#     count = [start]
#
#     def incr():
#         count[0] += 1
#         return count[0]
#     return incr
#
# c = counter(100)
# print(c())
# print(c())

# 4.nonlocal访问外部函数的局部变量(python3)
def counter(start=0):
    def incr():
        nonlocal start
        start += 1
        return start
    return incr

c = counter(88)
# print(c())
# print(c())

# 5.闭包的实际例子

# 闭包思考
#   1.闭包似优化了变量，原来需要类对象完成的工作，闭包也可以完成
#   2.由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存





