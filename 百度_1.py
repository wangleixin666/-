# -*- coding:utf-8 -*-
"""
有多少长度为N+1的整数序列A0到AN，满足A0=AN=1，1≤Ai≤M且Ai≠Ai-1（1≤i≤N）。

输入
输入两个空格隔开的整数N和M，1≤N，M≤10^9。

输出
输出满足给定条件的整数序列个数对10^9+7取模后的结果。


样例输入
3 3
样例输出
2

只有{1 2 3 1}和{1 3 2 1}这两个序列满足给定条件。
"""
import sys


def func1(n):
    a = [0 for _ in range(3)]
    length = 1
    a[1] = 1
    for i in range(2, n+1):
        carry = 0
        j = 1
        while j < length+1:
            tem = a[j] * (i+carry)
            a[j] = tem
            carry = tem / 10
            if j == length and carry != 0:
                length += 1
            j += 1
    """
    for i in range(len(a)):
        print a[i]
    """
    return a[1] % (10**9+7)


def func(N, M):
    if N <= 2:
        return 1
    else:
        return func1(M-1)


def func_1(N, M):
    res = 1
    if N <= 2:
        return res % (10**9+7)
    else:
        for i in range(N-1):
            res *= (M-i-1)
        return res % (10**9+7)

if __name__ == '__main__':
    line = [int(x) for x in sys.stdin.readline().split()]
    N = line[0]
    M = line[1]
    print func_1(N, M)
