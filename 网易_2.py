# -*- coding:utf-8 -*-
import sys


def fun2(number):
    # reverse: array[][] * -1
    return -1 * number
"""
if ((i - 1) >=0) and ((j - 1) >= 0) and ((j + 1) < m) and ((i + 1) < n):
    fun2(array[i-1][j-1])
    fun2(array[i-1][j])
    fun2(array[i-1][j+1])
    fun2(array[i][j-1])
    fun2(array[i][j])
    fun2(array[i][j+1])
    fun2(array[i+1][j-1])
    fun2(array[i+1][j])
    fun2(array[i+1][j+1])
"""


def fun1(array):
    # 朝下为-1，朝上为1
    # 变换好变
    n = array[0]
    m = array[1]
    array = [[1 for _ in range(m)] for _ in range(n)]
    # 存放变换的二维数组
    for i in range(n):
        for j in range(m):
            array[i][j] = fun2(array[i][j])
            if (i - 1) >= 0:
                array[i - 1][j] = fun2(array[i - 1][j])
                if (j - 1) >= 0:
                    array[i - 1][j - 1] = fun2(array[i - 1][j - 1])
                if (j + 1) < m:
                    array[i - 1][j + 1] = fun2(array[i - 1][j + 1])
            if (j - 1) >= 0:
                array[i][j - 1] = fun2(array[i][j - 1])
            if (j + 1) < m:
                array[i][j + 1] = fun2(array[i][j + 1])
            if (i + 1) < n:
                array[i + 1][j] = fun2(array[i + 1][j])
                if (j - 1) >= 0:
                    array[i + 1][j - 1] = fun2(array[i + 1][j - 1])
                if (j + 1) < m:
                    array[i + 1][j + 1] = fun2(array[i + 1][j + 1])
    # 求array中-1的个数
    # array.count(-1)
    count = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] == -1:
                count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    array = []
    for i in range(n):
        line = [int(x) for x in sys.stdin.readline().split()]
        array.append(fun1(line))
    for i in range(len(array)):
        print array[i]

"""
5
1 1
1 2
3 1
4 1
2 2
"""
