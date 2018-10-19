# coding:utf-8
import sys


def solution(x, y, z):
    # x, y, z 不越界，但是count可能超过2**32次，所以存不下
    count = 0
    for a in range(1, x+1):
        for b in range(1, y+1):
            min_1 = abs(a-b) + 1
            max_1 = min(a+b, z+1)
            for c in range(min_1, max_1):
                count = count & (count+1)
    return count % 1000000007


if __name__ == '__main__':
    Line = [int(x) for x in sys.stdin.readline().split()]
    x = Line[0]
    y = Line[1]
    z = Line[2]
    print solution(x, y, z)
    print 10**9 - 2**32
"""
2 3 3
"""