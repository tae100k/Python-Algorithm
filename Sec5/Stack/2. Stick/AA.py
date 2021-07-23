import sys
sys.stdin = open("input.txt", "r")

n = int(input())
ath = [list(map(int, input().split())) for _ in range(n)]
res = []

for a in ath:
    if any(t[0] > a[0] and t[1] > a[1] for t in ath):
        continue
    else:
        res.append(a)

print(len(res))
