import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.ticker as ticker
from matplotlib.ticker import MultipleLocator
#
# data_origin = pd.read_csv("LD_MT200_hour.csv",header=0,low_memory=False, infer_datetime_format=True, engine='c', index_col=['date'])
#
# print(data_origin.shape)
#
#
# print(data_origin.isna().sum())


# def dataset_distribution(dataset):
#     plt.figure(figsize=(16, 12), dpi=150)
#     for i in range(len(dataset.columns)):
#         ax = plt.subplot(len(dataset.columns), 1, i + 1)
#         ax.set_ylabel(r'$numbers$', size=10)
#
#         feature_name = dataset.columns[i]
#
#         dataset[feature_name].hist(bins=100)
#
#         plt.title(feature_name, y=0, loc='right', size=20)
#         plt.grid(linestyle='--', alpha=0.5)
#         plt.xticks(rotation=0)
#
#     plt.tight_layout()
#     plt.show()
#
#
# dataset_distribution(data_origin)
#

# def plot_features(dataset):
#     plt.figure(figsize=(16, 12), dpi=200)
#     for i in range(len(dataset.columns)):
#         ax = plt.subplot(len(dataset.columns), 1, i + 1)
#         x_major_locator = MultipleLocator(300)
#         feature_name = dataset.columns[i]
#         plt.plot(dataset[feature_name])
#         plt.title(feature_name, y=0)
#         plt.grid(linestyle='--', alpha=0.5)
#         ax.xaxis.set_major_locator(x_major_locator)
#         plt.savefig('save.jpg')
#
#     plt.tight_layout()
#     plt.show()
#
#
# plot_features(data_origin)


# db = pymysql.connect(host="localhost", user="root", password="LQW1107@python", database="modeldata",charset="utf8")
# cursor = db.cursor()
# x = ['cnn','lstm','en_de','cnn_lstm','convlstm']
# z = []
# h = []
# for i in range(len(x)):
#     sql = "select * from modelinfo where model=" + x[i]
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     for y in results:
#         z.append(y)
#     h.append(z)
#
# model_name = []
# rmse = []
# MAX_rmse = []
# MIN_rmse = []
# MAE = []
#
# sql = "insert into modelinfo values = (" + model_name + ',' + rmse + ',' + MAX_rmse + ',' + MIN_rmse + ','+ MAE+ ")"
# predictions = list()
#
#
# for i in range(len(predictions)):
#     sql = "insert into modelResult values = (" + predictions[i]+")"
# x = [28.400343635591003, 55.61318778193645, 84.04726828092312, 109.68652037297332, 157.44522567174425, 206.86909516785434, 225.0039287231956, 256.0383658309362, 259.2314902588912, 238.9473728834336, 215.14337541268958, 204.59966045044456, 209.97895947061323, 226.49103830249737, 239.06742571587344, 252.9779313219142, 254.7034743560408, 244.2934366010722, 231.8166268959205, 222.51556779550208, 212.07288772391476, 204.53865083191684, 189.37355456491892, 177.28910336035565]
# a = 0
# for i in range(24):
#     a += x[i]
# b = a/24
# print(b)
# [
#     [2910, 2853, 2816, 2810, 2829, 2854, 2953, 3030, 3024, 3032, 3024, 2998, 2958, 2925, 2834, 2808, 2866, 3115, 3216, 3170, 3152, 3066, 2920, 2780],
#     [2853, 2816, 2810, 2829, 2854, 2953, 3030, 3024, 3032, 3024, 2998, 2958, 2925, 2834, 2808, 2866, 3115, 3216, 3170, 3152, 3066, 2920, 2780, 2664],
#     [2816, 2810, 2829, 2854, 2953, 3030, 3024, 3032, 3024, 2998, 2958, 2925, 2834, 2808, 2866, 3115, 3216, 3170, 3152, 3066, 2920, 2780, 2664, 2611],
#     [2810, 2829, 2854, 2953, 3030, 3024, 3032, 3024, 2998, 2958, 2925, 2834, 2808, 2866, 3115, 3216, 3170, 3152, 3066, 2920, 2780, 2664, 2611, 2587],
#     [2829, 2854, 2953, 3030, 3024, 3032, 3024, 2998, 2958, 2925, 2834, 2808, 2866, 3115, 3216, 3170, 3152, 3066, 2920, 2780, 2664, 2611, 2587, 2619],
#     [],
# ]
#
#
#
# 2910, 2853, 2816, 2810, 2829, 2854, 2953, 3030, 3024, 3032, 3024, 2998, 2958, 2925, 2834, 2808, 2866, 3115, 3216, 3170, 3152, 3066, 2920, 2780, 2664, 2611, 2587, 2619, 2709, 2905, 3140, 3312, 3360, 3422, 3513, 3563, 3614, 3674, 3728, 3755, 3830, 4030, 4173, 4162, 4087, 3993, 3837, 3687, 3553, 3481, 3485, 3494, 3610, 3796, 3983, 4164, 4215, 4147, 4079, 3979, 3891, 3811, 3753, 3695, 3737, 3964, 4139, 4084, 4033, 3954, 3830, 3694, 3531, 3451, 3400, 3395, 3420, 3465, 3516, 3607, 3629, 3626, 3567, 3465, 3387, 3254, 3199, 3144, 3167, 3385, 3543, 3523, 3465, 3385, 3251, 3098, 2930, 2834, 2784, 2731, 2753, 2772, 2833, 2930, 3007, 3114, 3185, 3216, 3263, 3181, 3130, 3155, 3259, 3466, 3509, 3453, 3406, 3297, 3229, 3161, 3137, 3150, 3222, 3300, 3473, 3752, 4075, 4337, 4430, 4472, 4584, 4625, 4625, 4626, 4627, 4646, 4727, 4948, 5105, 5050, 5026, 4926, 4732, 4551, 4469, 4400,
#
#
# list = ['forecast-CNN.py','forecast-LSTM.py','forecast-Encoder-Decoder-LSTM.py','forecast-CNN-LSTM.py','forecast-ConvLSTM.py']
# x = 0
# def run():
#     for i in range(len(list)):
#         p = os.system(list[i])
#         if p == 0:
#             x += 1

# x = '12345'
# b = int(x)
# print(b)

# a = [0,1,2,3,4,5]
# # i = 2
# # h = (i-1)*1
# # a = a[h:h+24]
# a = a[1:5]
# print(a)
x = 0
h = x*24
k = h+24
data_origin = pd.read_csv('LD_MT200_hour.csv', header=0, low_memory=False, infer_datetime_format=True, engine='c',
                          index_col=['date'])
data_origin = data_origin.iloc[h:k]
print(data_origin)
# date = (data_origin.index.map(str) + ' '+data_origin['hour'].map(str)+':00').tolist()
# data_origin.index = pd.to_datetime(data_origin.index) + pd.to_timedelta(data_origin['hour'], unit='h')
data_col = data_origin.columns.tolist()
data = []
for i in range(6):
    data.append(data_origin[data_col[i]].tolist())
data_sum = data_origin.apply(lambda x: sum(x), axis=0).tolist()

# data = data[h:k]
# data_sum = data_sum[h:k]
print(data_col)
print(data)