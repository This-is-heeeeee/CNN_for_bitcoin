import subprocess
import os
import sys

formatters = {
    'RED' : '\033[91m',
    'GREEN' : '\033[92m',
    'END' : '\033[0m'
    }

order_currency = sys.argv[1]
chart_intervals = sys.argv[2]
windows_length = sys.argv[3]
dimension = sys.argv[4]

try :
    print('{RED}\nGet Training/Testing Data{END}'.format(**formatters))
    subprocess.call(
        f'python get_data.py -oc {order_currency} -ci {chart_intervals}',shell = True)
    print('{GREEN}Get Training/Testing Data Done\n{END}'.format(**formatters))

except Exception as identifier:
    print(identifier)

try :
    print('{RED}\nCreate Label Training Data{END}'.format(**formatters))
    subprocess.call(
        f'python createLabel.py -i coindatas/{order_currency}_training.csv -l {windows_length}', shell = True)
    print('{GREEN}Create Label Training Data Done\n{END}'.format(**formatters))

    print('{RED}\nCreate Label Testing Data{END}'.format(**formatters))
    subprocess.call(
        f'python createLabel.py -i coindatas/{order_currency}_testing.csv -l {windows_length}', shell = True)
    print('{GREEN}Create Label Testing Data Done\n{END}'.format(**formatters))

except Exception as identifier:
    print(identifier)

try :
    print('{RED}\nConvert Training Data to Candlestick img{END}'.format(**formatters))
    subprocess.call(
        f'python data_to_img.py -i coindatas/{order_currency}_training.csv -l {windows_length} -d {dimension} -t training', shell = True)
    print('{GREEN}Convert Training Data to Candlestick img Done\n{END}'.format(**formatters))

    print('{RED}\nConvert Testing Data to Candlestick img{END}'.format(**formatters))
    subprocess.call(
        f'python data_to_img.py -i coindatas/{order_currency}_testing.csv -l {windows_length} -d {dimension} -t testing', shell = True)
    print('{GREEN}Convert Testing Data to Candlestick img Done\n{END}'.format(**formatters))

except Exception as identifier:
    print(identifier)

try :
    print('{RED}\nLabelling Training Dataset{END}'.format(**formatters))
    subprocess.call(
        f'python img_to_dataset.py -i dataset/{windows_length}_{dimension}/{order_currency}/training -lf {order_currency}_training_label_{windows_length}.txt', shell = True)
    print('{GREEN}CLabelling Training Dataset Done\n{END}'.format(**formatters)) 

    print('{RED}\nLabelling Testing Dataset{END}'.format(**formatters))
    subprocess.call(
        f'python img_to_dataset.py -i dataset/{windows_length}_{dimension}/{order_currency}/testing -lf {order_currency}_testing_label_{windows_length}.txt', shell = True)
    print('{GREEN}Labelling Testing Dataset Done\n{END}'.format(**formatters))

except Exception as identifier:
    print(identifier)
    
