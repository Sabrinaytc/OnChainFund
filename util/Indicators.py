import pandas as pd
import numpy as np
import requests
from datetime import datetime


def Get_RawData(url, params, value_name):

    res = requests.get(url, params=params)
    data = res.json()

    df_nested_list = pd.json_normalize(data)
    df_nested_list['t'] = pd.to_datetime(df_nested_list['t'], unit= 's') 
    df_nested_list.rename(columns={'t':'Date', 'v': value_name}, inplace=True)
    df_nested_list.set_index('Date', inplace=True)

    return df_nested_list



def Get_Ribbon(url, params):

    res = requests.get(url, params=params)
    data = res.json()

    df_nested_list = pd.json_normalize(data)
    df_nested_list['t'] = pd.to_datetime(df_nested_list['t'], unit= 's') 
    df_nested_list.rename(columns={'t':'Date'}, inplace=True)
    df_nested_list.set_index('Date', inplace=True)

    return df_nested_list



def SMA():

    return


