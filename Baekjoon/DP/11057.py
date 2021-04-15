N = int(input())

dp = [[for _ in range(10)] for _ in range(1001)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = sum(dp[i-1])
        elif j == 9:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i][j-1] - dp[i-1][j-1]
