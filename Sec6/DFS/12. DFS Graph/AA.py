#만약 문제에서 path까지 구하라고 요구한다면
# board[c][k] = 0
# path.append(k) <= 이거 
# ch[c] = 1
# DFS(k)
# path.pop() <= 이거 추
# board[c][k] = 1

import sys
#sys.stdin = open("input.txt", "r")

def DFS(c):
    global cnt
    if c+1 == n:
        cnt += 1
    else:
        for k in range(n):
            if board[c][k] == 1 and ch[k] == 0:
                #board[c][k] = 0 #어차피ch가 중복 방지하기 때문에 이거 필요 없음
                ch[c] = 1
                DFS(k)
                board[c][k] = 1 #역시 필요 없
                ch[c] = 0
                

n, m = map(int, input().split())
cnt = 0
res = []
ch = [0] * n
board = [[0] * n for _ in range(n)]
for _ in range(m):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

DFS(0)
print(cnt)
