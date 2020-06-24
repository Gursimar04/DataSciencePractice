import pandas as pd
import numpy as np
A = ['1','2','3','4','2']
B = ['C++','Python','Java','C','Python']
d = {'numeric': A, 'categorical': B}
df = pd.DataFrame(d)
df['categorical'] = pd.Categorical(df['categorical'])
dfDummies = pd.get_dummies(df['categorical'], prefix = 'category')
df = pd.concat([df, dfDummies], axis=1)
print(df)