import pandas as pd
import matplotlib.pyplot as plt

# df= pd.read_csv("metropolitondata.csv")
# x=df.income
# plt.hist(x)
# plt.show()

df1={'Name': pd.Series([5, 17, 23, 31, 43, 49, 57, 17, 57, 17])}
df2=pd.DataFrame(df1)
print(df2.mode())