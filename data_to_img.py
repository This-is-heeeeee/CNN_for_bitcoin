import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec
import mplfinance as mpf
import os
import argparse

def main() :
    parser = argparse.ArgumentParser(
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input', help = 'a csv file of data', required = True)
    parser.add_argument('-l', '--seq_len', help = 'num of sequence length', default = 20)
    parser.add_argument('-d', '--dimension', help = 'a dimension value', type = int, default = 48)
    parser.add_argument('-t', '--dataset_type', help = 'training or testing datasets')
    args = parser.parse_args()

    make_candlechart(args.input, args.seq_len, args.dataset_type, args.dimension)

def make_candlechart(fname, seq_len, dataset_type, dimension) :
    path = "{}".format(os.getcwd())

    symbol = fname.split('_')[0]
    symbol = symbol.split('/')[1]#BTC

    if not os.path.exists("{}/dataset/{}_{}/{}/{}".format(path,seq_len,dimension,symbol,dataset_type)) :
        os.makedirs("{}/dataset/{}_{}/{}/{}".format(path,seq_len,dimension,symbol,dataset_type))

    df = pd.read_csv(fname, parse_dates = True, index_col=0)
    df.fillna(0)
    #df.reset_index(inplace = True)

    mc = mpf.make_marketcolors(up = 'tab:red', down = 'tab:blue', edge = 'inherit')
    myStyle = mpf.make_mpf_style(marketcolors = mc)

    plt.style.use('dark_background')

    for i in range(0, len(df)) :
        c = df.iloc[i : i + int(seq_len), :]
        if len(c) == int(seq_len) :
            imgfile = "dataset/{}_{}/{}/{}/{}-{}.png".format(seq_len,dimension,symbol,dataset_type,fname[10:-4],i)
            mydpi = 96
            """
            mpf.plot(c,type = 'candle', volume = True, figscale = 2.0,
                     figsize=((dimension+1)/mydpi,(dimension+1)/mydpi), style = myStyle,
                     savefig = dict(fname = imgfile,dpi = mydpi,pad_inches=0),
                     axisoff = True)#mav = (5,20,30,60)
            """
            fig = plt.figure(figsize=(dimension/mydpi,dimension/mydpi), dpi = mydpi)
            spec = gridspec.GridSpec(ncols = 1, nrows = 2, height_ratios = [2,1])
            ax1 = fig.add_subplot(spec[0])
            ax1.grid(False)
            ax1.set_xticklabels([])
            ax1.set_yticklabels([])
            ax1.xaxis.set_visible(False)
            ax1.yaxis.set_visible(False)
            ax1.axis('off')
            
            ax2 = fig.add_subplot(spec[1])
            ax2.grid(False)
            ax2.set_xticklabels([])
            ax2.set_yticklabels([])
            ax2.xaxis.set_visible(False)
            ax2.yaxis.set_visible(False)
            ax2.axis('off')
            
            mpf.plot(c,type='candle', ax = ax1, volume = ax2, style = myStyle)
            fig.savefig(imgfile, pad_inches = 0, transparent=False)
            plt.close(fig)
if __name__ == "__main__" :
    main()
