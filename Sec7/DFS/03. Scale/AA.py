import sys
#sys.stdin = open("input.txt", "r")

def DFS(L, sum):
    global poss
    if L == k:
        if 0<sum<=big:
            poss.add(sum)
    else:
        DFS(L+1, sum+arr[L])
        DFS(L+1, sum-arr[L])
        DFS(L+1, sum)

k = int(input())
poss = set()
arr = list(map(int, input().split()))
big = sum(arr)
DFS(0, 0)
print(big - len(poss))
