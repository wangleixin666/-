import sys


def printMenu(res):
    result = []
    result.append(res[0])
    for i in range(1, len(res)):
        if res[i][0] == res[i-1][0]:
            result.append(res[i][1:])
        else:
            result.append(res[i])
    return result


if __name__ == '__main__':
    n = int(input())
    res = []
    for i in range(n):
        line = [str(x) for x in sys.stdin.readline().split('\\')]
        res.append(line)
    result = printMenu(res)
    print result
    for i in range(len(result)):
        for j in range(len(result[i]) - 1):
            print result[i][j]
        print result[i][len(result[i]) - 1],
