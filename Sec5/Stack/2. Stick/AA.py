import sys
sys.stdin = open("input.txt", "r")
stick = input()
cnt = 0
temp =[]

for i,s in enumerate(stick):
    #'('나오면 무조건 추가
    if s == '(':
        temp.append(s)
        
    else:
        #절단인 경우
        if stick[i-1] == '(':
            temp.pop()
            cnt += len(temp)

        #길이가 짧아 아웃    
        else:
            temp.pop()
            cnt +=1
            
        
print(cnt)
