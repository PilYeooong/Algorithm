MAX = 1000
dp = [0] * (MAX+1)
dp[1] = 1
dp[2] = 2

for i in range(3, MAX+1):
    dp[i] = dp[i-1] + dp[i-2]

n = int(input())
print(dp[n] % 10007)
