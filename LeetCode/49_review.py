input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]


def solution(l):
    d = {}

    for word in l:
        if ''.join(sorted(word)) not in d:
            d[''.join(sorted(word))] = [word]
        else:
            d[''.join(sorted(word))].append(word)
    print(d.values())


solution(input_list)
