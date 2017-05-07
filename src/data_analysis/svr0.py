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
    Read Data from csv file
    Get X and y for the SVR model
    '''
    df1 = pd.read_csv("../../newdata/car_info_newest.csv",encoding='GBK')
    df1 = df1.drop('car_name',1)
    #print(df1)
    df2 = pd.read_csv("../../newdata/car_sales_new.csv",encoding='GBK')
    #print(df2)
    df3 = pd.merge(df1,df2,left_on=['car_id'], right_on=['car_id'])
    #print(df3)
    df3.to_csv("car_svr.csv")
    df4 = df3.drop('data_value',1)
    X = np.array(df4)
    #print(X)
    y = []
    for i in range(len(df3)):
        y.append(df3['data_value'][i])
    y = np.array(y)
    #print(y)


    '''
    Split the Training Data & Test Data
    '''
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


    '''
    SVR Model Training
    '''
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
    svr_lin = SVR(kernel='linear', C=1e3)
    svr_poly = SVR(kernel='poly', C=1e3, degree=2)

    print("y_true:")
    print(y_test)

    y_rbf = svr_rbf.fit(X_train, y_train).predict(X_test)
    print("y_rbf:")
    print(y_rbf)

    y_lin = svr_lin.fit(X_train, y_train).predict(X_test)
    print("y_lin:")
    print(y_lin)

    y_poly = svr_poly.fit(X_train, y_train).predict(X_test)
    print("y_poly:")
    print(y_poly)

    '''
    save result
    '''
    result  = []
    result.append(y_test)
    result.append(y_rbf)
    result.append(y_lin)
    result.append(y_poly)

    result = np.array(result)
    result = result.T

    resultdf = pd.DataFrame(result)
    resultdf.to_csv("svr_result.csv")

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