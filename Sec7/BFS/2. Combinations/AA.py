#왜 어떨때는 from a import b 이고,
#어떨때는 import b인 지 궁금

import sys
sys.stdin = open("input.txt", "r")
import itertools as it

n, k = map(int, input().split())
arr = list(map(int, input().split()))
m = int(input())
cnt = 0

for temp in it.combinations(arr,k):
    tot = sum(temp)
    if tot % m == 0:
        cnt +=1

print(cnt)
