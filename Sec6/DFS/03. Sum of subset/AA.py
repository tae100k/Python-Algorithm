#ntot을 만들지 않고 그냥 if sum>tot//2:만 해도 됨! 어차피 같은 말이기 때문에 변수 절약
#이 코드는 우연히 돌아간 것 같고, 원래대로 라면 v == n 이여야 함! v가 DFS(v+1)로 들어오기 때문
import sys
sys.stdin = open("input.txt", "r")

def DFS(v, tot, ntot):
    if tot + sum(arr) - ntot < sum(arr) /2:
        #print("too big already! check:{}, v:{}, tot:{}, ntot:{}".format(check, v, tot, ntot))
        return
    if v+1 == n:
        #print("check:{}, v:{}, tot:{}, ntot:{}".format(check, v, tot, ntot))
        if tot == sum(arr) / 2:
            print("YES")
            sys.exit(0)
    else:
        check[v] = 1
        DFS(v+1, tot + arr[v], ntot + arr[v])
        check[v] = 0
        DFS(v+1, tot, ntot + arr[v])

n = int(input())
check = [0] * (n)
arr = list(map(int, input().split()))
DFS(0, 0, 0)
print("NO")
