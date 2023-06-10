
from functools import reduce

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
print(A0)       # output -> {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}  it will return a dictionary 
                # and zip function will combine the keys values 

A1 = range(10)
print(A1)       # it will return range(0,10)

A2 = sorted([i for i in A1 if i in A0])
print(A2)     # it will return an empty list because in nothing is present in A1 it is just a range 

A3 = sorted([A0[s] for s in A0])
print(A3)    # output -> [1, 2, 3, 4, 5]  it will return a list A0[0] means value present in A0[0].....A0[s];

A4 = [i for i in A1 if i in A3]
print(A4)    #output -> [1, 2, 3, 4, 5] it will return a list if i is present in A3 then print i

A5 = {i:i*i for i in A1}
print(A5)     #  output -> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81} it will return a
              # dictionary in which value we get by multiply each and evry elemnt present in A1

A6 = [[i,i*i] for i in A1]
print(A6)  # output -> [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]] it will return a list 
           # and then multiply every element of A1

A7 = reduce(lambda x,y: x+y, [10,23, -45, 33])
print(A7)    # output -> 21 because this x+y will add everything present in this function and reduce funtion is for loop

A8 = map(lambda x: x*2, [1,2,3,4])
print(A8)     #output:-> <map object at 0x0000025F8A477640>
print(list(A8))        #output:-> [2, 4, 6, 8]

A9 = filter(lambda x: len(x) >3, ["I", "want", "to", "learn", "python"])
print(A9)       #output:-> <filter object at 0x0000025F8A477580>
print(list(A9))   #output:-> ['want', 'learn', 'python'] filter will select the elements which 
                  # has length greater than 3