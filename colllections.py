# collections: Couter, namedtuple, OrderedDict,defaultdict, deque
from collections import Counter

a = 'aaaabbbbcccccc'
my_counter = Counter(a)
print(my_counter)
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1))
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))

# **************************************

from collections import namedtuple

Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

# ************************************
from collections import OrderedDict

# Creating an OrderedDict
ordered_dict = OrderedDict()
ordered_dict['apple'] = 1
ordered_dict['banana'] = 2
ordered_dict['cherry'] = 3

print(ordered_dict)  # Output: OrderedDict([('apple', 1), ('banana', 2), ('cherry', 3)])

# Moving 'banana' to the end
ordered_dict.move_to_end('banana')
print(ordered_dict)  # Output: OrderedDict([('apple', 1), ('cherry', 3), ('banana', 2)])

# ********************************

from collections import defaultdict

d = defaultdict(int) 
   
L = [1, 2, 3, 4, 2, 4, 1, 2] 
   
# Iterate through the list 
# for keeping the count 
for i in L: 
       
    # The default value is 0 
    # so there is no need to  
    # enter the key first 
    d[i] += 1
       
print(d) 

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a'])

# ***********************************

from collections import deque

d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)
d.pop()
print(d)
d.append(1)
d.appendleft(2)
d.rotate(1)
print(d)