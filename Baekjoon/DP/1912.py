n = int(input())
l = list(map(int, input().split()))

dp = [0 for i in range(n)]

for i in range(n):
    dp[i] = max(l[i], dp[i-1] + l[i])

print(max(dp))
