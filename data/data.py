import yfinance as yf
import datetime
import math
import numpy as np



def get_data():
    tr_start_date=datetime.datetime(2015,1,1)
    tr_end_date=datetime.datetime(2021,12,30)

    v_start_date=datetime.datetime(2022,1,1)
    v_end_date=datetime.datetime(2024,12,30)


    te_start_date=datetime.datetime(2025,1,1)
    te_end_date=datetime.datetime.now()


    meta=yf.Ticker('META')  

    training_data=meta.history(start=tr_start_date,end=tr_end_date)
    validation_data=meta.history(start=v_start_date,end=v_end_date)
    test_data=meta.history(start=te_start_date,end=te_end_date)

    training_data = training_data.drop(columns=["Dividends","Stock Splits"])
    validation_data = validation_data.drop(columns=["Dividends","Stock Splits"])
    test_data = test_data.drop(columns=["Dividends","Stock Splits"])

    #simple returns calculated by closing prices
    training_data["Simple Return"]=(training_data['Close']/training_data['Close'].shift(1))-1
    validation_data["Simple Return"]=(validation_data['Close']/validation_data['Close'].shift(1))-1
    test_data["Simple Return"]=(test_data['Close']/test_data['Close'].shift(1))-1

    #logarithmic return for closing prices
    training_data["Logarithmic Return"]=np.log(training_data["Close"]/training_data["Close"].shift(1))
    validation_data["Logarithmic Return"]=np.log(validation_data["Close"]/validation_data["Close"].shift(1))
    test_data["Logarithmic Return"]=np.log(test_data["Close"]/test_data["Close"].shift(1))

    return training_data,validation_data,test_data






