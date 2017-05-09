import numpy as np
import pandas as pd


from sklearn.metrics import r2_score

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor

def main():
    df1 = pd.read_csv("train_data.csv")
    df2 = pd.read_csv("test_data.csv")
    df3 = pd.read_csv("normalize.csv")

    df_train = df1.drop(['sales', 'car_id'], 1)
    df_test = df2.drop(['sales', 'car_id'], 1)

    X_train = np.array(df_train)
    X_test = np.array(df_test)

    # normalize(X_train)
    # normalize(X_test)

    df4 = pd.merge(df1, df3, left_on=['car_id'], right_on=['car_id'])
    # print(df4)
    y_train = []
    for i in range(len(df4)):
        if df4['max'][i] == df4['min'][i]:
            my_sales = 0
        else:
            my_sales = (df4['sales'][i] - df4['mean'][i]) / (df4['max'][i] - df4['min'][i])
        y_train.append(my_sales)
        # print(my_sales)
    y_train = np.array(y_train)

    df5 = pd.merge(df2, df3, left_on=['car_id'], right_on=['car_id'])
    # print(df5)
    y_test = []
    for i in range(len(df5)):
        my_sales = (df5['sales'][i] - df5['mean'][i]) / (df5['max'][i] - df5['min'][i])
        y_test.append(my_sales)
        # print(my_sales)
    y_test = np.array(y_test)

    #print(X_train)
    #print(X_test)
    #print(y_train)
    print(y_test)

    '''
    mlpr
    '''
    mlpr = MLPRegressor(hidden_layer_sizes=100000,max_iter=100000)
    y_mlpr = mlpr.fit(X_train, y_train).predict(X_test)
    print(y_mlpr)


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
    reverse_normalize
    '''

    y_test_r = []
    y_mlpr_r = []

    for i in range(len(y_mlpr)):
        y_test_r.append(df5['sales'][i])

        if(y_mlpr[i]==0):
            y_mlpr_i = df5['sales'][i]
        else:
            y_mlpr_i = y_mlpr[i]*(df5['max'][i] - df5['min'][i]) + df5['mean'][i]
        y_mlpr_r.append(y_mlpr_i)



    '''
    save result into csv file
    '''
    result  = []
    result.append(y_test)
    result.append(y_mlpr)
    result.append(y_test_r)
    result.append(y_mlpr_r)
    result = np.array(result)
    result = result.T

    #new_result = np.row_stack((result, X_test.T))
    #new_result = new_result.T

    result_df = pd.DataFrame(result)
    result_df.to_csv("neural_network_model33.csv")


if __name__ == "__main__":
    main()