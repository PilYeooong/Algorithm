import sys
l = []
for i in range(9):
    n = int(input())
    l.append(n)

l.sort()
total = sum(l)
for i in range(9):
    for j in range(i + 1, 9):
        if total - l[i] - l[j] == 100:
            for k in range(9):
                if i == k or j == k:
                    continue
                print(l[k])
            sys.exit(0)
