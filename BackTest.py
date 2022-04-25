import pandas as pd
import numpy as np
import util.Config as config
import util.Glassnode as GN


API_KEY = config.Glassnode_API_KEY
HashRate = config.HashRate
HashRibbon = config.HashRibbon
params = {'a': 'BTC', 'api_key': API_KEY}


## Parameters
'''
a : symbol, BTC, ETH
s : integer (unix timestamp) since
u : integer (unix timestamp) until
i : string (frequency interval) 1h, 24h, 10m, 1month, 1w
f : string (format) JSON, CSV
'''



if __name__ == '__main__':

    HashRate_Data = GN.GetData(url=HashRate, params=params)

    print(HashRate_Data)