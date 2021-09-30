f = open("./data/history_3_8.txt", "r")
data = f.read()
listData = data.split("x\n")

f.close()
print(len(listData))
print(listData[len(listData)-2])
with open("./data/handingResult_3_8", "a+") as hs:
    for stringValue in listData:
        try:
            value = float(stringValue)
        except:
            pass
        if(value > 1 and value < 2):
            hs.write("a")
        elif(value >= 2 and value < 3):
            hs.write("b")
        elif(value >= 3 and value < 4):
            hs.write("c")
        elif(value >= 4 and value < 5):
            hs.write("d")
        elif(value >= 5 and value < 6):
            hs.write("e")
        elif(value >= 6 and value < 7):
            hs.write("f")
        elif(value >= 7 and value < 8):
            hs.write("g")
        elif(value >= 8 and value < 9):
            hs.write("h")
        elif(value >= 9 and value < 10):
            hs.write("i")
        else:
            hs.write("k")
rs = open("./data/handingResult_3_8", "r")
dataRs = rs.readline()
rs.close()
print(len(dataRs))
print(dataRs[len(dataRs)-1])
