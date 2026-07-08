Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#loops
for i in range(1,11):
    print(i)

1
2
3
4
5
6
7
8
9
10
>>> for i in range(1,11,1):
...     print(i)
... 
1
2
3
4
5
6
7
8
9
10
>>> for i in range(1,11,2):
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
for i in reversed(range(1,11)):"
SyntaxError: unterminated string literal (detected at line 1)
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
for i in range(1,110000000):
    print(i)
    if i==5:break

1
2
3
4
5
for i in range(1,11):
    if i%2==0:
        continue
    print(i)

1
3
5
7
9

for i in range(1,11):
    pass

