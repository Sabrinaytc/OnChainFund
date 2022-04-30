import pandas as pd
import numpy as np
import util.Config as config
import util.Glassnode as GN
import util.Indicators as Indicators


API_KEY = config.Glassnode_API_KEY
ClosedPrice = config.ClosedPrice
HashRate = config.HashRate
HashRibbon = config.HashRibbon
Difficulty = config.Difficulty
DifficultyRibbon = config.DifficultyRibbon

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

    ## Variables Declaration
    Column_Name = ["Date", "Price", "Buy/Sell"]


    HashRate_Data = Indicators.Get_RawData(url=HashRate, params=params, value_name= 'HashRate')
    ClosedPrice_Data = Indicators.Get_RawData(url=ClosedPrice, params=params, value_name='Closed Price')


    HashRibbon_Data = Indicators.Get_Ribbon(url=HashRibbon, params=params)

    # print(HashRate_Data)
    # print(HashRibbon_Data)
    # print(ClosedPrice_Data)