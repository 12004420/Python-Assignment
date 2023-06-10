
def get_file_type(input_list1,input_list2):
    extension_list = input_list1.split(";")
    dict_extension = {}
    for i in extension_list:
        extension, file_type = i.split(",")
        dict_extension[extension] = file_type

    result_dict = {}
    for j in input_list2:
        file_extension = j.split(".")[-1]
        file_type = dict_extension.get(file_extension, "unknown")
        result_dict[j] = file_type

    return result_dict

input1 =input("Enter a string in the form of extension and type ");
n=int(input("Enter a number of strings "))
input2=[]
for i in range(n):
    x=input("Enter a string with extension ")
    input2.append(x)
result=get_file_type(input1,input2)
print(result)


