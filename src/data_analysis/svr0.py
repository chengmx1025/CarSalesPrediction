import pandas as pd
import numpy as np

def main():
    df1 = pd.read_csv("../../newdata/car_info_newest.csv",encoding='GBK')
    df1 = df1.drop('car_name',1)
    #print(df1)

    df2 = pd.read_csv("../../newdata/car_sales_new.csv",encoding='GBK')
    #print(df2)

    df3 = pd.merge(df1,df2,left_on=['car_id'], right_on=['car_id'])
    #print(df3)
    #df3.to_csv("car_svr.csv")

    df4 = df3.drop('data_value',1)
    X = np.array(df4)
    print(X)

    y = []
    for i in range(len(df3)):
        y.append(df3['data_value'][i])
    print(y)


if __name__ == "__main__":
    main()