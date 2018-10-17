#! coding:utf-8
import sys
import unittest

class IterTest(object):

    def __init__(self):
       self.a=0
       self.b=1
    def __iter__(self):
        self.a,self.b=self.b,self.a+self.b
        return self.b
    def next(self):
        self.a,self.b=self.b,self.a+self.b
        return self.b




def main():
    print  u"生成器列表:", sum(i**2 for i in range(1,10))
    print  u"列表表达式:", sum([i**2 for i in range(1,10)])
    for x in IterTest():
        print x

if __name__ == "__main__":
    main()
