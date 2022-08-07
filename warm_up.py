import threading,requests,os,time,random
u = "@@@C@@@@@@@@@@@@@@:@@@@@@@@@@@@@@@@@@@@@@@@@\\@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@W@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@in@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@d@@@@@@@@@@@@@@@@@o@@@@@@@@@@@@@@@@@@@@@@@@@@@w@@@@@@@@@@@@s"
google = "https://www.google.com"
online = False
wow = ""
for char in u:
    if char != "@":
        wow += char
for _ in range(10):
    try:
        x = requests.get(google)
        time.sleep(.5)
        if x.status_code == 200:
            online = True
            break
    except:
        pass
if online:
    print("Online")
    f = open("random.txt","w")
    for _ in range(10):
        x = requests.get(google)
        f.write(x.text)
    time.sleep(1)
    f.write(" ")
    f.close()
    os.chdir(wow)
    os.system("tree")
else:
    print("Offline")
    f = open("random.txt","w")
    yo = ""
    for _ in range(90000000):
        yo += "wow"
    f.write(str(yo))
    time.sleep(1)
    f.write(" ")
    f.close()


    os.chdir(wow)
    os.system("tree")
    