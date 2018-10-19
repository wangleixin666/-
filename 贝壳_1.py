

def resolution(n):
    if n == 1:
        return 1
    k = 0
    i = 2*(n-1)
    while k < n:
        i += 1
        k = 0
        for j in range(1, i+1):
            if i % j == 0:
                k += 1
    return i


if __name__ == '__main__':
    n = int(input())
    print resolution(n)
