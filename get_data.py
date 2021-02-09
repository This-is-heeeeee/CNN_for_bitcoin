import argparse
import pandas as pd
import os
import time
from bithumb_api.PublicApi import candlestick
import numpy as np

def main() :
    parser = argparse.ArgumentParser(
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-oc', '--order_currency', type = str, default = 'BTC',
                        help = 'order currency(coin) - BTC, ETH, XRP ...')
    parser.add_argument('-ci', '--chart_intervals', type = str, default = '24h',
                        help = 'chart intervals - 1m, 3m, 5m, 10m, 30m, 1h, 6h, 12h, 24h')

    args = parser.parse_args()

    if not os.path.isdir("coindatas"):
        os.mkdir("coindatas")

    payment_currency = "KRW"
    get_bithumb_data(args.order_currency, payment_currency, args.chart_intervals,
                     "coindatas/{}_".format(args.order_currency))

def get_bithumb_data(order_currency, payment_currency, chart_intervals, fname):
    fname_training = fname+"training.csv"
    fname_testing = fname+"testing.csv"
    
    try :
        if os.path.exists(fname_training) :
            os.remove(fname_training)
        if os.path.exists(fname_testing) :
            os.remove(fname_testing)
        data = candlestick(order_currency, payment_currency, chart_intervals)
        if data['status'] == '0000' :
            data = data['data']
            df = pd.DataFrame(data, columns = ['Time', 'Open', 'Close', 'High', 'Low', 'Volume'])
            df = df.set_index('Time')
            df.index = pd.to_datetime(df.index, unit = 'ms', utc = True)
            df.index = df.index.tz_convert('Asia/Seoul')
            df.index = df.index.tz_localize(None)
            df = df.astype(float)
            train_size = int(len(df)/2)
            _index = df.index[train_size]
            df_training = df.loc[:_index,:]
            df_testing = df.loc[_index:,:]
            df_training.to_csv(fname_training)
            df_testing.to_csv(fname_testing)

    except Exception as e :
        print(f"{type(e).__name__}:{e}")
    

if __name__ == "__main__" :
    main()
