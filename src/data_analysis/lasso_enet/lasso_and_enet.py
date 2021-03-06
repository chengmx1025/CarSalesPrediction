import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.metrics import r2_score
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split

def main():

    df = pd.read_csv("../../newdata/car_new_data.csv", encoding='GBK')
    dfx = df.drop(['#','car_id','sales'], 1)
    #dfxx = df.loc[:,['car_id','year','month','time']]
    #dfxxx = df.drop(['#','sales','car_id'], 1)
    #dfsc = df[df['car_id']==d_car_id].drop(['sales','#','car_id'],1)

    X = np.array(dfx)
    #X = normalize(X)

    y = []
    for i in range(len(df)):
        y.append(df['sales'][i])
        #if(df['car_id'][i]==d_car_id):
        #    y.append(df['sales'][i])
    y = np.array(y)
    #print(X)
    #print(y)


    '''
    Split the Training Data & Test Data
    '''
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=57)

    print(y_test)

    '''
    lasso
    '''
    alpha = 0.1
    lasso = Lasso(alpha=alpha)

    y_pred_lasso = lasso.fit(X_train, y_train).predict(X_test)
    r2_score_lasso = r2_score(y_test, y_pred_lasso)
    print(lasso)
    print(y_pred_lasso)
    print("r^2 on test data : %f" % r2_score_lasso)


    '''
    enet
    '''
    enet = ElasticNet(alpha=alpha, l1_ratio=0.7)

    y_pred_enet = enet.fit(X_train, y_train).predict(X_test)
    r2_score_enet = r2_score(y_test, y_pred_enet)
    print(enet)
    print(y_pred_enet)
    print("r^2 on test data : %f" % r2_score_enet)


    '''
    plot show
    '''
    '''
    plt.plot(enet.coef_, color='lightgreen', linewidth=2, label='Elastic net coefficients')
    plt.plot(lasso.coef_, color='gold', linewidth=2, label='Lasso coefficients')
    plt.plot(coef, '--', color='navy', label='original coefficients')
    plt.legend(loc='best')
    plt.title("Lasso R^2: %f, Elastic Net R^2: %f" % (r2_score_lasso, r2_score_enet))
    plt.show()
    '''

    '''
    save result into csv file
    '''
    result  = []
    result.append(y_test)
    result.append(y_pred_lasso)
    result.append(y_pred_enet)
    result = np.array(result)

    new_result = np.row_stack((result, X_test.T))
    new_result = new_result.T

    result_df = pd.DataFrame(new_result)
    result_df.to_csv("lasso_enet.csv")


if __name__ == "__main__":
    main()