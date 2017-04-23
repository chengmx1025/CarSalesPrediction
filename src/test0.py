import pandas as pd

df1 = pd.read_csv("../data/Automobile_baiduIndex.csv",encoding='GBK')
df2 = pd.read_csv("../data/carcomment/4Runner.csv",encoding='GBK')

print(df1)
print(df2)
