# -*- coding:utf-8 -*-
import sys
import math

"""
5
1, 1
1, 1
2, 0
0, 0
3, 0
"""


def fun(array):
    res_0 = 0
    res_1 = 0
    for i in range(len(array)):
        if array[i][1] == 1:
            res_0 += 1
        else:
            res_1 += 1
    n = float(len(array))
    p_0 = res_0 / n
    p_1 = res_1 / n
    H_D = -1 * (p_0 * math.log(p_0, 2) + p_1 * math.log(p_1, 2))
    list_1 = []
    for i in range(len(array)):
        number = array[i][0]
        if number not in list_1:
            list_1.append(number)
    new_array = []
    for i in range(len(list_1)):
        list_2 = [0, 0]
        new_array.append(list_2)
    for j in range(len(list_1)):
        for i in range(len(array)):
            number = array[i][0]
            if number == list_1[j]:
                if array[i][1] == 0:
                    new_array[j][0] += 1
                else:
                    new_array[j][1] += 1
    H = 0
    for i in range(len(new_array)):
        p_00 = new_array[i][0]
        p_11 = new_array[i][1]
        add = float(p_00 + p_11)
        xishu = add / n
        if p_00 == 0 and p_11 != 0:
            H += -1 * xishu * (p_11 / add) * math.log((p_11 / add), 2)
        elif p_00 != 0 and p_11 == 0:
            H += -1 * xishu * (p_00 / add) * math.log((p_00 / add), 2)
        elif p_00 == 0 and p_11 == 0:
            H += 0
        else:
            H += -1 * xishu * ((p_00 / add) * math.log((p_00 / add), 2) + (p_11 / add) * math.log((p_11 / add), 2))
    return H_D - H

if __name__ == '__main__':
    n = int(input())
    array = []
    for i in range(n):
        line = [int(x) for x in sys.stdin.readline().split(',')]
        array.append(line)
    print "%.2f" % fun(array)
