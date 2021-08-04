#이렇게 3일차를 선택하면 6일차(+3)로 가게 되는거면 L을 사용해야 함. 그리고 d를 따로 리턴하지 않기 때문에 L을 d처럼 사

import sys
#sys.stdin = open("input.txt", "r")

def DFS(L, tot):
    global res
    if L > n:
        return
    if L == n:
        if tot > res:
            res = tot

    else:
        if L+T[L] <= n+1:
            DFS(L+T[L], sum+P[L])
        #DFS(L+arr[L][0], tot+arr[L][1])
        DFS(L+1, tot)

n = int(input())
arr = []
res = 0
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a,b))
DFS(0,0)
print(res)

