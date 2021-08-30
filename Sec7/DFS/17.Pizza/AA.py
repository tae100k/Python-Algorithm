#조합을 만들어두고 사용하지 않음

import sys
#sys.stdin = open("input.txt", "r")

def DFS(L, s):
    global res
    if L == m:
        one = 0
        for h in hs:
            hx = h[0]
            hy = h[1]
            sma = 2147000000
            for c in comb:
                px = pz[c][0]
                py = pz[c][1]
                dis = abs(hx - px) + abs(hy-py)
                if sma > dis:
                    sma = dis                
            one += sma
        if one < res:
            res = one
    else:
        for k in range(s, len(pz)):
            comb[L] = k
            DFS(L+1, k+1)
            

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
pz = []
hs = []
sma = 2147000000
res = 2147000000
comb = [0] * m

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            hs.append((i,j))
        elif board[i][j] == 2:
            pz.append((i,j))

DFS(0,0)
print(res)
