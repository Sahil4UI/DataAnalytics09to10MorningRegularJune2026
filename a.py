from datetime import datetime
helloIntent = ["hi","hey","wassup","hello","hy"]
byeIntent = ["bye","tata","see you"]
chat=True
while chat==True:
    msg = input ("enter msg :") 
    if msg in helloIntent:
        print ("wassup...")
    elif msg in byeIntent:
        print ("tata")
        chat = False
    elif "date" in msg:
        dt = datetime.now()
        print(dt.strftime("%d/%m/%Y %a"))
    elif "time" in msg:
        dt = datetime.now()
        print(dt.strftime("%H/%M/%S %p"))
    else:
        print ("Sorry I didn't understand")     

        
        
         

         