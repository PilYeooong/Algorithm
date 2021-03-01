import sys

N, M = map(int, input().split())

a = [0] * M
check = [False] * (N+1)


def solution(index, start, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, a)) + '\n')
        return
    for i in range(start, n+1):
        if check[i]:
            continue
        check[i] = True
        a[index] = i
        solution(index + 1, i + 1, n, m)
        check[i] = False


solution(0, 1, N, M)
