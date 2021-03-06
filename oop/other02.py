#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leon
# @Version : 2018/9/20 15:06
# 垃圾回收
## 1.小正数对象池
### 整数在程序中的使用非常广泛，Python为了优化速度，使用了小整数对象池， 避免为整数频繁申请和销毁内存空间。
### Python 对小整数的定义是 [-5, 257) 这些整数对象是提前建立好的，不会被垃圾回收。在一个 Python 的程序中，所有位于这个范围内的整数使用的都是同一个对象.
### 同理，单个字母也是这样的。但是当定义2个相同的字符串时，引用计数为0，触发垃圾回收

## 2.大整数对象池
### 每一个大整数，均创建一个新的对象。

## 3.intern机制
### 小整数[-5,257)共用对象，常驻内存
### 单个字符共用对象，常驻内存
### 单个单词，不可修改，默认开启intern机制，共用对象，引用计数为0，则销毁

# 垃圾回收(二)






