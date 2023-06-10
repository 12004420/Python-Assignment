def selection_sort(list1):
    m=len(list1)
    for i in range(0,m-1):
        x=list1[i]
        index=i
        for j in range(index+1,m):
            if list1[j]<x :
                x=list1[j]
                index=j
        list1[i],list1[index]=list1[index],list1[i]
    return list1

n=int(input("Enter number of elements "))
list1=[]
for i in range(n):
    x=int(input("Enter a element "))
    list1.append(x)
result=selection_sort(list1)

print("original list " , list1)
print("sorted list",result)

