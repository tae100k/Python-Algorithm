import sys
#sys.stdin = open("input.txt", "r")

exp = list(input())
temp = []
for e in exp:
    if e.isdigit():
        temp.append(int(e))
    else:
        #순서가 바뀌면 '-'나 '/'값이 바뀔 수 있어 값을 임시로 저장
        cur2 = temp.pop()
        cur1 = temp.pop()
        if e == '+':
            temp.append(cur1 + cur2)
        elif e == '-':
            temp.append(cur1 - cur2)
        elif e == '*':
            temp.append(cur1 * cur2)
        else:
            temp.append(cur1 / cur2)

print(temp[0])
