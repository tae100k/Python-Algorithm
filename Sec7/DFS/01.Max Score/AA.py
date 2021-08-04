import sys
sys.stdin = open("input.txt","r")

def DFS(L, tot, tim):
    #print("L:{}, tot:{}, tim:{}".format(L, tot, tim))
    global res
    if tim > m:
        return
    if L == n:
        if tot > res:
            res = tot
    else: 
        DFS(L+1, tot + arr[L][0], tim + arr[L][1])
        DFS(L+1, tot, tim)
n, m = map(int, input().split())
arr = []
res = 0
for _ in range(n):
    a,b = map(int, input().split())
    arr.append((a,b))
DFS(0, 0, 0)
print(res)

