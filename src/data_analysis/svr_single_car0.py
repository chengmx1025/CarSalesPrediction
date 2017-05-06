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
    '''
    df1 = pd.read_csv("../../newdata/train_new.csv",encoding='GBK')
    df2 = pd.read_csv("../../newdata/test_new.csv", encoding='GBK')

    df_train = df1.drop(['sales'],1)
    df_test = df2.drop(['sales'],1)

    X_train = np.array(df_train)
    X_test = np.array(df_test)

    #normalize(X_train)
    #normalize(X_test)

    y_train = []
    for i in range(len(df1)):
        y_train.append(df1['sales'][i])
    y_train = np.array(y_train)

    y_test = []
    for i in range(len(df2)):
        y_test.append(df2['sales'][i])
    y_test = np.array(y_test)

    print(X_train)
    print(X_test)
    print(y_train)
    print(y_test)
    '''

    d_car_id = 2

    df = pd.read_csv("../../newdata/car_new_data.csv", encoding='GBK')
    #dfx = df.drop(['#','sales','year','month'], 1)
    #dfxx = df.loc[:,['car_id','year','month','time']]
    #dfxxx = df.drop(['#','sales','car_id'], 1)

    dfsc = df[df['car_id']==d_car_id].drop(['sales','#','car_id'],1)

    X = np.array(dfsc)
    #X = normalize(X)

    y = []
    for i in range(len(df)):
        if(df['car_id'][i]==d_car_id):
            y.append(df['sales'][i])
    y = np.array(y)
    #print(X)
    #print(y)


    '''
    Split the Training Data & Test Data
    '''
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=57)

    print(X_train)
    print(X_test)
    print(y_train)
    print(y_test)


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
    result_df.to_csv("svr_single0.csv")

    '''
    Model Evaluation
    '''
    '''
    y_true = y_test
    y_pred = y_rbf

    score_1 = metrics.precision_score(y_true, y_pred)
    score_2 = metrics.recall_score(y_true, y_pred)
    score_3 = metrics.f1_score(y_true, y_pred)
    score_4 = metrics.fbeta_score(y_true, y_pred, beta=0.5)
    score_5 = metrics.fbeta_score(y_true, y_pred, beta=1)
    score_6 = metrics.fbeta_score(y_true, y_pred, beta=2)
    score_7 = precision_recall_fscore_support(y_true, y_pred)

    print(score_1)
    print(score_2)
    print(score_3)
    print(score_4)
    print(score_5)
    print(score_6)
    print(score_7)
    '''

    '''
    Measure the score
    precision, recall, threshold
    '''
    '''
    precision, recall, threshold = precision_recall_curve(y_true, y_scores)
    average_precision_score(y_true, y_scores)

    print("Precision:")
    print(precision)

    print("Recall:")
    print(recall)

    print("threshold")
    print(threshold)

    print("average_precision_score")
    print(average_precision_score)
    '''

if __name__ == "__main__":
    main()