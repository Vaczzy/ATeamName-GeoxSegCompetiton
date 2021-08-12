# 按照平均IoU排序
import numpy as np
import os
def readIOU(path):
    mIoU={}
    i=0
    for folder in os.listdir(path):
        f = open(path+'/'+folder+'/index.txt')
        
        modelName = ((f.readline()).split(':')[1]).split('\n')[0] 
        submitter = ((f.readline()).split(':')[1]).split('\n')[0] 
        time = ((f.readline()).split(':')[1]).split('\n')[0]
        line = f.readline()
        line = f.readline()
        line = f.readline()
        for i in range(9):
            element=f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        element=f.readline()
        mIoU[modelName]=float(element.split('|')[2])
        f.close()
    return mIoU

path='./data'
mIoU=readIoU(path)
smIoU=sorted(mIoU.items(), key = lambda kv:(kv[1], kv[0]))
# 写文件


