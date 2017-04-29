import pandas as pd

def main():

    '''
    Read csv files: (encoding='GBK') 
    '''
    df = pd.read_csv("../outputs/car_info_new.csv",encoding='GBK')
    df = df.drop('#',1)
    #print(df)

    df2 = pd.read_csv("../outputs/car_comment_output.txt",encoding='GBK')
    df2 = df2.drop('nan',1)
    #print(df2)

    #print(df.info(),df2.info())

    df3 = pd.merge(df,df2,left_on=['car_name'], right_on=['car_name'])
    print(df3)

    df3.to_csv("car_info_2.csv",encoding='gbk')


if __name__ == "__main__":
    main()