# coding:utf-8
"""
    给定一个长度为N的序列A1到AN，求所有区间[L，R]（1≤L≤R≤N）的极差之和
    其中区间[L，R]的极差定义为AL到AR中的最大值与最小值之差
    第一行包含一个整数N，1≤N≤105。
    第二行包含N个空格隔开的整数A1到AN，1≤Ai≤105
    输出所有区间的极差之和。
5
4 1 8 2 5
    6
"""
import sys


def sum_of_jizhi(a, n):
    sum = 0
    # 长度为2的
    for i in range(n - 1):
        j = i+1
        min_1 = min(a[i], a[i + 1])
        max_1 = max(a[i], a[i + 1])
        while j < n:
            if a[j] > max_1:
                max_1 = a[j]
            if a[j] < min_1:
                min_1 = a[j]
            jizhi = max_1 - min_1
            sum += jizhi
            j += 1
    return sum


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in sys.stdin.readline().split()]
    print sum_of_jizhi(a, n)

"""
for j in range(i+2, n+1):
    print a[i:j]
    sum += max(a[i:j]) - min(a[i:j])
    print sum
[4, 1]
3
[4, 1, 8]
10
[4, 1, 8, 2]
17
[4, 1, 8, 2, 5]
24
[1, 8]
31
[1, 8, 2]
38
[1, 8, 2, 5]
45
[8, 2]
51
[8, 2, 5]
57
[2, 5]
60
"""