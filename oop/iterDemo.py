#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leon
# @Version : 2018/9/13 11:16

from collections import Iterator
from collections import Iterable

# 迭代器
# 1.可迭代的对象
#   一类是集合数据类型，如 list 、 tuple 、 dict 、 set 、 str 等；
#   一类是 generator ，包括生成器和带 yield 的generator function。
#   这些可以直接作用于 for 循环的对象统称为可迭代对象： Iterable


# 2.判断是否可以迭代
#    isinstance() 判断一个对象是否是 Iterable 对象
# print(isinstance([], Iterable))
# print(isinstance({}, Iterable))
# print(isinstance(100, Iterable))

# 3.迭代器
#   可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
#   可以使用 isinstance() 判断一个对象是否是 Iterator 对象
r1 = isinstance((x for x in range(10)), Iterator)
# print(r1)
r2= isinstance([], Iterator)
# print(r2)
r3= isinstance({}, Iterator)
# print(r3)
r4= isinstance(123, Iterator)
# print(r4)
r5= isinstance("abc", Iterator)
# print(r5)

# 4.iter()函数
#   生成器都是 Iterator 对象，但 list 、 dict 、 str 虽然是 Iterable ，却不是 Iterator 。
#   把 list 、 dict 、 str 等 Iterable 变成 Iterator 可以使用 iter() 函数
isinstance(iter([]), Iterator)
isinstance(iter("abcd"), Iterator)

# 5.总结
#   凡是可作用于 for 循环的对象都是 Iterable 类型；
#   凡是可作用于 next() 函数的对象都是 Iterator 类型
#   集合数据类型如 list 、 dict 、 str 等是 Iterable 但不是 Iterator ，不过可以通过 iter() 函数获得一个 Iterator 对象。
list = [1, True, "hello"]
# for item in list:
#     print(item)
listIter = iter(list)
print(next(listIter))
print(next(listIter))















