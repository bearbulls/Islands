import pandas_datareader as web
import pandas as pd
import datetime as dt

data = pd.read_csv("Nifty_500.csv")
df = data['Symbol'].tolist()

st = dt.datetime.now() - dt.timedelta(days=1825)
et = dt.datetime.now()

while True:
    ticker = input("Enter Ticker Name = ") + ".NS"
    df = web.DataReader(ticker, 'yahoo', st, et)
    try:
        cmp = round(df['Close'][-1], 2)
        day_Change = round(((df['Close'][-1] - df['Close'][-2]) / df['Close'][-2]) * 100, 2)
        week_Change = round(((df['Close'][-1] - df['Close'][-5]) / df['Close'][-5]) * 100, 2)
        month_change = round(((df['Close'][-1] - df['Close'][-27]) / df['Close'][-27]) * 100, 2)
        ytd = round(((df['Close'][-1] - df['Close']['2022-01-03']) / df['Close']['2022-01-03']) * 100, 2)
        six = round(((df['Close'][-1] - df['Close'][-124]) / df['Close'][-124]) * 100, 2)
        one_yr = round(((df['Close'][-1] - df['Close'][-248]) / df['Close'][-248]) * 100, 2)
        three_yr = round(((df['Close'][-1] - df['Close'][-742]) / df['Close'][-742]) * 100, 2)
        five_yr = round(((df['Close'][-1] - df['Close'][-1234]) / df['Close'][-1234]) * 100, 2)
        print(f'Current Price = {cmp}')
        print(f'One Day Return = {day_Change}')
        print(f'Weekly Return = {week_Change}')
        print(f'Monthly Return = {month_change}')
        print(f'YTD Return = {ytd}')
        print(f'Six month Return = {six}')
        print(f'One Year Return = {one_yr}')
        print(f'Three Years Return = {three_yr}')
        print(f'Five Years Return = {five_yr}')
        print(f'**********************')
    except Exception as e:
        cmp = round(df['Close'][-1], 2)
        day_Change = round(((df['Close'][-1] - df['Close'][-2]) / df['Close'][-2]) * 100, 2)
        week_Change = round(((df['Close'][-1] - df['Close'][-5]) / df['Close'][-5]) * 100, 2)
        month_change = round(((df['Close'][-1] - df['Close'][-27]) / df['Close'][-27]) * 100, 2)
        ytd = round(((df['Close'][-1] - df['Close']['2022-01-03']) / df['Close']['2022-01-03']) * 100, 2)
        six = round(((df['Close'][-1] - df['Close'][-124]) / df['Close'][-124]) * 100, 2)
        one_yr = round(((df['Close'][-1] - df['Close'][-248]) / df['Close'][-248]) * 100, 2)
        three_yr = round(((df['Close'][-1] - df['Close'][0]) / df['Close'][0]) * 100, 2)
        five_yr = round(((df['Close'][-1] - df['Close'][0]) / df['Close'][0]) * 100, 2)
        print(f'Current Price = {cmp}')
        print(f'One Day Return = {day_Change}')
        print(f'Weekly Return = {week_Change}')
        print(f'Monthly Return = {month_change}')
        print(f'YTD Return = {ytd}')
        print(f'Six month Return = {six}')
        print(f'One Year Return = {one_yr}')
        print(f'Three Years Return = {three_yr}')
        print(f'Five Years Return = {five_yr}')
        print(f'**********************')