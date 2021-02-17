# BFS
# def solution(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
                
nums = [2, 7, 11, 15]
target = 13
# answer = solution(nums, target)
# print(answer)

# for in
for i, n in enumerate(nums):
    complement = target - n
    
    if complement in nums[i + 1:]:
        print(nums.index(n), nums.index(complement))