import sys
"""
3
5,5,7
6,7,8
2,2,4
"""


def MinNumber(array):
    res = [[0 for _ in range(len(array))] for _ in range(len(array))]
    res[0][0] = array[0][0]
    for i in range(1, len(array[0])):
        res[0][i] = res[0][i-1] + array[0][i]
    for i in range(1, len(array)):
        res[i][0] = res[i-1][0] + array[i][0]
    for i in range(1, len(array)):
        for j in range(1, len(array[0])):
            res[i][j] = min(res[i-1][j], res[i][j-1]) + array[i][j]
    return res[len(array)-1][len(array)-1]


if __name__ == '__main__':
    n = int(input())
    new_array = []
    for i in range(n):
        array = [int(x) for x in sys.stdin.readline().split(',')]
        new_array.append(array)
    print MinNumber(new_array)
