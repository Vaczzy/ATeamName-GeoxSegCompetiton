# “Who Has the Idea to Name a Team” WHINT-Geoxlab Segmentation Competiton
<img src="https://github.com/Vaczzy/ATeamName-GeoxSegCompetiton/raw/main/WHINT/whintlogo.PNG" >
“谁有创意起个队名”队遥感影像语义分割天梯榜


## 目的
**便于迭代优化和结果提交及查看**

## 构想
* 设定某个提交结果的标准，该标准应包括提交者，（提交时间），**训练测试结果**，**训练参数设置**等
* 对训练测试结果进行归档，**给出各项指标的最好结果**和历史结果，以及各个结果对应的提交时间，模型和参数设置，**提交者**等。

## 现阶段功能
1. 提交结果，给出各项指标的最好结果及其模型，提交者，时间等  
2. 查看提交模型的数据预处理设置，模型设置等

## 提交说明和规范
请按规范提交以下内容：
* index.txt **(必须包含的)**  
包含模型名称，提交者，和**各类精度**  
**示例:**  参考data中20210807zzy文件中index.txt
* 若使用**mmsegmentation**框架训练，还需要提交训练完成后**work_dir**中保存的**log**，**json**和训练设置**py**文件
* 上述文件放置在一个文件夹中提交到**data**目录下

## 提交后查看榜单（榜单仅列出最好结果和提交结果分数）
榜单存储于**BestList**文件夹中，包含历史榜单

## mIOU榜单排名[每日中午更新]
<img src="https://github.com/Vaczzy/ATeamName-GeoxSegCompetiton/raw/main/visual/mIoUrank.png" >



## 后续功能上线...
* 训练过程可视化分析

```diff
更新(最近5个)：
+ 2021.08.09： 更改了之前榜单时区的问题，目前的时区设定为北京时间（东8区）
+ 2021.08.10： 新增failedData栏，上传你的失败训练log文件，以供参考对照分析
+ 2021.08.12： 按照主流遥感影像语义分割竞赛评价指标mIoU进行排序,可视化排名结果
```
