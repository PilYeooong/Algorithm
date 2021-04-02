
dp = [0 for i in range(1000001)]

dp[0] = 1
mod = 1000000009

for i in range(1, 1000001):
    if i-1 >= 0:
        dp[i] += dp[i-1]
    if i-2 >= 0:
        dp[i] += dp[i-2]
    if i-3 >= 0:
        dp[i] += dp[i-3]

    dp[i] %= mod

T = int(input())

for _ in range(T):
    n = int(input())
    print(dp[n])
