import sys
from collections import deque
#sys.stdin = open("input.txt", "r")


n = int(input())
ch = [[0] * n for _ in range(n)]
board = [list(map(int, input().split())) for _ in range(n)]
dq = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
big = 0
cnt = 0
answer = []
for i in range(n):
    for j in range(n):
       if big < board[i][j]:
           big = board[i][j]

for h in range(0, big+1):
    for i in range(n):
        for j in range(n):
            if board[i][j] >= h and ch[i][j] == 0:
                dq.append((i,j))
                ch[i][j] = 1
                cnt +=1
                while dq:
                    cur = dq.popleft()
                    for f in range(4):
                            xx = cur[0] + dx[f]
                            yy = cur[1] + dy[f]
                            if 0<=xx<n and 0<=yy<n and ch[xx][yy] == 0 and board[xx][yy] >= h:
                                dq.append((xx,yy))
                                ch[xx][yy] = 1
                
    answer.append(cnt)
    cnt = 0
    ch = [[0] * n for _ in range(n)]
print(max(answer))
                    
                
