# coding:utf-8
# 最长公共子序列
"""
abcd1e1f1
bcd2e2f2

5
"""


def solution(s_1, s_2):
    if len(s_1) == 0 or len(s_2) == 0:
        return 0
    array = [[0 for _ in range(len(s_1))] for _ in range(len(s_2))]
    # s_2行，s_1列
    i = 0
    while i < len(s_2) and s_2[i] != s_1[0]:
        i += 1
    for j in range(i, len(s_2)):
        array[j][0] = 1
    i = 0
    while i < len(s_1) and s_1[i] != s_2[0]:
        i += 1
    for j in range(i, len(s_1)):
        array[0][j] = 1
    for i in range(1, len(s_2)):
        for j in range(1, len(s_1)):
            if s_2[i] == s_1[j]:
                array[i][j] = array[i-1][j-1] + 1
            else:
                array[i][j] = max(array[i-1][j], array[i][j-1])
    return array[-1][-1]


if __name__ == '__main__':
    s_1 = raw_input()
    s_2 = raw_input()
    print solution(s_1, s_2)

"""
9
34
"""