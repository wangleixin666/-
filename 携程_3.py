# -*- coding:utf-8 -*-
import sys


def panduan(list):
    list_good = ['good', 'like', 'worth', 'effective']
    list_bad = ['Not', 'bad', 'low']
    for i in list:
        if i in list_good:
            return 1
        if i in list_bad:
            return 0
    return 0

if __name__ == '__main__':
    line = [str(x) for x in sys.stdin.readline().split()]
    print panduan(line)
