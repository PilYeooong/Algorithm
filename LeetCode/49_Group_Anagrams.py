import collections

# defaultdict는 존재하지 않는 키를 삽입할 때 KeyError를 발생시키지 않는다.
# using defaultdict
# def solution(input_list):
#     anagrams = collections.defaultdict(list)    

#     for word in input_list:
#         anagrams[''.join(sorted(word))].append(word)

#     return anagrams.values()


# without using defaultdict
def solution(input_list):
    anagrams = {}
    
    for word in input_list:
        temp = ''.join(sorted(word))
        if temp not in anagrams:
            anagrams[temp] = []
        anagrams[temp].append(word)
    
    return anagrams.values()

input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]

answer = solution(input_list)

print(answer)