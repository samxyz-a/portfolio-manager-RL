import yfinance as yf
import datetime



start_date=datetime.datetime(2015,1,1)
end_date=datetime.datetime(2021,12,30)

meta=yf.Ticker('META')

data=meta.history(start=start_date,end=end_date)



print(data.to_string())
