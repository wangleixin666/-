# coding:utf-8
import sys

"""
3 4
.oxo
o..o
.xox
"""


def bianhuan(array, N, M):
    result = [['.' for _ in range(M)] for _ in range(N)]
    for i in range(M):
        low = 0
        high = N
        index = tihuan(low, high, array, result)
        tihuan(index, high, array, result)
    return result


def tihuan(low, high, array, result):
    count = 0
    index = low
    for j in range(low, high):
        if array[j][i] == 'o':
            count += 1
        if array[j][i] == 'x':
            index = j
            result[j][i] = 'x'
            for k in range(count):
                result[j-k-1][i] = 'o'
    return index

if __name__ == '__main__':
    line = [int(x) for x in sys.stdin.readline().split()]
    N = line[0]
    M = line[1]
    array = []
    for i in range(N):
        res = [None for _ in range(M)]
        string = raw_input()
        for j in range(M):
            res[j] = str(string[j])
        array.append(res)
    result = bianhuan(array, N, M)
    for i in range(len(result)):
        for j in range(len(result[0]) - 1):
            print result[i][j],
        print result[i][len(result[0]) - 1]
