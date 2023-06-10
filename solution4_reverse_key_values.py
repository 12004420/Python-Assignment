
def reverse_key_value(original_dict):
    x={value:key for key,value in original_dict.items()}
    return x

original_dict={}
n=int(input("Enter the number of inputs for the dictionary "))
for i in range(n):
    key=input("Enter key for this")
    value=input("Enter value for this")
    original_dict[key]=value
print("Original dictionary :->")
print (original_dict)

result=reverse_key_value(original_dict)
print(" dictionary after reverse key values :->")
print ( result)
