import sys
sys.stdin = open("input.txt", "r")

n = int(input())
mt = [list(map(int, input().split())) for _ in range(n)]
sma = 2147000000
big = -2147000000
dx = [-1, 0 , 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

for i in range(n):
    for j in range(n):
        sma = min(board[i][j], sma)
        big = max(board[i][j], big)







