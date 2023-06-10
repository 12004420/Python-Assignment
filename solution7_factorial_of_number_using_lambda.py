
factorial = lambda x : 1 if x==0 else x*factorial(x-1)

num=int(input("Write a number"))
result=factorial(num)
print(result)