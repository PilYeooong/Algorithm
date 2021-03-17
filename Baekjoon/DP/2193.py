dp = [[0 for _ in range(2)] for _ in range(91)]

dp[1][1] = 1
dp[2][0] = 1

n = int(input())

for i in range(3, 91):
    for j in range(2):
        if j == 0:
            dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
        if j == 1:
            dp[i][j] = dp[i-1][j-1]

print(sum(dp[n]))

# 1

# 10

# 100 101

# 1000 1001 1010

# 10000 10001 10010 10100 10101
