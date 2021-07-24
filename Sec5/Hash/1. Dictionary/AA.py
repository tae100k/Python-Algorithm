import sys
#sys.stdin = open("input.txt", "r")

words = dict()
n = int(input())
for _ in range(n):
    words[input()] = 1

for _ in range(n-1):
    words[input()] += 1

for k,v in words.items():
    if v == 1:
        print(k)
        break

    

