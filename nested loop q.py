'''
*
**
***
****
*****
'''

# for row in range(1,6):
#     for col in range(row):
#         print("*",end="")
#     print()#next line


# for row in range(1,6):
#     for col in range (row):
#         print(col,end="")
#     print()

# 1
# 01
# 010
# 1010
# 10101

'''
x=1
for row in range(1,6):
    for col in range(row):
        if x%2==0:
            print(0,end="")
        else:
            print(1,end="")
        
        x=x+1
    print()
'''

# *****
# *****
# *****
# *****
# *****

# for row in range(1,6):
#     for col in range (1,6):
#         print("*",end="")
#     print()
# H
# for row in range(1,6):
#     for col in range (1,6):
#         if col==1 or col==5 or row==3:
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

# E
# for row in range(1,6):
#     for col in range (1,6):
#         if col==1  or row in (1,5) or (row==3 and col<4 ):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()
