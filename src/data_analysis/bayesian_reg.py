import numpy as np
import pandas as pd

from sklearn.metrics import r2_score

from sklearn.model_selection import train_test_split
from sklearn import gaussian_process

from sklearn import linear_model

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
    mlpr
    '''
    reg = linear_model.BayesianRidge(n_iter=200000)
    reg.fit(X_train, y_train)
    y_pred = reg.predict(X_test)

    print(y_pred)


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
    result.append(y_pred)
    result = np.array(result)

    new_result = np.row_stack((result, X_test.T))
    new_result = new_result.T

    result_df = pd.DataFrame(new_result)
    result_df.to_csv("bayesian.csv")


if __name__ == "__main__":
    main()