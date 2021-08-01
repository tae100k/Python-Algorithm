#개선사항:
#elif v == n:
#        if tot == f:
#로 하지말고 그냥 if v == n and tot == f로 처리할 

import sys
#sys.stdin = open("input.txt","r")

def DFS(tot, v):
    if tot > f:
        return
    elif v == n:
        if tot == f:
            for r in res:
                print(r, end = ' ')
            sys.exit(0)
    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                res[v] = i+1
                DFS(tot + (i+1) * fr[v], v+1)
                ch[i] = 0

n, f = map(int, input().split())
fr = [1] * n
ch = [0] * n
res = [0] * n
for k in range(1, n):
    fr[k] = fr[k-1] * (n-k)//k
DFS(0, 0)
