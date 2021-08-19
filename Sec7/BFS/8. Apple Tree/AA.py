from collections import deque
import sys
#sys.stdin = open("input.txt", "r")


m = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = [(list(map(int, input().split()))) for _ in range(m)]
ch = [[0] * m for _ in range(m)]
dq = deque()
tot = board[m//2][m//2]
ch[m//2][m//2] = 1
dq.append((m//2,m//2))
while dq:
    cur = dq.popleft()
    if cur[0] == 0:
        break
    for k in range(4):
        xx = cur[0] + dx[k]
        yy = cur[1] + dy[k]
        if 0<=xx<m and 0<=yy<m and ch[xx][yy] == 0:
            tot += board[xx][yy]
            ch[xx][yy] = 1
            dq.append((xx,yy))
print(tot)
