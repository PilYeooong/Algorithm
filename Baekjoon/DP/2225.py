N, K = map(int, input().split())

dp = [[0 for _ in range(N+1)] for _ in range(K+1)]

dp[0][0] = 1

for i in range(1, K+1):
    for j in range(0, N+1):
        for k in range(0, j+1):
            dp[i][j] += dp[i-1][j-k]
        dp[i][j] %= 1000000000

print(dp[K][N])
