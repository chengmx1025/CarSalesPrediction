import pandas as pd
import codecs

def main():

    '''
    Read csv files: (encoding='GBK') 
    '''
    df_baidu = pd.read_csv("../data/Automobile_baiduIndex.csv",encoding='GBK')
    df_sales = pd.read_csv("../data/Automobile_sales.csv",encoding='GBK')
    df_car1 = pd.read_csv("../data/carcomment/3 Wheeler.csv",encoding='GBK')
    #print(df_baidu)
    #print(df_sales)
    #print(df_car1)

    '''
     each car's bdIndex
    '''
    #t0 = df_baidu[df_baidu['name']=="丰田凯美瑞"]
    #print(t0)

    '''
    Use groupby() to see 
    '''
    #t1 = df_baidu.groupby('name').sum()
    #print(t1)


    '''
    cc
    '''

    t2 = df_car1
    print(t2)
    print(len(t2))

if __name__ == "__main__":
    main()