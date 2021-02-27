dp = [0] * 11

dp[1] = 1
dp[2] = 2
dp[3] = 4

length = len(dp)

for i in range(4, length):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

T = int(input())

for i in range(T):
    t = int(input())
    print(dp[t])
