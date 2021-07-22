#답이 다르게 나오면 , 일단 내가 입출력 예시를 보면서 따라가보고, 그래도 틀린 곳을 못찾겠으면
#그 때 PRINT이용하기
#dq = dq(esse)를 for 문 안에서 계속 해주기
# x != dq.popleft() -> if/else 안 나누고 할 수 있음

import sys
sys.stdin = open("input.txt", "r")
from collections import deque

esse = input()
n = int(input())

for k in range(n):
    cur = deque(input())
    temp = deque(esse)
    while cur:
        if cur[0] in temp:
            #순서 체크
            if cur[0] == temp[0]:
                temp.popleft()
            else:
                print("#{} NO".format(k+1))
                break
        cur.popleft()
    else:
    # 전부 수강했는 지 체크
        if len(temp) != 0:
            print("#{} NO".format(k+1))
        else:
             print("#{} YES".format(k+1))
