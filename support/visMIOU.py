import matplotlib.pyplot as plt
import time

# read mIoU
path='./Rank_mIoU/rank.log'
f=open(path,'r')
title='mIoU Rank '+f.readline()
ModelNum=int(((f.readline()).split(':')[1]).split('\n')[0])
line=f.readline()
name_list=[]
num_list=[]
for i in range(ModelNum):
    element=f.readline().split(', ')[1]
    name_list.append(element.split(':')[0])
    num_list.append((element.split(':')[1]).split('\n')[0])
# darw and save
time_mark=time.strftime(r"%Y_%m_%d_%H_%M_%S", time.localtime())
savepath='./visual/mIoUrank_'+time_mark+'.png'

plt.title(title)
plt.barh(range(ModelNum), num_list,tick_label=name_list)
plt.savefig(savepath)
