#DFS문의 else에서는 크게 if문으로 해당 레벨에서 선택함 안함이 있고 for문으로 하나씩 넣어보기가 있음
#안 넣어보는 경우의수가 해당이 되는 지 안되는지를 생각하면서 둘 중에 고르기!
#DFS가 어디가 틀렸는지 감도 안 올 때는 res만들어서 넣어보고 그 리스트를 출력하기!
#이중 if가 나을 때도 있고 (else에 걸리지 않고 return하게) if a and b 가 나을 때도 있
import sys
#sys.stdin = open("input.txt", "r")

def DFS(L, tot):
    global cnt
    if tot > t:
        return
    if L == k:
        if tot == t:
            cnt +=1
    else:
        for p in range(arr[L][1]+1):
            #temp.append(arr[L][0]*p)
            DFS(L+1, tot+arr[L][0] * p)
            #temp.pop()
    

t = int(input())
k = int(input())
arr = []
#temp = []
for _ in range(k):
    p, n = map(int, input().split())
    arr.append([p,n])
cnt = 0
DFS(0, 0)
print(cnt)
