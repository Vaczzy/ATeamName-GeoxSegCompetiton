import os
import numpy as np
import pytz
import time
 
classlist=['background','farmland','city','village','water','forest','grass','road','others']

def WriteData(filePath,Best,modelScore):
    """
    将获取的最佳结果写入log中，最佳结果存储在Best中
    """
    ts=time.time()
    tz = pytz.timezone('Asia/Shanghai')
    dt = pytz.datetime.datetime.fromtimestamp(ts, tz)
    localtime=dt.strftime('%Y-%m-%d %H:%M:%S')
    f = open(filePath,'w')
    f.write('Time: '+localtime+'\n')
    f.write('BEST LIST\n')
    f.write('* IoU: \n')
    for i in range(9):
        f.write(' '+classlist[i]+': '+str((Best['best_iou'])[i,0])\
            +'   '+Best['best_iou_mark'][i]+'\n')
    f.write('* mIoU: '+str(Best['best_miou'])+'   '+Best['best_miou_mark']+'\n')
    f.write('* Acc: \n')
    for i in range(9):
        f.write(' '+classlist[i]+': '+str((Best['best_acc'])[i,0])\
            +'   '+Best['best_acc_mark'][i]+'\n')
    f.write('* mAcc: '+str(Best['best_macc'])+'   '+Best['best_macc_mark']+'\n')
    f.write('* aAcc: '+str(Best['best_aacc'])+'   '+Best['best_aacc_mark']+'\n')
    
    # 写入模型得分
    f.write('----------------------------------------------------')
    f.write('\nFull Marks: 21')
    for key,value in modelScore.items():
        f.write('\n'+key+':   '+str(value))
    f.close()

def ReadSelectBest(path):
    """
    读取存放在指定位置的提交结果，并寻找最佳结果
    路径总为./data
    """
    # 获取之前的最佳结果
    best_iou=np.zeros((9,1)) # 9种地物类型对应的最佳iou
    best_iou_mark=['','','','','','','','','']
    best_acc=np.zeros((9,1))
    best_acc_mark=['','','','','','','','','']

    best_aacc=0
    best_aacc_mark=['']
    best_miou=0
    best_miou_mark=['']
    best_macc=0
    best_macc_mark=['']

    # 检查提交的结果
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
            IoU = float(element.split('|')[2])
            if IoU>best_iou[i,0]:
                best_iou[i,0]=IoU
                best_iou_mark[i]=modelName+', '+submitter+', '+time
            Acc = float(element.split('|')[3])
            if Acc>best_acc[i,0]:
                best_acc[i,0]=Acc
                best_acc_mark[i]=modelName+', '+submitter+', '+time
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()

        element=f.readline()
        aAcc=float(element.split('|')[1])
        if aAcc>best_aacc:
            best_aacc=aAcc
            best_aacc_mark=modelName+', '+submitter+', '+time
        mIoU=float(element.split('|')[2])
        if mIoU>best_miou:
            best_miou=mIoU
            best_miou_mark=modelName+', '+submitter+', '+time
        mAcc=float(element.split('|')[3])
        if mAcc>best_macc:
            best_macc=mAcc
            best_macc_mark=modelName+', '+submitter+', '+time
        f.close()

    # 字典
    Best={}
    Best['best_iou']=best_iou
    Best['best_iou_mark']=best_iou_mark
    Best['best_acc']=best_acc
    Best['best_acc_mark']=best_acc_mark

    Best['best_aacc']=best_aacc
    Best['best_aacc_mark']=best_aacc_mark
    Best['best_miou']=best_miou
    Best['best_miou_mark']=best_miou_mark
    Best['best_macc']=best_macc
    Best['best_macc_mark']=best_macc_mark

    return Best

def GetScore(path, Best):
    """
    在获取完best之后打分
    """
    modelScore={}
    for folder in os.listdir(path):
        singleModelScore=0
        f = open(path+'/'+folder+'/index.txt')
        
        modelName = ((f.readline()).split(':')[1]).split('\n')[0] 
        submitter = ((f.readline()).split(':')[1]).split('\n')[0] 
        time = ((f.readline()).split(':')[1]).split('\n')[0]
        line = f.readline()
        line = f.readline()
        line = f.readline()
        for i in range(9):
            element=f.readline()
            IoU = float(element.split('|')[2])
            if IoU>=Best['best_iou'][i,0]:
                singleModelScore+=1    
            Acc = float(element.split('|')[3])
            if Acc>=Best['best_acc'][i,0]:
                singleModelScore+=1  
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()

        element=f.readline()
        aAcc=float(element.split('|')[1])
        if aAcc>=Best['best_aacc']:
            singleModelScore+=1  
        mIoU=float(element.split('|')[2])
        if mIoU>=Best['best_miou']:
            singleModelScore+=1  
        mAcc=float(element.split('|')[3])
        if mAcc>=Best['best_macc']:
            singleModelScore+=1  
        f.close()

        modelScore[modelName+','+submitter+','+time]=singleModelScore
    return modelScore

path='./data' # 保存提交结果的路径

time_mark=time.strftime(r"%Y_%m_%d_%H_%M_%S", time.localtime())
bestFolderName='./BestList/Best_'+time_mark+'.log' # 保存当前最佳结果的路径

Best=ReadSelectBest(path)
print(Best)
ModelScore=GetScore(path, Best)
WriteData(bestFolderName,Best,ModelScore)
