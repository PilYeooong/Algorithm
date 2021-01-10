# 메모리 초과
# not DP way
# N = int(input())

# l = [N]

# count = 0

# while True:
#     temp = []
#     for i in l:
#         temp.append(i-1)
#         if i % 3 == 0:
#             temp.append(i / 3)
#         if i % 2 == 0:
#             temp.append(i / 2)
#     count += 1
#     if min(temp) == 1:
#         print(count)
#         break
#     l = temp

def solution(number):
    dp = [0 for _ in range(1000001)]
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1

    for i in range(4, number + 1):
        dp[i] = dp[i - 1] + 1
        if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1
        if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1
    return dp[number]

N = int(input())

answer = solution(N)
print(answer)
    