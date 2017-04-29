import pandas as pd

def main():

    '''
    Read csv files: (encoding='GBK') 
    '''
    df = pd.read_csv("../outputs/car_info_new.csv",encoding='GBK')
    print(df)

    df2 = pd.read_csv("../outputs/car_comment_output.txt",encoding='GBK')
    print(df2)



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


if __name__ == "__main__":
    main()