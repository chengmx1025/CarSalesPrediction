import time
import pandas as pd
import numpy as np
from sklearn.svm import SVR

from sklearn.model_selection import train_test_split

from sklearn import metrics
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_recall_fscore_support

from sklearn.preprocessing import normalize

def main():

    '''
    Read Data from csv file
    Get X and y for the SVR model
    '''

    df1 = pd.read_csv("train_data.csv",encoding='GBK')
    df2 = pd.read_csv("test_data.csv", encoding='GBK')
    df3 = pd.read_csv("normalize.csv")

    df_train = df1.drop(['sales'],1)
    df_test = df2.drop(['sales'],1)

    X_train = np.array(df_train)
    X_test = np.array(df_test)

    #normalize(X_train)
    #normalize(X_test)

    df4 = pd.merge(df1,df3,left_on=['car_id'], right_on=['car_id'])
    #print(df4)
    y_train = []
    for i in range(len(df4)):
        if df4['max'][i] == df4['min'][i]:
            my_sales = 0
        else:
            my_sales = (df4['sales'][i] - df4['mean'][i]) / (df4['max'][i] - df4['min'][i])
        y_train.append(my_sales)
        #print(my_sales)
    y_train = np.array(y_train)

    df5 = pd.merge(df2, df3, left_on=['car_id'], right_on=['car_id'])
    #print(df5)
    y_test = []
    for i in range(len(df5)):
        my_sales = (df5['sales'][i] - df5['mean'][i]) / (df5['max'][i] - df5['min'][i])
        y_test.append(my_sales)
        #print(my_sales)
    y_test = np.array(y_test)

    #print(X_train)
    #print(X_test)
    #print(y_train)
    #print(y_test)


    '''
    df = pd.read_csv("../../newdata/car_new_data.csv", encoding='GBK')
    dfx = df.drop(['#','sales','year','month'], 1)
    dfxx = df.loc[:,['car_id','year','month','time']]
    dfxxx = df.drop(['#','sales','car_id'], 1)
    X = np.array(dfxxx)
    #X = normalize(X)

    y = []
    for i in range(len(df)):
        y.append(df['sales'][i])
    y = np.array(y)
    #print(X)
    #print(y)


    #Split the Training Data & Test Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=57)

    print(X_train)
    print(X_test)
    print(y_train)
    print(y_test)
    '''

    '''
    SVR Model Training
    '''
    svr_rbf1 = SVR(kernel='rbf', C=1e3, gamma=0.1)
    svr_rbf2 = SVR(kernel='rbf', C=1e4, gamma=0.1)
    svr_rbf3 = SVR(kernel='rbf', C=1e3, gamma=0.01)
    svr_lin = SVR(kernel='linear', C=1e3)
    svr_poly = SVR(kernel='poly', C=1e3, degree=2)

    print(time.time())
    print("y_true:")
    print(y_test)

    y_rbf1 = svr_rbf1.fit(X_train, y_train).predict(X_test)
    print(time.time())
    print("y_rbf1:")
    print(y_rbf1)

    y_rbf2 = svr_rbf2.fit(X_train, y_train).predict(X_test)
    print(time.time())
    print("y_rbf2:")
    print(y_rbf2)

    y_rbf3 = svr_rbf3.fit(X_train, y_train).predict(X_test)
    print(time.time())
    print("y_rbf3:")
    print(y_rbf3)

    y_lin = svr_lin.fit(X_train, y_train).predict(X_test)
    print(time.time())
    print("y_lin:")
    print(y_lin)

    y_poly = svr_poly.fit(X_train, y_train).predict(X_test)
    print(time.time())
    print("y_poly:")
    print(y_poly)


    '''
    save result into csv file
    '''
    result  = []
    result.append(y_test)
    result.append(y_rbf1)
    result.append(y_rbf2)
    result.append(y_rbf3)
    result.append(y_lin)
    result.append(y_poly)

    result = np.array(result)

    new_result = np.row_stack((result, X_test.T))

    new_result = new_result.T

    result_df = pd.DataFrame(new_result)
    result_df.to_csv("svr_model_result.csv")



if __name__ == "__main__":
    main()