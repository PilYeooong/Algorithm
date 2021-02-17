S = list(input())

ans = [0 for i in range(26)]

for i in S:
    idx = ord(i) - 97
    ans[idx] += 1

for s in ans:
    print(s, end=' ')