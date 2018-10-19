# coding:utf-8


def solution(n):
    array = []
    array.append(1)
    array.append(1)
    for i in range(2, n):
        array.append(array[i-1]+array[i-2])
    return array[n-1]


if __name__ == '__main__':
    n = int(input())
    print solution(n)
"""
9
34
"""