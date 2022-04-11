import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
import Config as config


API_KEY = config.Glassnode_API_KEY
HashRate = config.HashRate
HashRibbon = config.HashRibbon

res = requests.get(HashRate, params={'a': 'BTC', 'api_key': API_KEY})
data = res.json() 

print(data)