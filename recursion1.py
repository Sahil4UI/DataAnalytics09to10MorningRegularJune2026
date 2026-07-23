# find the power of number using recursion.
# def pow(a,b):
#     if b==0:
#         return 1
#     elif b==1:
#         return a
#     return a*pow(a,b-1)

# res = pow(2,4)
# print(res)

# find the length of string using recursion.

# def length(text):
#     if text=="":
#         return 0
#     return 1+length(text[1:])


# res = length("hello")
# print(res)



# find the factorial of no using recursion.
'''
def fac(x):
    if x==0 or x==1:
        return 1
    return x*(fac(x-1))

res = fac(5)
print(res)
'''

# find the sum of digits of no using recursion.
'''
def f1(x):
    if x==0:
        return 0
    return x%10+f1(x//10)
    

res = f1(123)
print(res)'''