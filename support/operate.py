f = open("./data/tets.txt")
line = f.readline()
while line:
    num=int(line)
    print(num)
    line = f.readline()
f.close()
