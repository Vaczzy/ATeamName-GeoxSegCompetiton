# 按照平均IoU排序
import numpy as np
import os
import time
import pytz
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

def WriteData(filePath,smIoU):
    """
    写入数据
    """
    ts=time.time()
    tz = pytz.timezone('Asia/Shanghai')
    dt = pytz.datetime.datetime.fromtimestamp(ts, tz)
    localtime=dt.strftime('%Y-%m-%d %H:%M:%S')
    f = open(filePath,'w')
    f.write('Time: '+localtime+'\n')
    f.write('*Sort by mIoU: \n')
    for i in range(len(smIoU)):
        f.write(str(i+1)+',  '+smIoU[i][0]+': '+str(smIoU[i][1])+'\n')
    f.close()
    
path='./data'
filepath='./Rank_mIoU/rank.log'
mIoU=readIOU(path)
smIoU=sorted(mIoU.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
WriteData(filepath,smIoU)

