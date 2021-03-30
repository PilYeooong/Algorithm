s = 'A man, a plan, a canal: Panama'
# s = 'race a car'


def solution(s):
    l = []
    for w in s:
        if w.isalnum():
            l.append(w.lower())

    while len(l) > 1:
        if l.pop(0) != l.pop():
            return False
    return True


ans = solution(s)

print(ans)
