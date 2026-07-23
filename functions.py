# user defined function
#function definition
#default
# def f1():
#     print("F1 called...")

# function calling
# f1()

# import calculator
# calculator.add(12,15)

#parameterised function
'''
def f1(a,b):
    print(a*b)

f1(12,5)
'''
# here b is optional parameter
# def f1(a,b=5):
#     print(a*b)

# f1(12)

#* args and ** arguments
# def student(roll,name,contact,*others):
#     print(roll,name,contact,others)


# student(101,"aman",987654210,"harish","dancing")

# ---------------------------------
'''
def student(roll,name,contact,**others):
    print(roll,name,contact,others)

student(101,"aman",987654210,father="harish",hobby="dancing")
'''


#function with return type
'''
def add(x,y):
    return x+y
# jaha se function call hua wapas vhi jayega

result = add(1,2)
print(result)
'''

# Return vs Yield
# def f1():
#     for i in range(1,11):
#         return i
#     # return statements help to exit the function

# result = f1()
# print(result)

'''
def f1():
    for i in range(1,11):
        yield i
    # return statements help to exit the function

result = list(f1())
print(result)
'''

#recursion - when a function calls itself again and again
# that function is known as recursion

def f1(x):
    if x>5:
        return

    f1(x+1)                   
    print(x)
    

f1(1)



