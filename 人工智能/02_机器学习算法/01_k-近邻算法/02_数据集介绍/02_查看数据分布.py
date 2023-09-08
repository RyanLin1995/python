import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]  # matplotlib 显示中文设置
mpl.rcParams["axes.unicode_minus"] = False  # 设置正常显示符号

# 把数据装换成 dataframe 格式
iris = load_iris()
iris_df = pd.DataFrame(iris['data'], columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])
iris_df['Species'] = iris.target  # 设置目标值列


def plot_iris(iris_data, col_x, col_y):
    # sns.lmplot() 表示绘制散点图
    # x, y 分别代表横纵坐标的列名,
    # data 是关联到数据集,
    # hue 代表按照 species （即花的类别）分类显示,
    # fit_reg 是否进行线性拟合
    sns.lmplot(iris_data, x=col_x, y=col_y, hue='Species', fit_reg=False)
    plt.xlabel(col_x)
    plt.ylabel(col_y)
    plt.title('鸢尾花种类分布图')
    plt.show()


plot_iris(iris_df, 'Petal_Width', 'Sepal_Length')
