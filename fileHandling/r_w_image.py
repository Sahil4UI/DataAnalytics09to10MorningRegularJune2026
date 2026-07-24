# read bytes
data = None
with open("image.png","rb") as file:
    data = file.read()

with open("oggy.png","wb") as file:
    file.write(data)