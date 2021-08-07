f = open("./data/ModelList.txt")
line = f.readline()
ModelNum=int(line)
for i in range(ModelNum):
    line = f.readline()
print('New Model Num is '+str(ModelNum))
print('New Model :'+line)
f.close()
