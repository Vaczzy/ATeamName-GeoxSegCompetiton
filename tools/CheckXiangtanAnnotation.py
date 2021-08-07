"""
由于标签数据经过多次修改，为确保采用了统一标准的标签数据，可利用此脚本对标签数据进行基础性的检查
！！！注意：请设置好标签数据路径
所采用的标签数据应满足如下要求：
1.不包含数值为255的像素
2.最大标号为8，且标号为7像素值不为0


！！！：若通过检查，打印符合要求的信息
anthor:zzy
time:2021.08.07
"""

import os
import cv2
import numpy as np 

# 在此设置包含标签数据的文件路径
# ！！！务必对训练集和测试集都进行检查
# 请只修改此处
annotation_dir = r'/media/csu/ZL/SegCompetition/annotations/validation_max8' 


control=True
annotation_count=np.zeros((10,1)) # target value
for file in os.listdir(annotation_dir):
    annotation=cv2.imread(annotation_dir+'/'+file)
    # check
    if np.sum(annotation==255)!=0:
        print('请使用不含255的标签数据！')
        control=False
        break
    else:
        # print(annotation)
        for i in range(10):
            annotation_count[i,0]+=np.sum(annotation==i)

if annotation_count[9,0]!=0:
    print('请使用去除none类型的标签数据！')
elif annotation_count[6,0]==0:
    print('请使用去除none类型的标签数据或检查标签转换过程！')
elif control:
    print('该标签数据符合基本要求！')
