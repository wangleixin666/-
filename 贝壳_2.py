# -*- coding:utf-8 -*-
import sys


def resolution(array):
    res = [1 for _ in range(len(array))]
    list = []
    for i in range(len(array)):
        list.append(array[i][0])
    list1 = sorted(list)
    for i in range(len(array)):
         for j in range(i, len(array)-1):
             if array[j][0] + array[j][1] >= array[j+1][0]:
                 res[i] += 1
    result = [None for _ in range(len(list))]
    for i in range(len(list1)):
        result[list.index(list[i])] = res[i]
    return result


if __name__ == '__main__':
    n = int(input())
    array = []
    for i in range(n):
        line = [int(x) for x in sys.stdin.readline().split()]
        array.append(line)
    print resolution(array)
