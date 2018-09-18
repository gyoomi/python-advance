#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leon
# @Version : 2018/9/18 22:37

# 1.import导入模块
## ①路径搜索顺序
import sys

# print(sys.path)

## ②重新导入模块

# 2.循环导入
## 怎样避免循环导入
## ①程序设计上分层，降低耦合
## ②导入语句放在后面需要导入时再导入，例如放在函数体内导入

# 3.作用域
## ①locals和globals
# def test():
#     a = 100
#     b = 200
#     print(locals())
#
# test()
A = 100
B = 200
# print(globals(), end=",")
# LEGB 规则
## Python 使用 LEGB 的顺序来查找一个符号对应的对象
## locals -> enclosing function -> globals -> builtins

# 4.==、is
## is 是比较两个引用是否指向了同一个对象（引用比较）。
## == 是比较两个对象是否相等