
def fun(firstlist,key):
    sorted_list =sorted(firstlist,key= lambda x:x[key])
    return sorted_list
    

firstlist=[]

n= int(input("Enter number of list "))
n1=int(input("Enter values for dictionary"))
for i in range(n):
    dict2={}
    for j in range(n1):
        key=input("Enter key")
        value=input("Enter value")
        dict2[key]=value
    firstlist.append(dict2)
print(firstlist)

key=input("Enter a string on the base of which you want to sort");
sorted_list=fun(firstlist,key)

print("after sorted according to the given strinf:->",sorted_list)
    