fare_data = df[["fare"]]

print(fare_data.info())

print("-------------------------------")

print(fare_data.count())

print("-------------------------------")

print(fare_data.sum(skipna = False))

print("-------------------------------")

print(fare_data.unique())

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 1 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   fare    891 non-null    float64
dtypes: float64(1)
memory usage: 7.1 KB
None
-------------------------------
fare    891
dtype: int64
-------------------------------
fare    28693.9493
dtype: float64
"""
