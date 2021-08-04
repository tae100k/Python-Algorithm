#L=0은 arr[0]을 더한다, 뺀다, 아무것도 안한다 이렇게 3개씩하고 다 하면 L+1

import sys
#sys.stdin = open("input.txt", "r")

def DFS(L, tot):
    global cnt
    if L == k:
        if 0<tot and temp[tot] == 0:
            cnt +=1
            temp[tot] = 1
#여기서 temp를 다시 안 쓰기 위해서
#   res = set()
#       if 0 < sum <= s:
#           res.add(sum)

    else:
        DFS(L+1, tot + arr[L])
        DFS(L+1, tot - arr[L])
        DFS(L+1, tot)
    

k = int(input())
cnt = 0
arr = list(map(int, input().split()))
s = sum(arr)
temp = [0] * (s +1)
DFS(0,0)
print(s-cnt)

