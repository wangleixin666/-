# coding:utf-8

import sys


def solution(P, line_2, array):
    for i in range(len(array)):
        n = int(array[i][1])
        if array[i][0] == 'A':
            line_2[n-1] += 1
        if array[i][0] == 'B':
            line_2[n-1] -= 1
    num = line_2[P-1]
    new_array = sorted(line_2, reverse=True)
    return new_array.index(num) + 1


if __name__ == '__main__':
    line_1 = [int(x) for x in sys.stdin.readline().split()]
    N = line_1[0]
    M = line_1[1]
    P = line_1[2]
    line_2 = [int(x) for x in sys.stdin.readline().split()]
    array = []
    for i in range(M):
        line = [x for x in sys.stdin.readline().split()]
        array.append(line)
    print solution(P, line_2, array)
"""
3 4 2
5 3 1
B 1
A 2
A 2
A 3
"""