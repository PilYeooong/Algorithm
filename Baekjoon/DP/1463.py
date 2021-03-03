MAX = 1000000

dp = [0] * (MAX+1)
dp[1] = 0
dp[2] = 1
dp[3] = 1
for i in range(4, MAX+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
        dp[i] = dp[i // 3] + 1
    if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
        dp[i] = dp[i // 2] + 1

n = int(input())
print(dp[n])
