
def fun(Mainstream,must_watch):
    common = list(set(Mainstream) & set(must_watch))
    not_common =list(set(Mainstream) ^ set(must_watch))
    return common,not_common

n=int(input("Enter number of strings for mainstream "))
Mainstream=[]
for i in range(n):
    x=input("Enter string for mainstream  ")
    Mainstream.append(x)

m=int(input("Enter number of strings for must_watch "))
must_watch=[]
for i in range(m):
    y=input("Enter string for must_watch ")
    must_watch.append(y)

common_elements,not_common_elements=fun(Mainstream,must_watch)
print(common_elements)
print(not_common_elements)


