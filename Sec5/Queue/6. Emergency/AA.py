#4~6번째 줄 한줄로 끝내기
# emer = [(idx, x) for idx, x in enumerate(list(map(int, input().split())))]
# emer = deque(emer)

import sys
#sys.stdin = open("input.txt", "r")
from collections import deque

n, m = map(int, input().split())
emer = list(map(int, input().split()))
temp = []
for idx, x in enumerate(emer):
    temp.append([idx, x])
temp = deque(temp)
cnt = 0
while temp:
    cur = temp.popleft()
    if any(cur[1] < t[1] for t in temp):
        temp.append(cur)
    else:
        cnt +=1
        if cur[0] == m:
            break

print(cnt)
