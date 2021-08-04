#주어진! 문제를! 제대로! 읽을 것!
# 문제에서 단, 세 사람의 총액은 서로 달라야 합니다 라고 했음

import sys
sys.stdin = open("input.txt", "r")

def DFS(L):
    global res
    if L == n:
        if max(ppl) - min(ppl) < res:
            k = set(ppl)
            if len(k) == 3:
                res = max(ppl) - min(ppl)
    else:
        for k in range(3):
            ppl[k] += coins[L]
            DFS(L+1)
            ppl[k] -= coins[L]
    

n = int(input())
coins = []
for _ in range(n):
    coins.append(int(input()))
ppl = [0] * 3
res = max(coins)
DFS(0)
print(res)
