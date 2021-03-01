import sys

N, M = map(int, input().split())

a = [0] * M


def solution(index, start, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, a)) + '\n')
        return
    for i in range(start, n + 1):
        a[index] = i
        solution(index + 1, i, n, m)


solution(0, 1, N, M)
