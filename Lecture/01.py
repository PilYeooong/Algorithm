# 1
# def solution(n):
#     total = 0
#     for i in range(1, n+1):
#         if i % 3 == 0  or i % 5 == 0:
#             total += i
#     return total

# n = int(input())
# ans = solution(n)
# print(ans)

# 2
# def solution(l, n):
#     for i in range(0, n):
#         for j in range(i + 1, n):
#             if l[i] + l[j] == 100:
#                 return 1
#     return 0

# l = [50, 42]

# ans = solution(l, len(l))
# print(ans)


# 3
# def solution(n):
#     is_square = n ** 0.5
    
#     if int(is_square) == is_square:
#         if n == is_square ** 2:
#             return 1
#     return 0

# n = int(input())

# ans = solution(n)
# print(ans)

# 4
# def solution(n):
#     case = 1
#     while (2 * case <= n):
#         case *= 2
#     return case

# n = int(input())

# ans = solution(n)
# print(ans)