import os
import argparse
from shutil import move

def main() :
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input',
                        help='a csv file of stock data', required=True)
    parser.add_argument('-lf', '--label_file',
                        help='a label_file')
    args = parser.parse_args()

    img_to_dataset(args.input, args.label_file)
        

def img_to_dataset(input, label_file) :
    label_dict = {}
    with open(label_file) as lf :
        for line in lf :
            (key, val) = line.split(',')
            label_dict[key] = val.rstrip()

    path = "{}/{}".format(os.getcwd(), input)
    print(path)#

    for filename in os.listdir(path):
        if filename is not '':
            for k,v in label_dict.items() :
                f,e = os.path.splitext(filename)
                if f == k :
                    new_name = "{}{}".format(v,filename)

                    os.rename("{}/{}".format(path, filename),
                              "{}/{}".format(path, new_name))
                    break

    folders = ['1', '0']

    for folder in folders:
        if not os.path.exists("{}/classes/{}".format(path, folder)):
            os.makedirs("{}/classes/{}".format(path,folder))

    for filename in os.listdir(path) :
        if filename is not '' :
            if filename[0] == "1" :
                move("{}/{}".format(path, filename),
                     "{}/classes/1/{}".format(path, filename))
            elif filename[0] == "0" :
                move("{}/{}".format(path, filename),
                     "{}/classes/0/{}".format(path, filename))

if __name__ == '__main__' :
    main()
