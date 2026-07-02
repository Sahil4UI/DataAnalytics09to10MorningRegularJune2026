#write a program to check whether a given no is even or odd
'''
x = int(input("Enter no : "))
if x%2==0:
    print("Even No")
else:
    print("Odd No")
'''
#write a program to find the largest b/w two nos
'''
x = int(input("Enter no1 : "))
y = int(input("Enter no2 : "))

if x>y:
    print(f"{x} is largest")
else:
    print(f"{y} is largest")
'''

#write a program to find the largest b/w three nos
'''
x = int(input("Enter no1 : "))
y = int(input("Enter no2 : "))
z = int(input("Enter no3 : "))

if x>y and x>z:
    print(x,"is largest")
elif y>z:
    print(y,"is largest")
else:
    print(z,"is largest")
'''

#take 3 sides as input, and if they form a traingle,state the type of traingle : 
# equilateral
# Isoceles
# Scalene
'''
x = int(input("Enter Side1: "))
y = int(input("Enter Side2: "))
z = int(input("Enter Side3: "))

if x+y>z and y+z>x and z+x>y:
    if x==y and y==z :
        print("Equilateral Traingle")
    elif x==y or y==z or z==x:
        print("Isoceles Traingle")
    else:
        print("Scalene Traingle")
else:
    print("Invalid Sides")
'''

#MAtch case
order = int(input('''
Press 1 to order Pizza
Press 2 to order burger
Press 3 to order Dessert : 
'''))

match order:
    case 1:
        print("Pizza Ordered Successfully")
    case 2:
        print("Burger Ordered Successfully")
    case 3:
        print("Dessert Ordered Successfully")
    case _: 
        print("Out of Stock")