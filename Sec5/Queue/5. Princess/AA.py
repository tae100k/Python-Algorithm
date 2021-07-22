#while문 안에 또 다른 for문으로 dq하는 방법도 있음!
#while s: 는 s가 빈리스트일 때 break

import sys
#sys.stdin = open("input.txt", "r")
from collections import deque

n, k = map(int, input().split())
s = [ k for k in range(1, n+1)]
s = deque(s)

i = 1
while s:
    if len(s)== 1:
        break
    if i == k:
        s.popleft()
        i = 1
    else:
        s.append(s.popleft())
        i+=1

print(s[0])
