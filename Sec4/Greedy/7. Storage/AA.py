import sys
sys.stdin = open("input.txt", "r")

l = int(input())
box = list(map(int, input().split()))
m = int(input())
#print(box)
for k in range(m):
    box.sort()
    #print("before:----{}------".format(k))
    #print(box)
    box[0] +=1
    box[-1] -=1
    #print("after:============")

print(max(box) - min(box))
