# coding:utf-8
import sys


def solution(array):
    guiji = []
    chaxun = []
    count = 0
    res = []
    for i in range(len(array)):
        if array[i][0] == 'T':
            guiji.append(array[i])
            count += 1
        if array[i][0] == 'Q':
            chaxun.append(array[i])
            res.append(count)
            count = 0
    return res


if __name__ == '__main__':
    n = int(input())
    res = []
    j = n
    while j > 0:
        m = int(input())
        array = []
        for i in range(m):
            Line = [x for x in sys.stdin.readline().split()]
            array.append(Line)
        res.append(solution(array))
        j -= 1
    for i in range(len(res)-1):
        for j in range(len(res[i])-1):
            print res[i][j]
        print sum(res[i])
        print '\n',
    for j in range(len(res[len(res)-1])):
        print res[len(res)-1][j]

"""
2
8
T 0 0 10 0
T 5 0 15 0
Q 1
T 0 1 10 1
T 5 1 15 1
Q 4
T 1 -1 1 1
Q 1
3
T 0 0 1 1
T 0 1 1 0
Q 2
"""