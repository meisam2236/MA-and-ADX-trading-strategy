import pandas as pd
import numpy as np
from ta.trend import ADXIndicator
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

file = pd.read_csv('Khesapa.csv', parse_dates=['<DTYYYYMMDD>'])
file = file.set_index('<DTYYYYMMDD>')

data = pd.DataFrame()
data['close'] = file['<CLOSE>']
data['SMA55'] = file['<CLOSE>'].rolling(window=55).mean()
data['EMA13'] = pd.Series.ewm(file['<CLOSE>'], span=13).mean()
data['EMA233'] = pd.Series.ewm(file['<CLOSE>'], span=233).mean()
data['ADX'] = ADXIndicator(file['<HIGH>'],file['<LOW>'],file['<CLOSE>'],14,False).adx()

def buy_sell(data):
    sigPriceBuy = []
    sigPriceSell = []
    flag = -1
    for i in range(len(data)):
        if data['EMA13'][i] > data['EMA233'][i] and data['ADX'][i] > 25:
            if flag != 1:
                sigPriceBuy.append(data['close'][i])
                sigPriceSell.append(np.nan)
                flag = 1
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        elif data['SMA55'][i] < data['EMA233'][i] and data['ADX'][i] > 25:
            if flag != 0:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(data['close'][i])
                flag = 0
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        else:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)
    return (sigPriceBuy, sigPriceSell)

buy_sell = buy_sell(data)
data['buy_signal_price'] = buy_sell[0]
data['sell_signal_price'] = buy_sell[1]

plt.figure(figsize=(12.5, 4.5))
print(data['close'])
plt.plot(data['close'], label='close', alpha=0.35)
plt.plot(data['SMA55'], label='SMA55', alpha=0.35)
plt.plot(data['EMA13'], label='EMA13', alpha=0.35)
plt.plot(data['EMA233'], label='EMA233', alpha=0.35)
plt.scatter(data.index, data['buy_signal_price'], label='buy signal', marker='^', color='green')
plt.scatter(data.index, data['sell_signal_price'], label='sell signal', marker='v', color='red')
plt.title('Close price of Khesapa')
plt.ylabel('Close price(Rial)')
plt.legend(loc='upper left')
plt.show()
