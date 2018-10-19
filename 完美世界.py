import sys


def MinNumber(n, m, array):
    number = [0 for _ in range(n)]
    array.sort(reverse=True)
    i = 0
    jiage = m
    while i < len(array) and jiage >= 0:
        number[i] = int(jiage / array[i])
        jiage -= number[i] * array[i]
        i += 1
    sum_number = 0
    for j in range(len(array)):
        sum_number += number[j]
    if jiage > 0:
        return -1
    else:
        return sum_number

if __name__ == '__main__':
    n = int(input())
    array = [int(x) for x in sys.stdin.readline().split()]
    m = int(input())
    print MinNumber(n, m, array)
