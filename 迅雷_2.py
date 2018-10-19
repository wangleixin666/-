# -*- coding:utf-8 -*-
import sys


def solution(list_1, list_2, k):
    list_1.sort(reverse=True)
    list_2.sort(reverse=True)
    res = []
    for i in range(len(list_1)):
        res.append(list_2[0] + list_1[i])
    for i in range(len(list_2)):
        j = 0
    return list_1, list_2, k


if __name__ == '__main__':
    array = [x for x in sys.stdin.readline().split(':')]
    # 2,4,2,7,7-3,2,5,6,1,9:6
    # 16,16,13,13,13,12
    k = array[1]
    array_1 = [x for x in array[0].split('-')]
    list_1 = [int(x) for x in array_1[0].split(',')]
    list_2 = [int(x) for x in array_1[1].split(',')]
    print solution(list_1, list_2, k)
