import pandas as pd
import codecs

df_baidu = pd.read_csv("../data/Automobile_baiduIndex.csv",encoding='GBK')
df_sales = pd.read_csv("../data/Automobile_sales.csv",encoding='GBK')
df_car1 = pd.read_csv("../data/carcomment/3 Wheeler.csv",encoding='GBK')

#print(df_baidu)
#print(df_sales)
#print(df_car1)

output_file = codecs.open("../outputs/car_names_bdIndex.txt", "w","GBK")
df_name = df_baidu['name'].drop_duplicates()
for each_name in df_name:
    #print(each_name)
    output_file.write(each_name)
    output_file.write("\n")
output_file.close()

output_file = codecs.open("../outputs/car_names_sales.txt", "w","GBK")
df_name = df_sales['name'].drop_duplicates()
for each_name in df_name:
    #print(each_name)
    output_file.write(each_name)
    output_file.write("\n")
output_file.close()

