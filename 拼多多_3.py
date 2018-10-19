# coding:utf-8
import sys


def result(a, b):
    index = 0
    length = 0
    shang = float(a) / b
    str1 = str(shang)
    list1 = []
    for i in range(len(str1) - 1):
        if str1[i] == '.':
            list1.extend(str1[i+1:])
    res = [int(x) for x in list1]
    if len(res) < 12:
        index = len(res)
        length = 0
    for i in range(len(res) - 1):
        if res[i+1] == res[i]:
            index = i
            length = 1
            break
    return index, length


if __name__ == '__main__':
    line = [int(x) for x in sys.stdin.readline().split()]
    a = line[0]
    b = line[1]
    index, length = result(a, b)
    print index,
    print length
