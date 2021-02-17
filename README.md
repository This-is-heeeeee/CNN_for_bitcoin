# CNN for Bitcoin Market Prediction

Predict the Bitcoin price will go up or not at the next candlestick

## Usage

### Prepare Dataset
"""
python preprocess_data.py {order_currency} {chart_intervals} {windows} {dimension}
python generatedata.py {root} {original_dir} {destination_dir}
"""
ex
"""
python preprocess_data.py BTC 24h 20 50
python generatedata.py dataset 20_50/BTC dataset_BTC_20_50
"""

### Remove alpha channel
"""
cd /dataset/dataset_BTC_20_50
find . -name "*.png" -exec convert "{}" -alpha off "{}" \;
"""

### Training
"""
python CNN.py -i {datasetdir} -e {epoch} -d {dimension} -b {batchsize} -o {result_report}
"""
ex
"""
python CNN.py -i dataset/dataset_BTC_20_50 -e 50 -d 50 -b 8 -o 20_50_result.txt
"""


