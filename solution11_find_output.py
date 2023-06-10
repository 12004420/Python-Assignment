def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)
f(2)   # it will make new list and give output as a list output:-> [0,1]
f(3,[3,2,1]) # it will not make a new list and append in this list only output:-> [3, 2, 1, 0, 1, 4]
f(3) # it will not make a new list because when first time our program run then it wil create list only 
     # once after that it will just append