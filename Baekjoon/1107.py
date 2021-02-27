broken = [False] * 10
N = int(input())
M = int(input())


if M > 0:
    b = list(map(int, input().split()))
    for i in b:
        broken[i] = True
else:
    b = []


def possible(n):
    if n == 0:
        if broken[n]:
            return 0
        else:
            return 1
    l = 0
    while n > 0:
        if broken[n % 10]:
            return 0
        l += 1
        n //= 10
    return l


ans = abs(N - 100)
for i in range(0, 1000000 + 1):
    channel = i
    l = possible(channel)
    if l > 0:
        press = abs(channel - N)
        if ans > l + press:
            ans = l + press

print(ans)
