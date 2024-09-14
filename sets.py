# Sets: unordered, mutable, no duplicates

myset = {1,2,3}
print(myset)
myset1 = set("Hello")
print(myset1)
print(myset.pop())

# ****************************

if 4 in myset:
    print("yes")

# ***************************

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

# ****************************

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff1 = setA.difference(setB)
print(diff1)
diff2 = setB.difference(setA)
print(diff2)
diff3 = setB.symmetric_difference(setA)
print(diff3)
setA.update(setB)
print(setA)
setB.difference_update(setA)
print(setB)

# **************************

set1 = {1, 2, 3, 4, 5, 6}
# set2 = set1
set2 = set1.copy()
set2.add(7)
print(set2)
print(set1)

# *****  Frozen set ******

a = frozenset([1, 2, 3, 4])
# error
# a.remove / a.add
print(a)

