# coding:utf-8

import sys


def solution(array):
    for i in range(len(array)):
        if array[i][0] > array[i][1]:
            array[i][0], array[i][1] = array[i][1], array[i][0]
    array.sort(key=lambda x: x[0])
    s = []
    f = []
    for i in range(len(array)):
        s.append(array[i][0])
        f.append(array[i][1])
    max_count = 0
    for j in range(len(f)):
        count = 1
        for i in range(1, len(s)):
            if s[i] >= f[j]:
                count += 1
                j = i
        if count > max_count:
            max_count = count
    return max_count


if __name__ == '__main__':
    n = int(input())
    array = []
    for i in range(n):
        line = [int(x) for x in sys.stdin.readline().split('  ')]
        array.append(line)
    print solution(array)
