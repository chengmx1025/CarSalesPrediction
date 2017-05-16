import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

from sklearn.preprocessing import normalize


def main():

    norm = pd.read_csv('normalize.csv', encoding='GBK')

    df = pd.read_csv("train_data.csv", encoding='GBK')

    df = pd.merge(norm, df, on='car_id')

    df = process(df)

    dfx = df.drop(['sales', 'mean', 'max', 'min'], 1)

    feature_count = len(dfx.columns)
    sample_count = dfx.shape[0]
    x = np.matrix(dfx)
    x.reshape(sample_count, feature_count)

    dfy = df.sales
    y = np.array(dfy)
    y.reshape(sample_count, 1)

    '''
    Model Training
    '''
    linear = LinearRegression().fit(x, y)
    # m = linear.coef_
    #
    test = pd.read_csv("test_data.csv", encoding='GBK')
    test = pd.merge(test, norm, on='car_id')

    test = process(test)

    test_x = test.drop(['sales', 'mean', 'max', 'min'], 1)
    predict = linear.predict(test_x)

    actual = test.sales

    test['predict'] = predict
    test.predict = test.predict * (test['max'] - test['min']) + test['mean']

    dif = (predict - actual)

    act_dif = test.predict - test.sales
    mean_square = np.mean(act_dif * act_dif)


    new = (dif * 10).round(0).to_frame()

    print mean_square
    fig = plt.figure()
    fig.set(alpha=0.2)
    uAcc = new[new['sales']<-2].shape[0] + new[new['sales']>2].shape[0]
    print 1- float(uAcc)/new.shape[0]
    new.groupby('sales').sales.count().plot(kind='bar', x='dif')
    plt.show()


def normalization():
    df = pd.read_csv("train_data.csv", encoding='GBK')
    sales = df.loc[:, ['car_id', 'sales']]

    mean = pd.DataFrame(sales.groupby('car_id').sales.mean())
    min = pd.DataFrame(sales.groupby('car_id').sales.min())
    max = pd.DataFrame(sales.groupby('car_id').sales.max())
    mean['car_id'] = mean.index
    min['car_id'] = min.index
    max['car_id'] = max.index
    mean.rename(columns={'sales': 'mean'}, inplace=True)
    min.rename(columns={'sales': 'min'}, inplace=True)
    max.rename(columns={'sales': 'max'}, inplace=True)
    result = pd.merge(mean, min, on='car_id')
    result = pd.merge(result, max, on='car_id')
    result.to_csv('normalize.csv', encoding='GBK')


def process(dataframe):
    dataframe.sales = (dataframe.sales - dataframe['mean']) / (dataframe['max'] - dataframe['min'])
    dataframe.fillna(0, inplace=True)
    dataframe.replace(np.inf, 0, inplace=True)
    dataframe.replace(-np.inf, 0, inplace=True)

    dataframe.min_price = normalize(dataframe.min_price)[0]
    dataframe.max_price = normalize(dataframe.max_price)[0]

    return dataframe

if __name__ == "__main__":
    main()
    # normalize()
