# coding:utf-8
import sys


def solution(n, m):
    if n == 0:
        return 0
    sum_score = n + m
    index = -1
    i = 0
    while i*i <= 2*sum_score:
        if i * (i+1) == 2 * sum_score:
            index = i
            break
        i += 1
    if index == -1:
        return -1
    if m == 0:
        return index
    if n > index and m > index:
        shang = n / index
        yushu = n % index
        if yushu > 0:
            return shang + 1
        else:
            return shang
    if n < index:
        return 1
    if m < index:
        return index - 1


if __name__ == '__main__':
    Line = [int(x) for x in sys.stdin.readline().split()]
    n = Line[0]
    m = Line[1]

    print solution(n, m)
"""
1 2
7 14
21 0
19 2
"""