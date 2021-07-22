import sys
from collections import deque

sys.stdin = open("input.txt", "r")

n = int(input())
array = deque(map(int, input().split()))
res= []
out= []

while array:
    if len(array) >=1 and all(out[-1] > array[0], out[-1] > array[-1]):
        break

    #아니면 좌우 비교
    else:
        if array[-1] < array[0]: #왼쪽 사용
            res.append('L')
            out.append(array.popleft())
        else:
            res.append('R')
            out.append(array.pop())
    print("------------------------")
    print("out:{},res:{}, array:{}".format(out, res, array))

print(len(res))
