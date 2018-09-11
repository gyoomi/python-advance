#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leon
# @Version : 2018/9/11 11:34

# 1.for循环
s = "hello python"
for item in s:
    print(item, end=",")
else:
    print("没有数据")

print("-" * 40)
# 注意：如果碰见break和return，else后面的语句不会执行，否则的话else后面的代码就会正常执行

# 2.字符串和下标
# 说明：列表与元组支持下标索引好理解，字符串实际上就是字符的数组，所以也支持下标索引。
# 反转字符串
s2 = "hello world"
print(s2[::-1])
print(s2[0:-1])
print("-" * 40)


# 3.Number
# type()不会认为子类是一种父类类型
# isinstance()会认为子类是一种父类类型
# 注意：在 Python2 中是没有布尔型的，它用数字0表示 False，用1表示True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。
f = True
d = False
print(f + 1)
print("-" * 40)

# 4.Set（集合）
# 基本功能是进行成员关系测试和删除重复元素
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
a = set("srerwerw")
b = set("oijnwer")
print("-" * 40)














