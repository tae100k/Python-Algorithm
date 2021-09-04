import sys
sys.stdin = open("input.txt","r")

def DFS(L):
    if dy[L] > 0:
        return dy[L]
    if L == 1:
        return 1
    elif L == 2:
        return 2
    else:
        dy[L] = DFS(L-1) + DFS(L-2)
        return dy[L]

n = int(input())
dy = [0] * (n+1)
print(DFS(n))
