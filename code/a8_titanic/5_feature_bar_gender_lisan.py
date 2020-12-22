# -*- coding: utf-8 -*-
# 加载相关模块和库
import sys
import io
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
"""
本次实战选择决策书作为分类算法，因此可以避免问题
至此来观察数据特征，以更好的选择算法
性别-获救比例
"""
import pandas as pd #数据分析
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
data_train = pd.read_csv("D:/python/projects/AI-learning/my_ai/day3/code/a8_titanic/data/train.csv")

#看看各性别的获救情况
Survived_0 = data_train.Sex[data_train.Survived == 0].value_counts()
Survived_1 = data_train.Sex[data_train.Survived == 1].value_counts()
df=pd.DataFrame({u'获救':Survived_1, u'未获救':Survived_0})


df.plot(kind='bar', stacked=True)
plt.title(u"按性别看获救情况")
plt.xlabel(u"性别")
plt.ylabel(u"人数")
plt.show()

