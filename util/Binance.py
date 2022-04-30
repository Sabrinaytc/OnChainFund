import pandas as pd
import Config as config
from binance.client import Client
import requests


def connect_Binance():

    api_key = config.Binance_API_Key
    api_secret = config.Binance_API_Secret
    client = Client(api_key, api_secret)

    return client
