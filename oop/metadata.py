#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leon
# @Version : 2018/9/11 14:24
# 一.元类
# 1. 类也是对象


class ObjectCreate(object):
    pass


myObj = ObjectCreate()
# print(ObjectCreate)

# 2. 动态地创建类


def choose_class(name):
    if name == "foo":
        class Foo(object):
            pass
        return Foo
    elif name == "bar":
        class Bar(object):
            pass
        return Bar


myClass = choose_class("foo")
# print(myClass)
# print(myClass())

# 3.type还有一种完全不同的功能，动态的创建类
Test1 = type("Test1", (), {})
Test2 = type("Test2", (), {"foo": False})
# print(Test2.foo)

# type的第2个参数，元组中是父类的名字，而不是字符串
# 添加的属性是类属性，并不是实例属性

# 4.使用type创建带有方法的类
Foo = type("Foo", (), {"bar": False})

# 添加实例方法
# def echo_bar(self):
#     print(self.bar)

# 添加静态方法
# @staticmethod
# def echo_bar():
#     print("static method")


# 添加类方法

@classmethod
def echo_bar(cls):
    print(cls.bar)


FooChild = type("FooChild", (Foo,), {"echo_bar": echo_bar})
# print(hasattr(FooChild, "echo_bar"))
child = FooChild()
# child.bar = "haha"
# child.echo_bar()
# FooChild.echo_bar()

# 结论：在Python中，类也是对象，你可以动态的创建类。这就是当你使用关键字class时Python在幕后做的事情，而这就是通过元类来实现的。

# 5.到底什么是元类（终于到主题了）

age = 53
name = "哈哈"
print(age.__class__)
print(name.__class__)
print(age.__class__.__class__)
print(name.__class__.__class__)
print(age.__class__.__class__.__class__)
print(name.__class__.__class__.__class__)







