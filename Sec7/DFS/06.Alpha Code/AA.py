import sys
sys.stdin = open("input.txt", "r")

def DFS(i, prev):
    global cnt
    if i == size:
        print(str)
        cnt +=1
    else:
        if code[i] in [0,1,2]:
            str.append(chr(code[i]))
            DFS(i+1)
            str.pop()
            
            DFS(i+1, code[i])
        else:
            str.append(chr(code[i]))
            DFS(i+1)
            

code= int(input())
size = len(code)
cnt = 0
str = []
DFS()
