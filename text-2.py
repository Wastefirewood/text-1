import pandas as pd


data = pd.read_csv('https://edidata.oss-cn-beijing.aliyuncs.com/fyx_chinamoney.csv')  # 读取CSV文件

code_list = data['code'].tolist()  # 获取代码列表

# 将代码列表拆分成多个数组
batch_size = 80
batches = []

for i in range(0, len(code_list), batch_size):  # 每个80个代码遍历一次,
    batch = code_list[i:i + batch_size]
    batches.append(batch)

# 打印输出每个批次的数组
for batch in batches:
    print(batch)