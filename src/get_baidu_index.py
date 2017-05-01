import codecs
import pandas as pd
import os

def getCarNames():
    list_car_names = []
    f = open("../outputs/car_names_sales.txt", encoding='GBK')  # 返回一个文件对象
    lines = f.readlines()  # 调用文件的 readline()方法
    for eachLine in lines:
        list_car_names.append(eachLine[:-1])
    #print(list_car_names)
    return list_car_names


def main():

    list_car_names = getCarNames()

    output_file = codecs.open("../outputs/car_comment_output.txt", "w", "GBK")
    output_file.write("car_name, bdi_num,\n")

    num = 0
    for each_car_name in list_car_names:
        cc_input_csv_file = "../newdata/carcomment/" + each_car_name + ".csv"
        print(cc_input_csv_file)

        if(os.path.exists(cc_input_csv_file)):
            df_car = pd.read_csv(cc_input_csv_file, encoding='GBK')

            car = []
            #car.append(str(num))
            car.append(each_car_name)

            print(df_car)

            car.append(str(len(df_car)))

            print(car)
            print("==========")

            for each_car_item in car:
                output_file.write(each_car_item + ",")
            output_file.write("\n")

            num += 1
        else:
            output_file.write("" + each_car_name + ",null,\n")

    output_file.close()

if __name__ == "__main__":
    main()