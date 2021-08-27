#y를 하나 줄이면 0<=y만 보면 됨!
#길이 무조건 있음!(거꾸로 가기 때문에)
#또, 길이 무조건 하나임! 따라서 a길로 갔는데 뒤로 돌아올 확률은 없음!(막다른 길에서 출발할 일이 없음)

import sys
#sys.stdin = open("input.txt", "r")

def DFS(x, y):
    board[x][y] = 0
    if x == 0:
        print(y)
    else:
        if 0<= y-1 and board[x][y-1] == 1:
        #if 0<= y-1 <10 and board[x][y-1] == 1
            DFS(x, y-1)
        elif y+1 < 10 and board[x][y+1] == 1:
            DFS(x, y+1)
        else:
            DFS(x-1, y)

board = [list(map(int, input().split())) for _ in range(10)]
for i in range(10):
    if board[9][i] == 2:
        st = i
        break;
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
DFS(9, st)
