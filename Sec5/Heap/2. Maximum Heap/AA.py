import sys
sys.stdin = open("input.txt", "r")
import heapq as hq

a = list()

while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            break
        else:
            print(hq.heappop(a) * -1)
    else:
        hq.heappush(a, -n)
