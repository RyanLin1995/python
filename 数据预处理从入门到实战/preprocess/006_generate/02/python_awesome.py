from preprocess.load_data.data_loader import load_production
production_tb = load_production()

# 本书刊登内容如下
# 从库中导入SMOTE函数
from imblearn.over_sampling import SMOTE

# 设置SMOTE函数参数
# ratio表示的是将不平衡数据中少数类的数据增加至多数类的数据的百分之多少
# （当设置为auto时，表示增加至与多数类的数据量相同；当设置为0.5时，表示增加至50%）
# k_neighbors为smote的k参数
# random_state是随机数种子（随机数生成模式的基础）
sm = SMOTE(ratio='auto', k_neighbors=5, random_state=71)

# 执行过采样
balance_data, balance_target = \
  sm.fit_sample(production_tb[['length', 'thickness']],
                production_tb['fault_flg'])
