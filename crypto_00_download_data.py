import ssl
import os
import urllib.request

import config

url = "https://www.cryptodatadownload.com/cdd/Binance_BTCUSDT_minute.csv"
filename = config.FOLDERNAME + '/' + config.FILENAME

if not os.path.exists(config.FOLDERNAME):
    os.makedirs(config.FOLDERNAME)

print('Please be patient, downloading 130MB ...')
ssl._create_default_https_context = ssl._create_unverified_context
urllib.request.urlretrieve(url, filename)
print('File downloaded successfully')

with open(filename) as f:
    lines = f.readlines()[1:]
    lines[0] = 'unix,date,symbol,open,high,low,close,VolumeBTC,VolumeUSDT,tradecount\n'

with open(filename, "w") as f:
    f.writelines(lines)
