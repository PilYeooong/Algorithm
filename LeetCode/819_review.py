import re
from collections import Counter

paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit.'
banned = ['hit']


def solution(paragraph, banned):
    trans = re.sub(r'[^\w]', ' ', paragraph)
    check = [word for word in trans.lower().split() if word not in banned]
    d = {}
    for w in check:
        if w not in d:
            d[w] = 1
        else:
            d[w] += 1
    return Counter(d).most_common()[0][0]


ans = solution(paragraph, banned)
