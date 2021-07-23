import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
n = list(str(n))
res = []
cnt = 0 
for x in list(n):
    #작으면 지우고
    while res:
        if res[-1] < x and cnt < m:   #cnt를 따로 만들지 않고 m-=1를 했어도 좋았을 듯
            res.pop()
            cnt+=1
        else:
            break
    #아니면 append
    res.append(x)

while cnt < m:
    cnt +=1
    res.pop()

print(''.join(res))
    
