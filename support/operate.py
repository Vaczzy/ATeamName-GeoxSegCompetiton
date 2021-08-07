f = open("./data/test.txt")
line = f.readline()
while line:
    num=int(line)
    print(num)
    line = f.readline()
f.close()
