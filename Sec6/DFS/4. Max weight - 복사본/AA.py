#시간을 단축하는 방법
#가장 큰 값을 구해야하기 때문에, 남은 걸 다 더해봤자 현재 값보다 작다면 그 노드는 가지 않도록 if컷

import sys
#sys.stdin = open("input.txt", "r")

def DFS(v, tot, ntot):
    global res
    if tot + (sum(arr) - ntot) < res:
        return
    if c < tot:
        return
    if v == n:
        if res < tot:
            res = tot
    else:
        DFS(v+1, tot+arr[v], ntot + arr[v])
        DFS(v+1, tot, ntot + arr[v])

c, n = map(int, input().split())
arr = [int(input()) for _ in range(n)]
res = 0
DFS(0, 0, 0)
print(res)
