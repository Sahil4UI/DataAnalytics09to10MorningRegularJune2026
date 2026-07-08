Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #variables are the container which contains value
>>> x = 12
>>> #x is VARIABLE
>>> #rules to name variables:
>>> \
...   
>>> #variable name cannot starts with no or any special character(except _)
>>> 1x = 12
SyntaxError: invalid decimal literal
>>> %^&%^x = 12
SyntaxError: invalid syntax
>>> #variable name cannot contains special character(except _)
>>> x$y - 12
SyntaxError: invalid syntax
>>> x$y=12
SyntaxError: invalid syntax
>>> #variable name cannot be named with keywords name

print = 12
print(print)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(print)
TypeError: 'int' object is not callable
del print
print
<built-in function print>

#data types:
x = 12
type(x)
<class 'int'>
x = 34.456
type(x)
<class 'float'>
x = 4+6j
type(x)
<class 'complex'>
x = "hello jyoti"
type(x)
<class 'str'>
a = None
type(x)
<class 'str'>
type(a)
<class 'NoneType'>
a = True
type(a)
<class 'bool'>
