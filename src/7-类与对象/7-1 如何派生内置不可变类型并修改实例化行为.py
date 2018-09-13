# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
实际案例:
    我们想要自定义一种新类型的 tuple, 对于传入的可迭代对象, 我们只保留其中 int 类型且值大于
0的元素, 例如:
    IntTuple([1, -1, 'abc', 6, ['x', 'y'], 3]) ==> (1, 6, 3)

要求 IntTuple 是内置 tuple 的子类, 如何实现?
'''

'''
解决方案:
    定义类 IntTuple 继承内置 tuple, 并实现构造器__new__(), 修改实例化行为
'''
class IntTuple(tuple):
    
    def __new__(cls, iterable):     # cls指定类对象
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple, cls).__new__(cls, g)
        
    def __init__(self, iterable):
        #before 不可行
        # when pass self to __init__(), instance of tuple is established.
        print(self)
        super(IntTuple, self).__init__()
        #after 不可行
        
t = IntTuple([1, -1, 'abc', 6, ['x', 'y'], 3])
print(t)