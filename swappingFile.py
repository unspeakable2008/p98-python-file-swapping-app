def swapFileData():
    fileName = input("enter the first file name-")
    fileName2 = input("enter the second file name-")
    f1=open(fileName,"r")
    f2=open(fileName2,"r")
    data1 = f1.read()
    data2 = f2.read()
    with open(fileName,"w")as a:
        a.write(data2)
    with open(fileName2,"w")as b:
        b.write(data1)
swapFileData()    