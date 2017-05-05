import time
import pandas as pd
import numpy as np
from sklearn.svm import SVR

from sklearn.model_selection import train_test_split

from sklearn import metrics
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_recall_fscore_support



def main():

    '''
    Read Training Data & TestData from csv file
    Get X and y for the SVR model
    '''
    df1 = pd.read_csv("../../newdata/car_train_data.csv",encoding='GBK')
    df2 = pd.read_csv("../../newdata/car_test_data.csv", encoding='GBK')

    df_train = df1.drop(['sales'],1)
    df_test = df2.drop(['sales'],1)

    X_train = np.array(df_train)
    X_test = np.array(df_test)

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

    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
    svr_lin = SVR(kernel='linear', C=1e3)
    svr_poly = SVR(kernel='poly', C=1e3, degree=2)

    print("start time: %s" % time.time())

    '''
    y_rbf = svr_rbf.fit(X_train, y_train).predict(X_test)
    print("y_rbf:")
    print(y_rbf)
    print("finish time: %s" % time.time())


    y_lin = svr_lin.fit(X_train, y_train).predict(X_test)
    print("y_lin:")
    print(y_lin)
    print("finish time: %s" % time.time())
    '''

    y_poly = svr_poly.fit(X_train, y_train).predict(X_test)
    print("y_poly:")
    print(y_poly)
    print("finish time: %s" % time.time())



    '''
    save result
    '''
    result = []
    result.append(y_test)
    result.append(y_rbf1)

    result = np.array(result)
    result = result.T

    resultdf = pd.DataFrame(result)
    resultdf.to_csv("svr_result_output.csv")

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