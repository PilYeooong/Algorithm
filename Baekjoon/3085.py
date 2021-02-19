def check(board):
    ans = 1
    n = len(board)
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
        cnt = 1
        for j in range(1, n):
            if board[j][i] == board[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
    return ans


N = int(input())
board = [list(input()) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(N):
        if j + 1 < N:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            temp = check(board)
            if ans < temp:
                ans = temp
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
        if i + 1 < N:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            temp = check(board)
            if ans < temp:
                ans = temp
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
print(ans)
