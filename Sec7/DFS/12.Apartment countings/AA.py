# 문제에서 띄어쓰기가 없는데 split()을 했음 -> 문제를 제대로 읽지 않음
# 문제를 제대로 읽지 않음 오름차순이라는 말을 못챙기함


import sys
sys.stdin = open("input.txt", "r")

def DFS(x,y):
    global apt
    apt +=1
    board[x][y] = 0
    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if 0<= xx < n and 0<= yy < n and board[xx][yy] == 1:
            DFS(xx,yy)

n = int(input())
board = [list(map(int, input())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answers = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            apt = 0
            DFS(i,j)
            answers.append(apt)

print(len(answers))
answers = sorted(answers)
for answer in answers:
    print(answer)
