import pandas as pd
import yfinance as yf

class get_data:
    def __init__(self):
        self.n200 = pd.read_csv("C:/Users/adity/Desktop/EQ/n200.csv")
        self.symbols = self.n200['symbol']
    
    def extract_data(self):
        for i in self.symbols:
            ticker_symbol = i
            data = yf.download(f"{ticker_symbol}.NS")
            data.to_csv(f"C:/Users/adity/Desktop/EQ/1500_stock_his_data/{ticker_symbol}.csv")
    


obj = get_data()
symbols = obj.extract_data()
print(symbols)