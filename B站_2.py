import sys


def solution(matrix):
    m = len(matrix)
    n = len(matrix[0])
    output = []
    startX= 0
    endX = n - 1
    startY = 0
    endY = m - 1

    while True:
        if startX > endX:
            break
        for i in range(startX, endX + 1, 1):
            output.append(matrix[startY][i])
        startY += 1

        if startY > endY:
            break
        for j in range(startY, endY + 1, 1):
            output.append(matrix[j][endX])
        endX -= 1

        if startX > endX:
            break
        for i in range(endX, startX -1 , -1):
            output.append(matrix[endY][i])
        endY -= 1

        if startY > endY:
            break
        for j in range(endY, startY -1 , -1):
            output.append(matrix[j][startX])
        startX += 1
    return output


if __name__ == '__main__':
    result = []
    while True:
        line = [int(x) for x in sys.stdin.readline().split()]
        m = int(line[0])
        n = int(line[1])
        new_array = []
        if m != -1 and n != -1:
            for i in range(m):
                array = [int(x) for x in sys.stdin.readline().split()]
                new_array.append(array)
            result.append(new_array)
        else:
            break
    for i in range(len(result)):
        res = solution(result[i])
        string = ''
        for i in range(len(res)-1):
            string = string + str(res[i]) + ','
        string += str(res[len(res)-1])
        print string

"""
3 3
1 2 3
4 5 6
7 8 9
3 3
1 2 3
4 5 6
7 8 9
-1 -1
"""