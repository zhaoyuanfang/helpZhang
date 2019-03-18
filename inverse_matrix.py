import pandas as pd
import numpy as np

print('reading')
K_left = pd.read_csv('./K_left.csv',header=None)
K_left_array = np.array(K_left)
hc = pd.read_csv('./hc.csv',header=None)
hc_array = np.array(hc)

print('计算ing')
K = np.matmul(hc_array.transpose(),K_left_array)
K = np.matmul(K, hc_array)
'''
从矩阵取部分行、列
先取行，后从行里取列
'''
kaa = K[252:]
kaa = kaa[:,252:]

ktt = K[126:252]
ktt = ktt[:,126:252]

kta = K[126:252]
kta = kta[:,252:]

kat = K[252:]
kat = kat[:,126:252]

print('计算ing')
'''
矩阵乘法
'''
K1 = np.matmul(np.linalg.inv(kaa),kat)
K2 = np.matmul(np.linalg.inv(kta),ktt)
K_ = np.linalg.inv(K1 - K2)
print('存ing')
'''
存入文件
'''
df_k = pd.DataFrame(K_)
df_k.to_csv('./k1.csv',header=None,index=None)