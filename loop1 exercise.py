# Q1.wap to find sum of first 10 natural nos
'''
result=0
for i in range(1,11):
    result=result+i
print(result)
'''

# Write a Python program to find those numbers which are
# divisible by 7 and multiples of 5, 
# between 1500 and 2700 (both included).
'''
for i in range(1500,2701):
    if i%7==0 and i%5==0:
        print(i)
'''

# Write a Python program to convert temperatures to and 
# from Celsius and Fahrenheit.
# [ Formula : c/5 = (f-32)/9
#   [ where c = temperature in celsius and 
#    f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius
'''
t = int(input("enter temperature : "))
choice = input("Enter C/F : ")
if choice=="F" or choice=="f":
    print((t-32)*5/9," C")
elif choice=="C" or choice=="c":
    print(t*9/5+32,"F")
'''

# Write a Python program to guess a number between 1 and 9.
'''
import random
no = random.randint(1,9)
#infinite loop
while True:
    x = int(input("Enter no:"))
    if x==no:
        print("Your Guess is correct")
        break
    print("Try again")
'''
'''
*
**
***
****
*****
'''
'''
for i in range(1,6):
    print("*"*i)
'''
'''
    *
   **
  ***
 ****
*****
'''
for i in range(1,6):
    print(" "*(5-i),"*"*i)
