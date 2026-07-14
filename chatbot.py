from datetime import datetime

helloIntent = ["hi","hey","wassup","hello","hy"]
byeIntent = ["bye","tata","see you","ttyl"]
chat=True
while chat==True:
    msg = input("Enter msg : ")
    if msg in helloIntent:
        print("hey...")
    elif msg in byeIntent:
        print("Bye...")
        chat = False
    elif "date" in msg:
        dt = datetime.now()
        # String Format Time
        print(dt.strftime("%d/%m/%Y %a"))
    elif "time" in msg:
        dt = datetime.now()
        # String Format Time
        print(dt.strftime("%H/%M/%S %p"))
    else:
        print("Sorry I Didn't Understand")