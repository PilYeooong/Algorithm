import sys

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

ans = 0

for i in range(N):
    for j in range(i+1, N-1):
        for k in range(j + 1, N):
            total = 0
            total += cards[i] + cards[j] + cards[k]
            if ans < total and total <= M:
                ans = total
print(ans)
