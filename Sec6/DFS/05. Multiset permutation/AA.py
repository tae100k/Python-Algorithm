#inpt = sys.stdin.readline하면 더 빠르게 파일을 읽음


import sys
#sys.stdin = open("input.txt", "r")

def DFS(v):
    global cnt
    if v == m:
         for c in ch:
             print(c, end = '')
         print()
         cnt +=1
    else:
        for k in range(1, n+1):
            ch[v] = k
            DFS(v+1)

n, m = map(int, input().split())
ch = [0] * m
cnt = 0
DFS(0)
print(cnt)
