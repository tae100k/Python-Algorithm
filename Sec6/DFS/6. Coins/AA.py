import sys
sys.stdin = open("input.txt", "r")

def DFS(tot, cnt):
    global res
    if res <= cnt:
        return
    if tot > m:
        return
    if tot == m:
        if cnt < res:
            res = cnt
    else:
        for k in range(n):
            DFS(tot + arr[k], cnt+1)       

n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse = True)
m = int(input())
res = 2147000000
DFS(0, 0)
print(res)
