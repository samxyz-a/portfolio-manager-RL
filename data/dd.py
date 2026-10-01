from data import get_data
import pandas as pd

datasets=get_data()


def features_data(data_f):

    for data in data_f:
        data["5-Day Return"]=(data["Close"]/data["Close"].shift(5))-1 #5-day return  
        data["20-Day Return"]=(data["Close"]/data["Close"].shift(20))-1 #20 day return
        data["20-Day Moving Avg"]=data["Close"].rolling(20).mean() #20-day SMA
        data["50-Day Moving Avg"]=data["Close"].rolling(50).mean() #50-day SMA
        data["Price/20-day SMA"]=data["Close"]/data["Close"].rolling(20).mean()
        data["Price/50-day SMA"]=data["Close"]/data["Close"].rolling(50).mean()

        rs_value=data["Close"].diff().where(data["Close"].diff() > 0, 0).expanding().mean()/-data["Close"].diff().where(data["Close"].diff() < 0, 0).expanding().mean()
        data["RSI"]=100-(100/(1+rs_value))

        #EMA calculation
        multiplier=2/13
        ema=data["Close"].iloc[0]

        for i in range(1,len(data)):
            current_ema=


        data["%Volume Change"]=((data["Volume"]/data["Volume"].shift(1))-1)*100
        data["20-day Volume Change"]=data['Volume'].rolling(20).mean()

    return data_f    


result=features_data(datasets)

print(result[0])