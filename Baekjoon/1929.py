# def is_prime(num):
#     if num < 2:
#         return False
#     i = 2
#     while i * i <= num:
#         if (num % i) == 0:
#             return False
#         i += 1
#     return True


# M, N = map(int, input().split())

# for i in range(M, N + 1):
#     if is_prime(i):
#         print(i)

# ----
# 에라토스테네스의 체를 활용

MAX = 1000000

check_primes = [False] * (MAX + 1)
check_primes[0] = check_primes[1] = True

for i in range(2, MAX + 1):
    if check_primes[i] == False:
        for j in range(i * i, MAX + 1, i):
            check_primes[j] = True

M, N = map(int, input().split())
for i in range(M, N + 1):
    if check_primes[i] == False:
        print(i)
