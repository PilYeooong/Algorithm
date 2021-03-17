n = int(input())
l = list(map(int, input().split()))
length = len(l)

dp = [1 for i in range(length+1)]
v = [0 for i in range(length+1)]

for i in range(2, length+1):
    j = 1
    while i > j:
        if l[i-1] > l[j-1]:
            if dp[j]+1 > dp[i]:
                dp[i] = dp[j]+1
                v[i] = j
        j += 1


index = dp.index(max(dp))
ans = []
while True:
    ans.append(l[index-1])
    index = v[index]
    if index == 0:
        break
print(max(dp))
print(' '.join(map(str, reversed(ans))))
