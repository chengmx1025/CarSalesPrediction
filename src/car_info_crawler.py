import re
import urllib.request
import codecs

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

    output_file = codecs.open("../outputs/car_info.txt", "w", "GBK")
    output_file.write("#; car_name; price; structure; emission; gearbox; fc;\n")

    car_num = -1
    for each_car_name in list_car_names:
        car_name = each_car_name

        car_name_gbk = car_name.encode('GBK')
        newstr = ""
        for x in car_name_gbk:
            newstr += hex(x)
        str_re = re.compile('0x')
        car_name_url = str_re.sub('%',newstr)
        #print(car_name_url)

        url = "http://sou.autohome.com.cn/zonghe?q="+car_name_url+"&entry==1"
        #print(url)
        data = urllib.request.urlopen(url).read().decode('GBK')
        #print(data)

        '''
        price - 指导价
        structure - 车身结构
        emission - 排量
        gearbox - 变速箱
        fc(fuel consumption) - 油耗
        '''

        car = []
        car_num += 1
        car.append(str(car_num))

        car.append(car_name)

        car_price_re = re.search(r'<td>指导价：(.*?)</td>', data)
        car_structure_re = re.search(r'<td>车身结构：(.*?)</td>', data)
        car_emission_re = re.search(r'<td>排量：(.*?)</td>', data)
        car_gearbox_re = re.search(r'<td>变速箱：(.*?)</td>', data)
        car_fc_re = re.search(r'<td>油耗：(.*?)</td>', data)

        if car_price_re:
            car_price = car_price_re.group(1)
            car.append(car_price)
        else:
            car.append("null_price")

        if car_structure_re:
            car_structure = car_structure_re.group(1)
            car.append(car_structure)
        else:
            car.append("null_structure")

        if car_emission_re:
            car_emission = car_emission_re.group(1)
            car.append(car_emission)
        else:
            car.append("null_emission")

        if car_gearbox_re:
            car_gearbox = car_gearbox_re.group(1)
            car.append(car_gearbox)
        else:
            car.append("null_gb")

        if car_fc_re:
            car_fc = car_fc_re.group(1)
            car.append(car_fc)
        else:
            car.append("null_fc")

        print(car)

        for each_car_item in car:
            output_file.write(each_car_item + ";")
        output_file.write("\n")

    output_file.close()

if __name__ == "__main__":
    main()