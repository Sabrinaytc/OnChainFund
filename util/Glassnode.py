import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
import Config as config


API_KEY = config.Glassnode_API_KEY
HashRate = config.HashRate
HashRibbon = config.HashRibbon

## Parameters
'''
a : symbol, BTC, ETH
s : integer (unix timestamp) since
u : integer (unix timestamp) until
i : string (frequency interval) 1h, 24h, 10m, 1month, 1w
f : string (format) JSON, CSV
'''

res = requests.get(HashRate, params={'a': 'BTC', 'api_key': API_KEY})
data = res.json() 

df_nested_list = pd.json_normalize(data)
df_nested_list['t'] = pd.to_datetime(df_nested_list['t'], unit= 's') 

print(df_nested_list)



def GetData(url):

    return