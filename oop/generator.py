#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leon
# @Version : 2018/9/12 22:13

# 生成器
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# 1.创建生成器方法1
L = [x*2 for x in range(5)]
# print(L)
G = (x*2 for x in range(5))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
# print(next(G))
#  L 和 G 的区别仅在于最外层的 [ ] 和 ( ) ， L 是一个列表，而 G 是一个生成器















