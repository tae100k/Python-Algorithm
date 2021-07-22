import sys
sys.stdin = open("input.txt", "r")

#input받기
n, m = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort(reverse = True)

cnt = 0
i = 0

while i < len(weights):
    #print("weights[i]:{}, weights[-1]:{}".format(weights[i], weights[-1]))
    if weights[i] + weights[-1] <= m:
        weights.pop()
    i +=1
    cnt +=1
    #print("weights:{}, cnt:{}".format(weights, cnt))

print(cnt)


#--------------------------
# while i < len(wegihts)하지 않고
# while p:
#    if len(p) == 1:
#            cnt += 1
#            break        
