import sys
sys.stdin = open("input.txt", "r")

def DFS(x, y):
    global cnt
    if x == endx and y == endy:
        cnt +=1
    else:
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0<= xx<n and 0<= yy <n and board[x][y] < board[xx][yy]:
                DFS(xx, yy)
        

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
st = 2147000000
end = -2147000000
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
for i in range(n):
    for j in range(n):
        if st > board[i][j]:
            st = board[i][j]
            stx = i
            sty = j
        if end < board[i][j]:
            end = board[i][j]
            endx = i
            endy = j
DFS(stx,sty)
print(cnt)
            
