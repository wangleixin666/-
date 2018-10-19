# coding:utf-8


def solution(k, A, B):
    array_a = []
    array_b = []
    for i in range(len(A)-k+1):
        if A[i:i+k] not in array_a:
            array_a.append(A[i:i+k])
    for i in range(len(B)-k+1):
        array_b.append(B[i:i+k])
    map_1 = {}
    for i in array_b:
        if i not in map_1:
            map_1[i] = 1
        else:
            map_1[i] += 1
    count = 0
    for i in array_a:
        if not map_1.has_key(i):
            count += 0
        else:
            count += map_1[i]
        # ount += array_b.count(i)
    return count


if __name__ == '__main__':
    k = int(input())
    A = str(raw_input())
    B = str(raw_input())
    print solution(k, A, B)
"""
2
abab
ababab
"""