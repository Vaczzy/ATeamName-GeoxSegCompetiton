# “Who Has the Idea to Name a Team” WHINT-Geoxlab Segmentation Competiton
<img src="https://github.com/Vaczzy/ATeamName-GeoxSegCompetiton/raw/main/WHINT/whintlogo.PNG" >


### *“谁有创意起个队名”队* 遥感影像语义分割天梯榜


## mIoU Top5
<img src="https://github.com/Vaczzy/ATeamName-GeoxSegCompetiton/raw/main/visual/mIoUrank.png" >

(在[**visual**](./visual)文件夹中查看历史mIoU Top5榜单，在[**Rank_mIoU**](./Rank_mIoU)文件夹中查看所有的mIoU排序表单)
## 提交说明和规范
### 提交结果应包含：
* **index.txt**

该文件为提交结果的索引文件，榜单将根据索引文件对你的结果进行评估，请勿提交伪造的结果，管理员会检查你的设置和训练日志文件

示例模板：（提交时请不要包含注释说明和注释指引短线）
```
ModelName:deeplabv3p  -------------给您的提交结果（模型）起个名字，应包含使用的语义分割框架和简单trick
Submitter:zzy  --------------------您将展示给大家的提交者代号或姓名
Time:2021.08.07 -------------------提交时间
+------------+-------+-------+
|   Class    |  IoU  |  Acc  | ----请复制log文件中的最终结果
+------------+-------+-------+
| background | 99.61 | 99.67 |
|  farmland  | 76.56 | 86.09 |
|    city    | 46.87 | 62.35 |
|  village   | 44.57 | 57.19 |
|   water    | 67.39 | 79.14 |
|   forest   | 85.09 | 94.58 |
|   grass    | 10.67 | 13.66 |
|    road    | 37.51 | 52.04 |
|   others   |  0.13 |  0.63 |
+------------+-------+-------+
+-------+-------+------+
|  aAcc |  mIoU | mAcc |  -------请复制log文件中的最终结果
+-------+-------+------+
| 86.34 | 52.04 | 60.6 |
+-------+-------+------+
```
* 若使用**MMSegmentation**框架训练，还需：

对**default_runtime.py**中的**log_config**作如下设置：
```
log_config = dict(
    interval=50, # 设置您的打印频率，可更改
    hooks=[
        dict(type='TextLoggerHook', by_epoch=False),
    ])
```
提交：
1. **work_dir**中保存的**训练日志（log)文件**
2. **work_dir**中保存的**训练过程主要指标（log.json）文件**
3. **work_dir**中保存的**训练设置（py）文件**

* 使用其他框架的，应至少提交：

**训练日志和训练设置文件**

### 提交文件组织和提交位置：
* 提交文件组织：请将上述文件放置在**同一文件夹**中提交，文件夹名称可以不与index.txt中的ModelName相同，但**应体现提交模型的特点**
* 提交位置：[**data**](./data)文件夹内

### 提交后注意事项
* 提交结果后几秒内榜单将自动更新最佳榜单，最新的最佳榜单（Best_xxx.log保存在[**BestList**](./BestList)文件夹中）
* 若您的提交结果**超过了当前mIoU Top5**的成员，在检查无误后，主榜单将在几分钟内更新。

### 技术细节与数据保护
* 提交结果应采用与本榜其他提交结果一致的**基础**数据集
* 从数据保护的角度出发，本榜将不公开使用的基础数据集
* 若要获取数据，请联系管理员
* **特殊条款：若您的策略处于技术保护阶段，在提交技术保护表单（[TecProtectList](./TecProtectList)）的基础上，您可以隐去需要保护的训练设置后上传**

## 现阶段功能
为便于模型的迭代优化和改进，该榜现阶段提供的功能有：
1. 结果归档
2. 榜单显示
3. 设置查看


## 榜单查看
* 21个指标的榜单存储于[**BestList**](./BestList)文件夹中，包含历史榜单
* mIoU榜单(主榜)将在您的结果提交后给出（仅展示前5名），该榜单将展示在主页上方

## TODO List
* 训练时间加入评分标准
* 可视化训练过程重要参数变化

## Contributor:
贡献您的智慧将使得该榜单的功能更**完善**：）
