# -*- coding:utf-8 -*-
import sys
import math


if __name__ == '__main__':
    p_list = [int(x) for x in sys.stdin.readline().split()]
    q_list = [int(x) for x in sys.stdin.readline().split()]

    dict_p = {}
    dict_q = {}

    for i in p_list:
        if i not in dict_p:
            dict_p[i] = 1
        else:
            dict_p[i] += 1

    for i in q_list:
        if i not in dict_q:
            dict_q[i] = 1
        else:
            dict_q[i] += 1

    res = 0.0
    len_p = float(len(p_list))
    len_q = float(len(q_list))
    for key, value in dict_p.items():
        p_prob = value / len_p
        if dict_q.has_key(key):
            q_prob = dict_q[key] / len_q
            res += p_prob * math.log(p_prob / q_prob, 2)

    print "%.2f" % res
