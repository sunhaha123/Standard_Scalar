# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn import  preprocessing
data1=pd.read_excel('motion_data.xlsx',sheet_name='Sheet1')



#归一化[0,1]  x' = (x - X_min) / (X_max - X_min)
data2=data1.iloc[:,6:].apply(lambda x: (x - np.min(x)) / (np.max(x)-np.min(x))).fillna(0)
data3=data1.iloc[:,:6]
data4=pd.concat([data3,data2],axis=1)

#均值归一化[0,1]  x' = (x - X_mea) / (X_max - X_min)
#data2=data1.iloc[:,6:].apply(lambda x: (x - np.min(x)) / (np.max(x)-np.min(x))).fillna(0)
#data3=data1.iloc[:,:6]
#data4=pd.concat([data3,data2],axis=1)

#data4.to_excel('motion_data3.xlsx',index=False) 
#
#ss=preprocessing.StandardScaler()
#data22=ss.fit_transform(data1.iloc[:,6:])
#    
#标准化
from sklearn import preprocessing
scaler1 = preprocessing.StandardScaler().fit(data1.iloc[:,6:])
df1 = scaler1.transform(data1.iloc[:,6:])
df1 = pd.DataFrame(df1)


#归一化[0,1]  x' = (x - X_min) / (X_max - X_min)
from sklearn import preprocessing
scaler2 = preprocessing.MinMaxScaler().fit(data1.iloc[:,6:])
df2 = scaler2.transform(data1.iloc[:,6:])
df2 = pd.DataFrame(df2)

#归一化[-1,1]
from sklearn import preprocessing
scaler3 = preprocessing.MaxAbsScaler().fit(data1.iloc[:,6:])
df3 = scaler3.transform(data1.iloc[:,6:])
df3 = pd.DataFrame(df3)