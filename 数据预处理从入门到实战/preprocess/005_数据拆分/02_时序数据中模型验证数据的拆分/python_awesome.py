from preprocess.load_data.data_loader import load_monthly_index
monthly_index_tb = load_monthly_index()

# 本书刊登内容如下
# 在train_window_start中指定原始的训练数据的起始行号
train_window_start = 1
# 在train_window_end中指定原始的训练数据的终止行号
train_window_end = 24
# 在horizon中指定验证数据的条数
horizon = 12
# 在skip中设置要滑动的数据条数
skip = 12

# 基于年月进行数据排序
monthly_index_tb.sort_values(by='year_month')

while True:
  # 计算验证数据的终止行号
  test_window_end = train_window_end + horizon

  # 指定行号，从源数据中获取训练数据
  # 如果将train_window_start 固定为1，则可以方便地调整训练数据的条数
  train = monthly_index_tb[train_window_start:train_window_end]

  # 指定行号，从源数据中获取验证数据
  test = monthly_index_tb[(train_window_end + 1):test_window_end]

  # 判断验证数据的终止行号是否超出源数据的行数 
  if test_window_end >= len(monthly_index_tb.index):
    # 全部数据已用到，退出 
    break

  # 滑动数据 
  train_window_start += skip
  train_window_end += skip

# 汇总交叉验证的结果
