import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
board = [[0] * n for _ in range(n)]

for _ in range(m):
    r, c, v = map(int, input().split())
    board[r-1][c-1] = v

for b in board: 
    print(b)
    
