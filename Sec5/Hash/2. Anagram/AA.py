#아나그램 개선코드 질문 확인하기

import sys
#sys.stdin= open("input.txt", "r")

alist = list(input())
blist = list(input())
check = dict()

for a in alist:
    if a in check:
        check[a] +=1
    else:
        check[a] = 1

for b in blist:
    if b in check:
        check[b] -=1
    else:
        print("NO")
        sys.exit(0)

for v in check.values():
    if v != 0:
        print("NO")
        break

#개선 코드
#for x in a:
#    if check.get(a) != 0:
#        print("NO")
#        break

else:
    print("YES")
    
    

