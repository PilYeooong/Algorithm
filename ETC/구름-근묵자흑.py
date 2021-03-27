# 4 3
# 2 3 1 4

# 2

# 8 3
# 7 3 1 8 4 6 2 5

# 4

N, K = 8, 3
l = [7, 3, 1, 8, 4, 6, 2, 5]

count = 0

while True:
    index = 0
    if index >= N:
        break
    elif index == 0:
        index += K
    else:
        index += K-1
    count += 1

print(count)
