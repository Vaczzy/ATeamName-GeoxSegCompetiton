# ATeamName-GeoxSegCompetiton
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
* 若使用**mmsegmention**框架训练，还需要提交训练完成后**work_dir**中保存的**log**，**json**和训练设置**py**文件
* 上述文件放置在一个文件夹中提交到**data**目录下

## 提交后查看榜单（榜单仅列出最好结果和提交结果分数）
榜单存储于**BestList**文件夹中，包含历史榜单

## 后续功能上线...
* 训练过程可视化分析
* 榜单结果可视化 
