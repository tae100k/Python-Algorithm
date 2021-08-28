#flag를 사용하면 좋을 듯

import sys
from collections import deque
#sys.stdin = open("input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
m, n = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dis = [[0] * m for _ in range(n)]
dq = deque()
big = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            dq.append((i,j))
while dq:
    cur = dq.popleft()
    for f in range(4):
        xx = cur[0] + dx[f]
        yy = cur[1] + dy[f]
        if 0<= xx<n and 0<= yy < m and board[xx][yy] == 0:
            dis[xx][yy] = dis[cur[0]][cur[1]] + 1
            board[xx][yy] = 1
            dq.append((xx, yy))
flag = 1
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            flag = 0
            sys.exit(0)
if flag == 1:          
    for i in range(n):
        for j in range(m):
            if big < dis[i][j]:
                big = dis[i][j]
    print(big)
else:
    print(-1)
