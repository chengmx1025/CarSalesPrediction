import numpy as np
import pandas as pd

from sklearn.metrics import r2_score
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split

def main():

    df1 = pd.read_csv("train_data.csv")
    df2 = pd.read_csv("test_data.csv")
    df3 = pd.read_csv("normalize.csv")

    df_train = df1.drop(['sales','car_id'],1)
    df_test = df2.drop(['sales','car_id'],1)

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

    print(X_train)
    print(X_test)
    print(y_train)
    print(y_test)

    print(len(X_train))
    print(len(X_test))
    print(len(y_train))
    print(len(y_test))

    '''
    lasso
    '''
    alpha = 0.1
    lasso = Lasso(alpha=alpha)

    y_pred_lasso = lasso.fit(X_train, y_train).predict(X_test)
    print(lasso)
    print(y_pred_lasso)


    '''
    enet
    '''
    enet = ElasticNet(alpha=alpha, l1_ratio=0.7)

    y_pred_enet = enet.fit(X_train, y_train).predict(X_test)
    print(enet)
    print(y_pred_enet)


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

    result = []
    result.append(y_test)
    result.append(y_pred_lasso)
    result.append(y_pred_enet)
    result = np.array(result)
    result = result.T

    result_df = pd.DataFrame(result)
    result_df.to_csv("lasso_enet.csv")



if __name__ == "__main__":
    main()