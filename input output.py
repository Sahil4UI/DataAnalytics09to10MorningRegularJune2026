#How to take input and output in python
x = int(input("Enter No1:"))
y = int(input("Enter No2:"))
print("The sum of",x,"and",y,"is",x+y)
print("The sum of %d and %d is %d"%(x,y,x+y))
print("The sum of {} and {} is {}".format(x,y,x+y))
print(f"The sum of {x} and {y} is {x+y}")
