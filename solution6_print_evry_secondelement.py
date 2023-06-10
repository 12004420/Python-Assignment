
def fun(list1,index_first,index_last):
    list2=[]
    for i in range(index_first,index_last+1,2):
        list2.append(list1[i])
    return list2
    
    
    
n=int(input("Enter number of elements for list "))
list1=[]
for i in range(n):
    num=int(input("Enter an element for list1 "))
    list1.append(num)

index_first=int(input("Enter first_index "))
index_last=int(input("Enter second_index "))
result=fun(list1,index_first,index_last)
print(result)
