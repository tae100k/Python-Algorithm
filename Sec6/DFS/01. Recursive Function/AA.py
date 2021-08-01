import sys
#sys.stdin = open("input.txt", "r")

def DFS(n):
    if n == 0:
        return
    else:
        DFS(n//2)
        answer.append(n%2)
    

n = int(input())
answer = []
DFS(n)
temp = ''
for a in answer:
    temp += str(a)
print(temp)

#이렇게 하지 말고 그냥 'print(x%2, end = '')하면 나중에 answer처리 안 해도 됨
#n진수는 n == 0일때 종료
