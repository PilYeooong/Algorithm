# n 이하의 자연수 중 1을 약수로 갖는 수의 갯수 = n // 1
# n 이하의 자연수 중 2를 약수로 갖는 수의 갯수 = n // 2 (2의 배수)
# ...
# n 이하의 자연수 중 n을 약수로 갖는 수의 갯수 = n // n

n = int(input())

ans = 0

for i in range(1, n + 1):
    ans += (n // i) * i

print(ans)
