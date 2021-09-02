#**중요**
#tmp.append(arr[p1:mid+1]) 이렇게 하면 tmp라는 리스트에 새로은 리스트를 넣어 2차원 리스트가 됩니다.
#tmp=tmp+arr[p1:mid+1] 이렇게 해야 일차원리스트 + 일차원리스트=일차원리스트가 됩니다.

def Dsort(lt, rt):
    if lt < rt:
        mid = (lt + rt)//2
        Dsort(lt, mid)
        Dsort(mid +1, rt)
        p1 = lt
        p2 = mid +1
        temp = []
        while p1 <= mid and p2 <= rt:
            if arr[p1] < arr[p2] :
                temp.append(arr[p1])
                p1+=1
            else:
                temp.append(arr[p2])
                p2 +=1
        if p1 <= mid:
            temp = temp + arr[p1:mid+1]
        if p2 <= rt:
            temp = temp + arr[p2:rt+1]
        for i in range(len(temp)):
            arr[lt+i] = temp[i]

arr=[23, 11, 45, 36, 15, 67, 33, 21]
print("Before:", end = ' ')
print(arr)
Dsort(0,7)
print("After:", end = ' ')
print(arr)
