Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple : tuple is python's immutable and ordered data collection.
>>> #immutable : which cannot be changed
>>> x = (12,14,18,98,0,-90)
>>> type(x)
<class 'tuple'>
>>> x[0]
12
>>> x[-1]
-90
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
>>> len(x)
6
>>> sum(x)
52
min(x)
-90
max(x)
98
x
(12, 14, 18, 98, 0, -90)
x.count(12)
1
x
(12, 14, 18, 98, 0, -90)
x.index(12)
0

#List remaining properties
x = [1,2,3,4,5]
x*2
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
x
[1, 2, 3, 4, 5]
y = [6,7,8,9,10]
x
[1, 2, 3, 4, 5]
y
[6, 7, 8, 9, 10]
x.extend(y)
x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = [1,2,3,4,5]
y = x
#shallow copy
del x[0]
x
[2, 3, 4, 5]
y
[2, 3, 4, 5]
#deep copy
x
[2, 3, 4, 5]
from copy import deepcopy
y = deepcopy(x)
x
[2, 3, 4, 5]
y
[2, 3, 4, 5]
del x[0]
x
[3, 4, 5]
y
[2, 3, 4, 5]

x
[3, 4, 5]
x = [10,5,67,8,3,4,90,-9]
x.sort()
x
[-9, 3, 4, 5, 8, 10, 67, 90]
x.sort(reverse=True)
x
[90, 67, 10, 8, 5, 4, 3, -9]
x = [1,2,3,4,5]
y = [1,4,9,16,25]
res = list(zip(x,y))
res
[(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

#dictionary :
#it is python's unordered and mutable data collection
#unordered - no indexing
#mutable- changable
x = {"roll":101,"name":"amit","class":1}
x.keys()
dict_keys(['roll', 'name', 'class'])
x.values()
dict_values([101, 'amit', 1])
x.items()
dict_items([('roll', 101), ('name', 'amit'), ('class', 1)])
x
{'roll': 101, 'name': 'amit', 'class': 1}
x["contact"]=9876543210
x
{'roll': 101, 'name': 'amit', 'class': 1, 'contact': 9876543210}
x["roll"]=102
x
{'roll': 102, 'name': 'amit', 'class': 1, 'contact': 9876543210}
x.popitem()#it will remove last key value pair
('contact', 9876543210)
x
{'roll': 102, 'name': 'amit', 'class': 1}
del x['name']
x
{'roll': 102, 'class': 1}
x['roll']
102
len(x)
2
#more data
x = [{"id":101,"name":"amit"},]


x = [{"id":101,"name":"amit"},
     {"id":102,"name":"ravi"},
     {"id":103,"name":"tanya"}]
x
[{'id': 101, 'name': 'amit'}, {'id': 102, 'name': 'ravi'}, {'id': 103, 'name': 'tanya'}]

for row in x:
    print(row["id"],row["name"])

101 amit
102 ravi
103 tanya
\
