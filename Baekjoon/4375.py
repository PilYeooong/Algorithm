while True:
    try:
        n = int(input())
    except:
        break

    num = 0
    i = 1
    while True:
        num = num * 10 + 1
        num %= n
        if num == 0:
            print(i)
            break
        i += 1

# 1 % 7 = 1
# 11 % 7 = 4

# 11 % 7 == (1 % 7) * 10 + 1 == 4
