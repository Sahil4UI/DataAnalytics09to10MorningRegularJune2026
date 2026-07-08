#input and output in python
'''
x = int(input("Enter no1:"))
y = int(input("Enter no2:"))

print("sum of",x,"and",y,"is",x+y)
print("sum of {} and {} is {}".format(x,y,x+y))
print("sum of %d and %d is %d"%(x,y,x+y))
print(f"sum of {x} and {y} is {x+y}")
'''

#conditions
#match case:
#\n means next line
'''
order = int(input("Press 1 to Order Burger\nPress 2 to order Pizza:"))
match(order):
    case 1:print("Your Burger is ready")
    case 2:print("Your Pizza is ready")
    case _:print("not in menu")
'''
#if else
'''
x = int(input("enter no1:"))
y = int(input("enter no2:"))
z = int(input("enter no3:"))

if x>y and x>z :
    print(x,"is largest")
elif y>z:
    print(y,"is largest")
else:
    print(z,"is largest")
'''





















