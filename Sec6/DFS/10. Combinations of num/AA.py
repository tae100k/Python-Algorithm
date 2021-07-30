import sys
#sys.stdin = open("input.txt", "r")

def DFS(prev, L, tot):
    global cnt
    if L == k and tot % m == 0:
        cnt +=1
    else:
        for r in range(prev, n):
            DFS(r+1, L+1, tot + nums[r])


n, k = map(int, input().split())
cnt = 0
nums = list(map(int, input().split()))
m = int(input())
DFS(0, 0, 0)
print(cnt)
