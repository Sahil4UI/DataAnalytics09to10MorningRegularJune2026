Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
x = []
type(x)
<class 'list'>
#List is Python's mutable and ordered data collection
#mutable -add,remove,update
#ordered - indexing
x = [10,65,8,5,34,7]
x[0]
10
x[1]
65
x[-1]
7
x
[10, 65, 8, 5, 34, 7]
x[0:5]
[10, 65, 8, 5, 34]
#Nested indexing
x = [1,2,3,[4,5,[6,7,8,[9,10,11]]]]
x[3][2][3][1]
10
#methods of List
x = [1,2,3]
x.append(10)#it will add the value at last
x
[1, 2, 3, 10]
x.insert(90,0)
x
[1, 2, 3, 10, 0]
x.insert(1,-9)
x
[1, -9, 2, 3, 10, 0]
x[0]=8#update
x
[8, -9, 2, 3, 10, 0]
x.pop()#it will remove last value
0
>>> x
[8, -9, 2, 3, 10]
>>> x.pop(1)
-9
>>> x
[8, 2, 3, 10]
>>> x.remove(10)#remove by value
>>> x
[8, 2, 3]
>>> del x[0]
>>> x
[2, 3]
>>> x.clear()
>>> x
[]
>>> #list comprehension
>>> x = [i for i in range(1,11)]
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
