import sys
from collections import deque
#sys.stdin = open("input.txt", "r")

n = int(input())
board = [ list(map(int, input().split())) for _ in range(n)]
dq = deque()
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1,1,0, -1, -1, -1]
answer = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            dq.append((i,j))
            board[i][j] = 0
            cnt = 1
            while dq:
                cur = dq.popleft()
                for k in range(8):
                    xx = cur[0] + dx[k]
                    yy = cur[1] + dy[k]
                    if 0<=xx<n and 0<=yy<n and board[xx][yy] == 1:
                        dq.append((xx,yy))
                        board[xx][yy] = 0
                        
print(len(answer))
                
