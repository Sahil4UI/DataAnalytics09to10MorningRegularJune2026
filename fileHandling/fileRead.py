#r stands for read
with open("abc.txt","r") as file:
    # data = file.read()
    # data = file.read(5)
    # shuru ke 5 characters
    # data = file.readline()
    #first line
    data = file.readlines()
    # all lines in a list

    print(data)