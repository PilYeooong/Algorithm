N = int(input())
dp = [[0, 0, 0] for i in range(N+1)]
a = [(0, 0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]

for i in range(1, N+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + a[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + a[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + a[i][2]

print(min(dp[N][0], dp[N][1], dp[N][2]))
