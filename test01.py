#coding: utf8
#auth:wsg

import time
from selenium import webdriver

# 计算 1 + 11 + 111 + 1111 + 11111 的和

def atest(num,count):
    li = []
    j = 0
    for i in range(1,count+1):
        a = num
        b =10**(i-1)
        c = a*b
        j = j + c
        li.append(j)
    a = 0
    for jj in li:
        a = a+jj
    print(a)





if __name__ == '__main__':
    pass

    atest(1,8)
