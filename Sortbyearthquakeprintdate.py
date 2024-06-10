import pandas as pd
from stocklist import list1

class Earthquake:
    def __init__(self,x):
        self.x = x
        # Read data from CSV and set date as index
        self.data = pd.read_csv(f'C:\\Users\\adity\\Desktop\\EQ\\ranking_list\\{self.x}.csv')
        self.newsort = self.data.sort_values(['earthquake'], ascending=True, kind='mergesort')
        self.newsort2 = self.data.sort_values(['earthquake'], ascending=False, kind='mergesort')

    def print(self):
        print(self.newsort[['date','earthquake']].head(5))
        print(self.newsort2[['date','earthquake']].head(5))



object_list = [Earthquake(list1[i]) for i in range(0,200)] 

for obj in object_list:
    obj.print()
    

        