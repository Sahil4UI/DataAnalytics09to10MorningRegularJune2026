#Q1.Write a program to find sum of first 10 integers
'''
result = 0
for i in range(1,11):
    result = result+i
print(result)
'''
#Q2. Print table of 2 as this format
'''
2X1=2
2X2=4
2X3==6
'''
'''
for i in range(1,11):
    print(f"2X{i}={2*i}")
'''
#Q3.Wap to find factorial of a number.
'''
result = 1
x = int(input("Enter no:"))
for i in range(1,x+1):
    result = result*i
print(result)
'''
#Q4.Wap to check whether the given no is prime or not
'''
x = int(input("Enter no:"))
for i in range(2,x):
    if x%i==0:
        print("Not Prime")
        break
else:
    print("Prime")
''' 
        

#Q5.Wap to find sum of digits of number.
'''x = int(input("Enter no:"))
result = 0
for i in range(len(str(x))):
    rem = x%10
    result = result+rem
    x=x//10
print(result)
 '''








