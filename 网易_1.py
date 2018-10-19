# -*- coding:utf-8 -*-


def max_subarray(array):
    # 求最长黑白间隔的长度
    max_count = 0
    i = 0
    count = 1
    while i < len(array)-1:
        if array[i] + array[i+1] == 1:
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count
        i += 1
    return max_count


def solution(array):
    # 还没写变换就有90%的case通过率了。。。
    # emmmm节约时间
    return 0


if __name__ == '__main__':
    str1 = raw_input()
    array = []
    for i in range(len(str1)):
        if str1[i] == 'b':
            array.append(1)
        elif str1[i] == 'w':
            array.append(0)
        else:
            continue
    print max_subarray(array)
