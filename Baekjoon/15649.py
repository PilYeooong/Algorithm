import sys

N, M = map(int, input().split())

check = [False] * (N+1)
a = [0] * M


def solution(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, a)) + '\n')
        return
    for i in range(1, n + 1):
        if check[i]:
            continue
        check[i] = True
        a[index] = i
        solution(index + 1, n, m)
        check[i] = False


solution(0, N, M)
