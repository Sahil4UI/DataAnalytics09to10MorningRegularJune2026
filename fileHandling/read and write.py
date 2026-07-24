with open("demo.txt","w+") as file:
    # w+ - write+read
    file.write("Hello welcome to our class")
    file.seek(0)
    # cursor will now be at starting
    data = file.read()
    print(data)