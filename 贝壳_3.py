# -*- coding:utf-8 -*-


def fun3(n):
    res = 0
    for i in range(n+1):
        j = i
        while j > 0:
            res += (j % 2)
            j /= 2
    return res


n = int(input())
print fun3(n)