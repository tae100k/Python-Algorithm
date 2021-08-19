from collections import deque
import sys
sys.stdin = open("input.txt", "r")

board = [ list(map(int, input().split())) for _ in range(7)]
dq = deque()
dq.append((0,0))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board[0][0] = 1
dis = [[0] * 7 for _ in range(7)]
ch = [[0] * 7 for _ in range(7)]

while dq:
    cur = dq.popleft()
    if cur[0] == 6 and cur[1] == 6:
        break
    for k in range(4):
        xx = cur[0] + dx[k]
        yy = cur[1] + dy[k]
        if 0<=xx<7 and 0<=yy<7 and board[xx][yy] == 0 and ch[xx][yy] == 0:
            dis[xx][yy] = dis[cur[0]][cur[1]] + 1
            dq.append((xx, yy))
            ch[xx][yy] = 1

if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])
