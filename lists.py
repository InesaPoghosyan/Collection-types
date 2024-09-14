mylist = ['banana', 'cherry', 'apple']
print(mylist)

# item = mylist[-1]
# print(item)

for i in mylist:
    print(i)


# if "banana" in mylist:
#     print("yes")
# else:
#     print("no")

print(len(mylist))

# mylist.append("lemon")
# print(mylist)

mylist.insert(1, "blueberry")
print(mylist)

# item = mylist.pop()
# print(item)
# print(mylist)

item = mylist.remove("cherry")
print(mylist)

#  **************************************
#  Lists: ordered, mutable, allows duplicate elements

numbers = [1, 2, 0, 53, 5, 6]
print(sorted(numbers))  

# a = numbers[1:5]
# b = numbers[:5]
# c = numbers[1:]
# print(a)
# print(b)
# print(c)

a = numbers[::-1]
print(a)

# *************************************

list_org = ['banana', 'cherry', 'apple']

# list_cpy = list_org 
# list_cpy.append('lemon')

list_cpy = list_org.copy()
# list_cpy = list_org[:]
# list_cpy = list(list_org)
list_cpy.append('lemon')

print(list_cpy)
print(list_org)

# ***************************************

numberss = [1, 2, 3, 4,5, 6]
b = [i*i for i in numberss]

print(numberss)
print(b)