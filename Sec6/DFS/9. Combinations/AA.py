#어차피 prev부터 for문이 돌기 때문에 ch리스트가 필요하지 않음
#단 for문에서는 if ch[k] == 0을 통해서 한단계식 상승하던 게 없기 때문에
#DFS(k+1, L+1)해야 함

import sys
#sys.stdin = open("input.txt", "r")

def DFS(prev, L):
    global cnt
    if L == m:
        for r in res:
            print(r, end = ' ')
        print()
        cnt +=1
    else:
        for k in range(prev, n):
            #if ch[k] == 0:
                #ch[k] = 1
            res[L] = k+1
            DFS(k+1, L+1)
                #ch[k] = 0
                

n, m = map(int, input().split())
cnt = 0
res = [0] * m
#ch = [0] * n
DFS(0, 0)
print(cnt)
