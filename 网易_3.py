# -*- coding:utf-8 -*-
import sys


def solution(array):
    font = 0
    rear = len(array)-1
    font_len = array[font]
    rear_len = array[rear]
    while font+2 <= rear:
        if font_len < rear_len:
            font += 1
            font_len += array[font]
        elif font_len < rear_len:
            rear -= 1
            rear_len += array[rear]
        else:
            if font+2 == rear and array[font+1] == font_len:
                return array[font+1]
            else:
                rear -= 1
                rear_len += array[rear]
    return False


if __name__ == '__main__':
    array = [int(x) for x in sys.stdin.readline().split()]
    print solution(array)
