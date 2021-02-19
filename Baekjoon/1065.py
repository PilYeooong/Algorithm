N = int(input())
cnt = 0

for i in range(1, N+1):
    l = list(map(int, str(i)))
    n = len(l)

    if n == 1 or n == 2:
        cnt += 1
    elif n == 3:
        temp = l[0] - l[1]
        if l[1] - l[2] == temp:
            cnt += 1

print(cnt)
