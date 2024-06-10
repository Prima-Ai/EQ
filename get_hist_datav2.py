import yfinance as yf
import  pandas as pd
import datetime
import sqlite3
from stocklist import list1

class Get_Hist_Data:
    def __init__(self,x):
        self.x = x
        # Read data from CSV and set date as index
        self.data = pd.read_csv(f'C:/Users/adity/Desktop/EQ/1500_stock_his_data/{self.x}.csv')
        self.data["Date"] = pd.to_datetime(self.data['Date'])
        self.data.set_index('Date',inplace=True)
        self.length = len(self.data)
        ## empty lists to store the values 
        self.SP1 = []
        self.SP2 = []
        self.earthquake_vals = []        
        

    # spot value 1 function
    def Spot_value1_fn(self):
        for i in range(self.length-1):
            today_low = self.data['Low'].iloc[i+1]
            today_high = self.data['High'].iloc[i+1]
            today_closed = self.data['Close'].iloc[i+1]
            diff = today_high - today_low
            Spot_value = (diff / today_closed) * 100
            self.SP1.append(Spot_value)
        return "spot value 1 calculated \n"
    
    #spot value 2 function
    def Spot_value2_fn(self):
        for i in range(self.length-1):
            yesterdays_closed = self.data['Close'].iloc[i]
            today_low = self.data['Low'].iloc[i+1]
            diff = yesterdays_closed - today_low
            spot_values = (diff/today_low) * 100
            self.SP2.append(spot_values)
        return"spot values 2 calculated \n"
    
    
    def earthquake(self):
        for i in range(len(self.SP1)):
            value = self.SP1[i] + self.SP2[i]
            self.earthquake_vals.append(value)
        return "the earthquake values are saved sucessfully."

    def create_df(self):
        # date_column = self.data['Date']
        df = pd.DataFrame({
            'date' : self.data.index[1:],
            'SP1': self.SP1,
            'SP2': self.SP2,
            'earthquake': self.earthquake_vals
        })
        # df['date'] = date_column
        df.to_csv(f"C:/Users/adity/Desktop/EQ/ranking_list/{self.x}.csv")
        return df
    
    
    def print_lists(self):
        print("sp1",self.SP1)
        print("\n","\n")
        print("SP2",self.SP2)
        print("\n","\n")
        print("earthquake values\n",self.earthquake_vals)


# Create a list of Get_Hist_Data objects using list comprehension
object_list = [Get_Hist_Data(list1[i]) for i in range(0,200)] 

# Access objects in the list
for obj in object_list:
    print(f"calculating spot 1 value\n{obj.Spot_value1_fn()}")
    print(f'calculating spot 2 value\n{obj.Spot_value2_fn()}')
    print(f"the earthquake values\n{obj.earthquake()}")
    obj.print_lists()
    print(obj.create_df())

