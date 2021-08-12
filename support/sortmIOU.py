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

def WriteData(filePath,smIoU):
    """
    将获取的最佳结果写入log中，最佳结果存储在Best中
    """
    ts=time.time()
    tz = pytz.timezone('Asia/Shanghai')
    dt = pytz.datetime.datetime.fromtimestamp(ts, tz)
    localtime=dt.strftime('%Y-%m-%d %H:%M:%S')
    f = open(filePath,'w')
    f.write('Time: '+localtime+'\n')
    f.write('*Sort by mIoU: \n')
    for i in len(smIoU):
        f.write(str(i)+',  '+smIoU[i][0]+': '+smIoU[i][1])
    f.close()
    
path='./data'
filepath='./Rank_mIoU/rank.log'
mIoU=readIoU(path)
smIoU=sorted(mIoU.items(), key = lambda kv:(kv[1], kv[0]))
# 写文件
WriteData(filePath,smIoU)

