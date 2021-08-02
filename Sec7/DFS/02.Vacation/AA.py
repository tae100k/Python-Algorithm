import sys
#sys.stdin = open("input.txt", "r")

def DFS(L, sum):
    #print("L:{}, sum:{}".format(L, sum))
    global res
    if L == n+1:
        if sum > res:
            res = sum
            #print("res:{}".format(res))
            return
    else:
        if L+dlist[L-1] <= n+1:
            #print("go = L:{}".format(L))
            DFS(L+dlist[L-1], sum+mlist[L-1])
        DFS(L+1, sum)

n = int(input())
dlist = []
res = -21730000000
mlist = []
for _ in range(n):
    a,b = map(int, input().split())
    dlist.append(a)
    mlist.append(b)
DFS(1,0)
print(res)
