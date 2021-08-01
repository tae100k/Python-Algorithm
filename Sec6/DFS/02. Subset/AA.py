import sys
#sys.stdin = open("input.txt", "r")

def DFS(k):
    if k == n:
        for c in range(len(check)):
            if check[c] == 1:
                print(c+1, end = '')
        print()
    else:
        check[k] = 1
        DFS(k+1)
        check[k] = 0
        DFS(k+1)
        
    

n = int(input())
check = [0 for _ in range(n)]
DFS(0)

