from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from DateTime import DateTime


def CleanData(symbol):

    ## Read from CSV
    HashRate_24h = pd.read_csv('./data/hash-rate-%s-24h.csv' %(symbol)) 
    Price_24h = pd.read_csv('./data/price-%s-24h.csv' %(symbol)) 

    ## Clean the timestamp column (type: string)
    HashRate_24h['timestamp'] = HashRate_24h['timestamp'].str[0:10]
    Price_24h['timestamp'] = Price_24h['timestamp'].str[0:10]

    ## Merge two dfs based on timestamp, rename, and change string to datetime
    df = pd.merge(HashRate_24h, Price_24h, on='timestamp')
    df.rename( columns = {'value_x' : 'Hash Rate', 'value_y' : 'Price'}, inplace = True)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    return df


def Data_Normalize():


    return 



if __name__ == '__main__':

    ETH_df = CleanData('ETH')
    BTC_df = CleanData('BTC')

    ## Calculate the Correlation between Hash Rate and Price
    BTC_1D_Corr = BTC_df['Hash Rate'].corr(BTC_df['Price'])
    ETH_1D_Corr = ETH_df['Hash Rate'].corr(ETH_df['Price'])

    ## Moving Average???
    BTC_5D_Corr = BTC_df['Hash Rate'].rolling(5).corr(BTC_df['Price'])
    ETH_5D_Corr = ETH_df['Hash Rate'].rolling(5).corr(ETH_df['Price'])

    ##################################################################################
    '''
    ETH
    POW: 2015.08.08 - 2020.11.30
    '''

    POW_Date = datetime.strptime('2020-12-01', '%Y-%m-%d')
    ETH_POW_df = ETH_df[ETH_df['timestamp'] < POW_Date]
    ETH_POW_POS_df = ETH_df[ETH_df['timestamp'] > POW_Date]

    ETH_POW_Corr = ETH_POW_df['Hash Rate'].corr(ETH_df['Price'])
    ETH_POW_POS_Corr = ETH_POW_POS_df['Hash Rate'].corr(ETH_df['Price'])

    # print('ETH All Time Corr is : ' + str(ETH_1D_Corr))
    # print('ETH POW Corr is : ' + str(ETH_POW_Corr))
    # print('ETH POW & POS Corr is : ' + str(ETH_POW_POS_Corr))
    # print('\n' + 'BTC All Time Corr is : ' + str(BTC_1D_Corr))

    BTC_5D_Corr = BTC_5D_Corr.dropna()
    print(max(BTC_5D_Corr))
    print(min(BTC_5D_Corr))

    plt.plot(BTC_5D_Corr)
    plt.show()

    '''
    fig, ax = plt.subplots()
    ax.plot(BTC_df['timestamp'], BTC_df['Price'], color = 'red')
    ax.set_xlabel("time")
    ax.set_ylabel("price", color = "red")

    ax2 = ax.twinx()
    ax2.plot(BTC_df['timestamp'], BTC_df['Hash Rate'], color = 'blue')
    ax2.set_ylabel("hash rate", color = "blue")
    plt.show()

    '''


    # plt.plot(ETH_df['timestamp'], ETH_df['Price'], label = 'Price')
    # plt.plot(ETH_df['timestamp'], ETH_df['Hash Rate'], label = 'Hash Rate')

    # plt.legend()
    # plt.show()