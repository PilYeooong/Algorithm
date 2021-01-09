import re
from collections import Counter

def solution(paragraph, banned):
    trans = re.sub(r'[^\w]', ' ', paragraph.lower())
    checklist = [word for word in trans.split() if word not in banned]
    counter = Counter(checklist)

    common_word = counter.most_common()[0][0]
    
    return common_word
    
paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit.'
banned = ['hit']

answer = solution(paragraph, banned)

print(answer)