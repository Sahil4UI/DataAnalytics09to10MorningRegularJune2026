# Wap to find largest no from list.
'''
x = [10,0,78,65,7,546,-10,4]
largest = x[0]
for num in x:
    if num>largest:
        largest=num
print(largest)
'''
#shortcut
# x = [10,0,78,65,7,546,-10,4]
# print(max(x))



#write a program to remove the duplicates from the list
'''
x = [1,1,1,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5]
y = []

for num in x:
    if num not in y:
        y.append(num)

print(y)
'''
#shorcut
# x = [1,1,1,2,2,2,2,2,3,4,4,4,4,4,5,5,5,5]
# print(list(set(x)))


#write a program to sort the array in ascending order.
'''
x = [10,0,78,65,7,546,-10,4]
for i in range(0,len(x)-1):
    for j in range(i+1,len(x)):
        if x[i]>x[j]:
            x[i],x[j]=x[j],x[i]
            #swapping the values
print(x)
'''
x = [10,0,78,65,7,546,-10,4]
x.sort(reverse=True)
print(x)