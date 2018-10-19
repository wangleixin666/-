# coding:utf-8
import sys


def fun(n):
    if n == 1:
        return n
    return n * fun(n-1)


def solution(array):
    np = array[0]
    nq = array[1]
    nr = array[2]
    if array.count(0) >= 2:
        return 0
    return fun(np+nq+nr) / (fun(np)*fun(nq)*fun(nr)) - fun(nq+nr+1)


def fun_1(a, b, c):
    global count
    a -= 1
    while b >= 0:
        count += fun_1(b, a, c)
        count += fun_1(b, c, a)
        b -= 1
    while c >= 0:
        count += fun_1(c, a, b)
        count += fun_1(c, b, a)
        c -= 1
    return 1

if __name__ == '__main__':
    array = [int(x) for x in sys.stdin.readline().split()]
    array.sort(reverse=True)
    a = array[0]
    b = array[1]
    c = array[2]
    count = 0
    print fun_1(a, b, c)
    print count
    # print solution(array)
"""
2 3 3
"""