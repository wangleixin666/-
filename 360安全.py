# -*- coding:utf-8 -*-


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
    print num
    return num


def solution(n):
    res = sushu(n)
    result = []
    flag = True
    for i in range(len(res)):
        number = res[i]
        while number > 0:
            if number in res:
                number %= 10
            else:
                flag = False
                break
        if flag is True:
            result.append(res[i])
    return result


def fun_2(n):
    # 完美素数
    res = [2, 3, 5, 7]
    flag = True
    if n <= 10:
        if n not in res:
            flag = False
    else:
        j = 2
        while j * j < n:
            if n % j == 0:
                flag = False
                break
            else:
                j += 1
    while n > 10:
        if n % 10 in res and n/10 in res:
            n /= 10
        else:
            flag = False
            break
    return flag


def fun(n):
    res = []
    for i in range(n*100):
        if fun_2(i):
            res.append(i)
    print res
    return res[n]


if __name__ == '__main__':
    n = int(input())
    print fun(n)
