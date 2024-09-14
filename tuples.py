#   tuple: ordered, imutable, allows duplicate elements

mytuple = ("max", 28, True)
# mytuple = tuple('Max', 28, True)
# mytuple = ('Max',)
# print(type(mytuple))
print(mytuple)

item = mytuple[0]
print(item)

# This is not possible, cause Tuple is unmutable 
# mytuple[0] = "Tim"

for i in mytuple:
    print(i)
    continue

# ********************************

if 'Max' in mytuple:
    print('yes')
else:
    print('no')

# ********************************
mytuple = ('a', 'p', 'p', 'l', 'e')
print(mytuple.count('p')) 
print(mytuple.index('p'))

# ********************************
my_list = list(mytuple)
print(my_list)
my_tuple2 = tuple(my_list)
print(my_tuple2)

# *********************************
a = (1, 2, 3, 4, 5, 6, 7)
b = a[2:5]
c = a[::2]
print(b)
print(c)

# *********************************
my_tuple = "Max", 28, "Boston"

name, age, city = my_tuple
print(name)
print(age)
print(city)

# ********************************
my_tuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = my_tuple
print(i2)

#  ******************************
import sys

my_list = [0, 1, 2, "hello", True]
my_tuple= (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

# ******************************

import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))

# **********************************
