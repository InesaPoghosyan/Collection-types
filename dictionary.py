# Dictionary: Key-Value pairs, Unordered, Mutable

mydict = {"name": "Max", "age":28, "city": "New York"}
print(mydict)

mydict2 = dict(name = "Mary", age = 27, city = "Bostom", mail = "Ines@gmail.com")
print(mydict2)

value = mydict["name"]
print(value)

try:
    print(mydict["sname"])
except:
    print("Error")

# **********************************

for key in mydict.keys():
    print(key) 
for value in mydict.values():
    print(value)

# *******************************

mydict_cpy = mydict
mydict_cpy = mydict.copy()
print(mydict_cpy)
mydict_cpy["email"] = "mari@gmail.com"
print(mydict)

# ******************************
# Merge 2 dicts

mydict.update(mydict2)
print(mydict)
