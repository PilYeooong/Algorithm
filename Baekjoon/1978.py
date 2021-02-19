# 2 - 루트 n까지 검사

def is_prime(num):
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if (num % i) == 0:
            return False
        i += 1
    return True


N = int(input())
nums = list(map(int, input().split()))
ans = 0
for num in nums:
    if is_prime(num):
        ans += 1

print(ans)
