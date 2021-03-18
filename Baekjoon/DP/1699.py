# 1 - 1 = 1
# 2 - 1 + 1 = 2
# 3 - (1+1+1) = 3
# 4 - (2^2), (1+1+1+1) = 1
# 5 - (2^2+1), (1+1+1+1+1) = 2
# 6 - (2^2+1+1) = 3
# 7 = (2^2+1+1+1) = 4
# 8 = (2^2+2^2) = 2

N = int(input())

dp = [0 for i in range(N+1)]

for i in range(1, N+1):
    dp[i] = i
    j = 1
    while j*j <= i:
        if dp[i] > dp[i-j*j]+1:
            dp[i] = dp[i-j*j]+1
        j += 1
print(dp[N])
