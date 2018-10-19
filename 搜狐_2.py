# coding:utf-8


def sushu(n):
    num = []
    for i in range(2, n):
        flag = True
        j = 2
        while j*j <= i:
            if i % j == 0:
                flag = False
                break
            else:
                j += 1
        if flag is True:
            num.append(i)
    return num


def solution(n):
    res = sushu(n)
    count = 0
    i = 0
    while i <= n/2:
        if i in res and (n-i) in res:
            count += 1
        i += 1
    return count


if __name__ == '__main__':
    n = int(input())
    print solution(n)
"""
3 4 2
5 3 1
B 1
A 2
A 2
A 3
"""