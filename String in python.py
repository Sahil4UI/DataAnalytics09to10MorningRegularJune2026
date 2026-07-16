Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#String:
#String is Python's mutable and ordered data collection.
#mutable means which can be changed
#ordered means indexing
x = "hello python"
len(x)
12
x.upper()
'HELLO PYTHON'
x.lower()
'hello python'
x.capitalize()
'Hello python'
x.title()
'Hello Python'
x
'hello python'
x[0]
'h'
x[1]
'e'
x[2]
'l'
x[-1]
'n'
x[-2]
'o'
#String slicing
x
'hello python'
x[0:5]
'hello'
x[:5]
'hello'
>>> x[:]
'hello python'
>>> x[0:5:1]
'hello'
>>> x[0:5:2]
'hlo'
>>> x[::-1]
'nohtyp olleh'
>>> #reverse of String
>>> x
'hello python'
>>> x.find("o")
4
>>> x.find("0",5)
-1
>>> #-1 means value not found
>>> x.find("o",5)
10
>>> x.rfind("o")#reverse find
10
x.index("o",5)
10
x.find("X")
-1
#-1 means value not found
x.index("X")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    x.index("X")
ValueError: substring not found

x
'hello python'
words = x.split()
words
['hello', 'python']
" ".join(words)
'hello python'

"#".join(words)
'hello#python'
x
'hello python'
x.count("e")
1
x.count("o")
2
x
'hello python'
x = "hello"
x
'hello'
x.center(6)
'hello '
x.center(7)
' hello '
x.center(15)
'     hello     '
x.center(20,"*")
'*******hello********'
x = '*******hello********'
x.lstrip("*")
'hello********'
x.rstrip("*")
'*******hello'
x.strip("*")
'hello'
x
'*******hello********'
x = "hey python"
x.startswith("h")
True
x.endswith("x")
False
x
'hey python'
x.isalpha()
False
x.isdigit()
False
y = "566"
y.isdigit()
True
x.isalnum()
False
x
'hey python'
x.islower()
True
x.isupper()
False
x
'hey python'
x.replace("python","java")
'hey java'
x
'hey python'
for char in x:
    print(char)

h
e
y
 
p
y
t
h
o
n

for i in range(len(x)):
    print(x[i])

h
e
y
 
p
y
t
h
o
n
