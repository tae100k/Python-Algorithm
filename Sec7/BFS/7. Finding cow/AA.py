import sys
from collections import deque
sys.stdin = open("input.txt", "r")

s, e = map(int, input().split())
dq = deque([s])
dis = [0] * 10001
ch = [0] * 10001
while True:
    cur = dq.popleft()
    if cur == e:
        break
    else:
        for k in [1, -1, 5]:
            if 0 <= k+cur <= 10000:
                if ch[k+cur] == 0:
                    ch[k+cur] = 1
                    dq.append(k+cur)
                    dis[k+cur] = dis[cur] + 1
                        
            
print(dis[e])
            
            

