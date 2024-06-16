# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 18:50:56 2020

@author: Administrator
"""
from preprocess.load_data.data_loader import load_production_missing_num
# 直接调用已经封装好的函数
production_miss_num = load_production_missing_num()

import statsmodels.api as sm
from statsmodels.imputation import mice
import pandas as pd
import numpy as np

#将缺失值统一替换为np.nan
production_miss_num.replace('None',np.nan,inplace=True)

#将数据类型由pandas的Series类型转换为float64、category类型
production_miss_num['thickness']=\
    production_miss_num['thickness'].astype('float64')
    
production_miss_num['type']=\
    production_miss_num['type'].astype('category')
    
production_miss_num['fault_flg']=\
    production_miss_num['fault_flg'].astype('category')

#将分类变量转换为哑变量
production_dummy_flg=pd.get_dummies(
        production_miss_num[['type','fault_flg']],drop_first=True)

#将转换后的各列拼接成一个数据集
dataset=pd.concat([production_miss_num[['length','thickness']],production_dummy_flg],axis=1)
#封装数据集，供插补模型使用
fit_data=mice.MICEData(dataset,k_pmm=6)
#指定扰动变量
fit_data.perturb_params('thickness')
#使用预测均值插补
fit_data.impute_pmm('thickness')
#查看插补后数据
fit_data.data
#查看模型参数置信区间
fit_data.results['thickness'].conf_int()
#查看各变量间的协方差矩阵，可分析变量间的相关性
fit_data.results['thickness'].cov_param()
#更新参数列的值
fit_data.update('thickness')

#下面的注释代码是通过使用普通最小二乘法拟合进行线性插补
#fml='thickness ~ length + type_B + type_C + type_E + type_E + fault_flg_True'
#model=mice.MICE(fml,sm.OLS,fit_data)
#results=model.fit()
#results.summary()


