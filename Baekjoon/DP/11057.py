N = int(input())

dp = [[0 for _ in range(10)] for _ in range(1001)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]  # 맨 마지막자리 j를 없앴을때 올수있는 앞자리의 모든 경우의수를 더한다.
            dp[i][j] %= 10007
ans = sum(dp[N])
print(ans % 10007)
