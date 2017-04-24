import os
import codecs

def ListFilesToTxt(dir, output_file):
    files = os.listdir(dir)
    for name in files:
        names = name.split('.')
        #print(names[0])
        output_file.write(names[0]+'\n')


def main():
    dir = "../data/carcomment"
    outfile = "../outputs/car_names_cc.txt"

    output_file = codecs.open(outfile, "w", "GBK")
    if not output_file:
        print ("cannot open the file %s for writing" % outfile)
    ListFilesToTxt(dir, output_file)

    output_file.close()

if __name__ == "__main__":
    main()