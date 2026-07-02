Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#loop - repetition
print(1)
1
print(2)
2
print(3)
3
#DRY - Dont Repeat Yourself
for i in range(1,6):
    print(i)

1
2
3
4
5
for i in range(1,6,1):
    print(i)

1
2
3
4
5

for i in range(1,11,2):
    print(i)

1
3
5
7
9
for i in range(10,0,-1):
    print(i)

10
9
8
7
6
5
4
3
2
1
for i in reversed(range(1,11)):
    print(i)

10
9
8
7
6
5
4
3
2
1
#break,continue,pass
for i in range(1,10000000000000000001):
    if i==5:
        break
    print(i)
#break - it is used to exit the loop
... 
1
2
3
4
>>> 
>>> for i in range(1,11):
...     if i%2==0:
...         continue
...     print(i)
... 
1
3
5
7
9
>>> #continue is used to skip current iteration
>>> for i in range(1,11):
...     pass
... 
