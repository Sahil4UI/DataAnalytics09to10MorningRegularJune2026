from datetime import datetime
import webbrowser
import os
import glob
#iski help se kisi folder ki specific files ko filter krlete h

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
    elif "open" in msg:
        webbrowser.open(msg.split()[1]+".com")
    elif "music" in msg or "song" in msg:
        # chdir - change directory - us folder m jyenge jaha files hongi
        os.chdir(r"C:\Users\user\Downloads")
        # list directory - jis folder me mai gaya hu uske andar ki sari files show hojyengi
        # files = os.listdir()
        songs = glob.glob("*.mp3")
        print("MUSIC LIST : ")
        x=1
        for song in songs:
            print(x,"=>",song)
            x=x+1
            print()
        no =  int(input("Enter Song No to Play : "))
        os.startfile(songs[no-1])
        print("*****Music Played***")
    else:
        print("Sorry I Didn't Understand")