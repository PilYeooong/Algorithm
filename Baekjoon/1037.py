n = int(input())
divisor = list(map(int, input().split()))

ans = max(divisor) * min(divisor)
print(ans)
