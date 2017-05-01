import pandas as pd

df = pd.read_csv("../outputs/emi2.csv", encoding='GBK')

#print(df)
print(df.axes)

for x in range(len(df)):

    emission1 = df['emission1'][x]
    e_str_1 = str(emission1)
    if (e_str_1 != 'nan'):
        df.loc[x:x, (emission1)] = 1
        print(emission1)

    emission2 = df['emission2'][x]
    e_str_2 = str(emission2)
    if (e_str_2 != 'nan'):
        df.loc[x:x, (emission2)] = 1
        print(emission2)

    emission3 = df['emission3'][x]
    e_str_3 = str(emission3)
    if (e_str_3 != 'nan'):
        df.loc[x:x, (emission3)] = 1
        print(emission3)

    emission4 = df['emission4'][x]
    e_str_4 = str(emission4)
    if (e_str_4 != 'nan'):
        df.loc[x:x, (emission4)] = 1
        print(emission4)

    print("====")

#print(df)

df.drop(['emission1','emission2','emission3','emission4'],1)

df.to_csv("../outputs/emi_new.csv")
