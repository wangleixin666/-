# coding=utf-8
"""
import sys


if __name__ == '__main__':
    lines = [int(x) for x in sys.stdin.readline().split()]
    n = lines[0]
    k = lines[1]
    score = [int(x) for x in sys.stdin.readline().split()]
    wake = [int(x) for x in sys.stdin.readline().split()]
    win = [0 for i in range(k)]
    res = 0
    i = 0
    maxwin = 0
    while i < n:
        if wake[i] != 0:
            res += score[i]
        for j in range(i, min(n, i+k)):
            if wake[j] == 0:
                win[j - i] = score[j]
        sum = 0
        for m in range(k):
            sum += win[m]
            win[m] = 0
        if sum > maxwin:
            maxwin = sum
        i += 1
    print res + maxwin
"""

"""
1
1 1 0 0
-1 1 0 0
-1 1 0 0
1 -1 0 0
1 1 0 0
-1 1 0 0
-1 1 0 0
1 -1 0 0

data = [[1, 1, 0, 0], [-1, 1, 0, 0], [-1, 1, 0, 0], [1, -1, 0, 0]]
坐标变换:x,y绕ab逆时针旋转90度后
x1 = a - y + b
y1 = x - a + b
构成正方形：
一组邻边相等并且不为0
有一个直角，也就是两条线垂直
(y3 - y2) * (y1 - y2) + (x3 - x2) * (x1 - x2) == 0
(y2 - y1)**2 + (x2 - x1)**2 == (y3 - y2)**2 + (x3 - x2)**2
"""
import sys


def move(data):
    x = [0 for i in range(len(data))]
    y = [0 for i in range(len(data))]
    a = [0 for i in range(len(data))]
    b = [0 for i in range(len(data))]
    for i in range(len(data)):
        x[i], y[i], a[i], b[i] = data[i][0], data[i][1], data[i][2], data[i][3]
    number = 0
    if [(y[3] - y[2]) * (y[1] - y[2]) + (x[3] - x[2]) * (x[1] - x[2]) == 0] and [(y[2] - y[1]) ** 2 + (x[2] - x[1]) ** 2 == (y[3] - y[2]) ** 2 + (x[3] - x[2]) ** 2]:
        return number
    else:
        x[1] = a[1] - y[1] + b[1]
        y[1] = x[1] - a[1] + b[1]
        number += 1
        return number

if __name__ == '__main__':
    n = int(input())
    result = []
    for i in range(0, 4 * n, 4):
        data = []
        for j in range(i, i+4, 1):
            lines = [int(x) for x in sys.stdin.readline().split()]
            data.append(lines)
        result.append(move(data))
    for i in range(n):
        print result[i]

