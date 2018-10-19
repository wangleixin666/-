import sys


def chaifen(string):
    array = [int(x) for x in string.split('.')]
    return array


def compare(array_1, array_2):
    if len(array_1) == 0 and len(array_2) == 0:
        return 0
    elif len(array_1) == 0 and len(array_2) != 0:
        return -1
    elif len(array_1) != 0 and len(array_2) == 0:
        return 1
    else:
        if array_1[0] < array_2[0]:
            return -1
        elif array_1[0] > array_2[0]:
            return 1
        else:
            return compare(array_1[1:], array_2[1:])


if __name__ == '__main__':
    array = [str(x) for x in sys.stdin.readline().split()]
    v_1 = array[0]
    version_1 = chaifen(v_1)
    v_2 = array[1]
    version_2 = chaifen(v_2)
    print compare(version_1, version_2)
