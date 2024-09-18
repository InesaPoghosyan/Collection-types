# Strings: ordered, immutable, text representation

my_string = "Hello World"
print(my_string)

my_str = "Hello World"
char = my_string[0]
#  error  my_string[0] = 'l'
substring = my_string[1:7]
print(substring)
print(char)

#  *********************************

greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)

# *******************************

greet = "Hello"
for i in greeting:
    print(i)

if 'e' in greeting:
    print('yes')
else:
    print('no')

# ******************************* 

my_strr = '       Hello World  '
my_strr = my_strr.strip()
print(my_strr)

# ******************************

my_word = 'Hello World'
print(my_word.lower())
print(my_word.upper())
print(my_word.startswith('J'))
print(my_word.endswith('d'))
print(my_word.count('o'))
print(my_word.replace('World', 'Universe'))

# ***************************************

my_string = 'how,are,you,doing'
my_list = my_string.split(",")
print(my_list)
new_string = ''.join(my_list)
print(new_string)

# **************************************

my_list = ['a'] * 6
print(my_list)

# bad
string = ''
for i in my_list:
    string += i

print(string)

# good
my_string = ''.join(my_list)
print(my_string)

# *************************************
# %, .format(), f_String

var = 'Tom'
strr = "the variable is %s" %var
num = 123
strrr = "the variable is %d" %num
print(strrr)
print(strr)