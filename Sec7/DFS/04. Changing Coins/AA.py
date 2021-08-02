import sys
#sys.stdin = open("input.txt", "r")

def DFS(L, sum):
    global cnt
    if sum > t:
        return
    if L == k:
        if sum == t:
            cnt += 1
    else:
        for i in range(cnl[L]+1):
            DFS(L+1, sum + (cvl[L] * i))


t = int(input())
k = int(input())
cnt = 0
cvl = []
cnl = []
for _ in range(k):
    a, b = map(int, input().split())
    cvl.append(a)
    cnl.append(b)
DFS(0,0)
print(cnt)
