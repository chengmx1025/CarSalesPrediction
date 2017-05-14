import os
import codecs
import pandas as pd

def listFilesToTxt(dir, output_file):
    files = os.listdir(dir)
    for name in files:
        names = name.split('.')
        #print(names[0])
        output_file.write(names[0]+'\n')

def list_car_comment():
    dir = "../data/carcomment"
    outfile = "../outputs/car_names_cc.txt"

    output_file = codecs.open(outfile, "w", "GBK")
    if not output_file:
        print ("cannot open the file %s for writing" % outfile)
    listFilesToTxt(dir, output_file)

    output_file.close()

def list_car_comment_new():
    dir = "../newdata/carcomment"
    outfile = "../outputs/car_names_cc.txt"

    output_file = codecs.open(outfile, "w", "GBK")
    if not output_file:
        print ("cannot open the file %s for writing" % outfile)
    listFilesToTxt(dir, output_file)

    output_file.close()

def list_bdi_and_sales():
    df_baidu = pd.read_csv("../data/Automobile_baiduIndex.csv", encoding='GBK')
    df_sales = pd.read_csv("../data/Automobile_sales.csv", encoding='GBK')

    output_file = codecs.open("../outputs/car_names_bdIndex.txt", "w", "GBK")
    df_name = df_baidu['name'].drop_duplicates()
    for each_name in df_name:
        output_file.write(each_name + "\n")
    output_file.close()

    output_file = codecs.open("../outputs/car_names_sales.txt", "w", "GBK")
    df_name = df_sales['name'].drop_duplicates()
    for each_name in df_name:
        output_file.writelines(each_name + "\n")
    output_file.close()

def main():
    #list_car_comment()
    list_bdi_and_sales()
    list_car_comment_new()

if __name__ == "__main__":
    main()