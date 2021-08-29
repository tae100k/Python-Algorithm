import sys
sys.stdin = open("input.txt", "r")


def DFS(L, p):
    if 

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
pz = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            pz += 1

arr = [0] * m
DFS(0)
