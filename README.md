# ATeamName-GeoxSegCompetiton
“谁有创意起个队名”队遥感影像语义分割天梯榜

## 目的
**便于迭代优化和结果提交及查看**

## 初步构想
* 设定某个提交结果的标准，该标准应包括提交者，（提交时间），**训练测试结果**，**训练参数设置**等
* 对训练测试结果进行归档，**给出各项指标的最好结果**和历史结果，以及各个结果对应的提交时间，模型和参数设置，**提交者**等。

## 功能测试中....
1.提交数字，按照高低排序
2.显示提交时间

## 提交说明和规范
请按规范提交以下内容：
* index.txt **(必须包含的)**  
包含模型名称，提交者，和**各类精度**  
**示例:**  参考data中20210807zzy文件中index.txt
* 若使用**mmsegmention**框架训练，还需要提交训练完成后**work_dir**中保存的**log**和**json**文件
* 上述文件放置在一个文件夹中提交到**data**目录下
