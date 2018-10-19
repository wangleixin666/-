# coding:utf-8
"""
只能是增或者减的序列
求最小的输出次数
第一行为个数
第二行为数字
5
3 5 2 4 1
输出 2
6
1 2 4 3 3 3
输出 3


"""

import sys

n = int(input())
line = sys.stdin.readline().split()
print n / 2
