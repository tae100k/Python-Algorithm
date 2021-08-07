import sys
import itertools as it
sys.stdin = open("input.txt", "r")

n, f = map(int, input().split())
bi = [1] * n
for i in range(1, n):
    bi[i] = bi[i-1] * (n -i) //i

arr = list(range(1, n+1))
for temp in it.permutations(arr):
    sum = 0
    for idx, x in enumerate(temp):
        sum += x * bi[idx]
    if sum == f:
        for t in temp:
            print(t, end = ' ')
        break
