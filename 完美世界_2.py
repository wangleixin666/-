import sys


def MinNumber(map):
    res = [[0 for _ in range(m)] for _ in range(n)]
    res[0][0] = map[0][0]
    for i in range(1, len(map[0])):
        res[0][i] = res[0][i-1] + map[0][i]
    for i in range(1, len(map)):
        res[i][0] = res[i-1][0] + map[i][0]
    for i in range(1, len(map)):
        for j in range(1, len(map[0])):
            res[i][j] = max(res[i-1][j], res[i][j-1]) + map[i][j]
    # print res
    """
    result = map[0][0]
    for i in range(len(map) - 1):
        for j in range(len(map[0]) - 1):
            if res[i][j+1] < 0 and res[i+1][j] < 0:
                temp = max(res[i][j+1], res[i+1][j])
                if temp < result:
                    result = temp
    """
    result = res[len(map)-1][len(map[0])-1]
    if result >= 0:
        return 0
    return -result + 1


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    array = [int(x) for x in sys.stdin.readline().split()]
    map = [[0 for _ in range(m)] for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(m):
            map[i][j] = array[index]
            index += 1
    print MinNumber(map)
