from preprocess.load_data.data_loader import load_production
production_tb = load_production()

# 本书刊登内容如下
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

# 为进行留出验证而执行数据拆分
# 分别在train_test_split函数中设置预测模型的输入值和预测值
# test_size是验证数据的比例
train_data, test_data, train_target, test_target = \
  train_test_split(production_tb.drop('fault_flg', axis=1),
                   production_tb[['fault_flg']],
                   test_size=0.2)

# 通过train_test_split将行名修改为当前的行号
train_data.reset_index(inplace=True, drop=True)
test_data.reset_index(inplace=True, drop=True)
train_target.reset_index(inplace=True, drop=True)
test_target.reset_index(inplace=True, drop=True)

# 生成对象的行号列表
row_no_list = list(range(len(train_target)))

# 为进行交叉验证而执行数据拆分
k_fold = KFold(n_splits=4, shuffle=True)

# 执行“交叉验证的折数”次循环处理，可并行处理 
for train_cv_no, test_cv_no in k_fold.split(row_no_list):

  # 提取交叉验证用的训练数据
  train_cv = train_data.iloc[train_cv_no, :]

  # 提取交叉验证用的测试数据
  test_cv = train_data.iloc[test_cv_no, :]

  # 将train_data和train_target作为训练数据，
  # 将test_data和test_target作为验证数据，构建和验证机器学习模型

# 汇总交叉验证的结果

# 将train作为训练数据，将private_test作为验证数据，构建和验证机器学习模型
