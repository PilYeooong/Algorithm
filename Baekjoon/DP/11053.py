n = int(input())
l = list(map(int, input().split()))

length = len(l)
dp = [1 for i in range(length+1)]

for i in range(2, length+1):
    j = 1
    while j < i:
        if l[i-1] > l[j-1]:
            dp[i] = max(dp[i], dp[j] + 1)
        j += 1
print(max(dp))
