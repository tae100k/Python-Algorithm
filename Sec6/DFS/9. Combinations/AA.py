#꼭 다시 풀어보기
# 특히 파스칼 삼각형 부분 스스로 쓸 수 있도록 하기!

import sys
sys.stdin = open("input.txt", "r")

def DFS(v, tot):
    if v == n and tot == f:
        for x in res:
            print(x, end = '')
        sys.exit(1)
    else:
        for k in range(1, n+1):
            if ch[k] == 0:
                ch[k]= 1
                res[v] = k
                DFS(v+1, tot+(bi[v] * res[v]))
                ch[k]= 0

n, f = map(int, input().split())
res = [0] * n
ch = [0] * (n+1)
bi = [1] * n
for i in range(1, n):
    bi[i] = bi[i-1] * (n-i) / i
    
DFS(0, 0) 
