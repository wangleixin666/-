# coding:utf-8

"""
输入
输入第一行包含6个整数n,P1,P2,P3,T1,T2, (1≤n≤100,0≤P1, P2, P3≤100, 1≤T1, T2≤60)
接下来有n行，每行有两个整数li,ri(0≤li, ri≤1440, ri<li+1)，表示一段连续的时间区间

输出
输出仅包含一个整数，表示总耗电量。

样例输入
1 3 2 1 5 10
0 10
样例输出
30
输入样例2
2 8 4 2 5 10
20 30
50 100
输出样例2
570
3 8 4 2 5 10
20 30
50 100
130 140
760
"""
import sys


def haodian(a, work):
    n = a[0]
    p1 = a[1]
    p2 = a[2]
    p3 = a[3]
    t1 = a[4]
    t2 = a[5]
    zc = [0 for i in range(n)]
    pb = [0 for i in range(n)]
    xm = [0 for i in range(n)]
    # 三个不同的状态的耗电量
    if n == 1:
        zc[0] = work[0][1] - work[0][0]
    for i in range(n - 1):
        temp = work[i+1][0] - work[i][1]
        zc[i] = work[i][1] - work[i][0]
        if (temp > t1) and (temp < t1+t2):
            zc[i] += t1
            pb[i] = temp - t1
        if temp > t1 + t2:
            zc[i] += t1
            pb[i] = t2
            xm[i] = temp - t1 - t2
        if temp < t1:
            zc[i] += temp
    zc[n-1] = work[n-1][1] - work[n-1][0]
    print zc, pb, xm
    res = 0
    for i in range(n):
        res += zc[i] * p1 + pb[i] * p2 + xm[i] * p3
    return res

if __name__ == '__main__':
    a = [int(x) for x in sys.stdin.readline().split()]
    n = a[0]
    work = []
    for i in range(n):
        line = [int(x) for x in sys.stdin.readline().split()]
        work.append(line)
    print haodian(a, work)
