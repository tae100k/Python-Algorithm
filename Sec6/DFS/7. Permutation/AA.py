# 이렇게 해도 개수는 똑같은데 이렇게 하지 않고 res를 만드는 이유!
# 해당 식은 for c in range(len(ch))를 하기 때문에 무조건 작은 숫자부터 나온다
# 따라서 그 순서쌍도 중요한 것들은 이렇게 ch용 리스트와 res리스트 두개를 사용!
#참고로 아래거는 답이 아님!

import sys
sys.stdin = open("input.txt", "r")

def DFS(v):
    global cnt
    if v == m:
        for c in range(len(ch)):
            if ch[c] == 1:
                print(c+1, end = ' ')
        cnt +=1
        print()
    else:
        for k in range(n):
            if ch[k] == 0:
                ch[k] = 1
                DFS(v+1)
                ch[k] = 0
                

n, m = map(int, input().split())
cnt = 0
ch = [0] * n
DFS(0)
print(cnt)
