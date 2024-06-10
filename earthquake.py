import pandas as pd
# import get_hist_data

class earthquake:
    def __init__(self):
        self.data  = pd.read_csv("earthquake_v_2.0/1500_stock_his_data/ranking_list_hdfc.csv")
        
    def ranking(self):
        if 'earthquake' not in self.data.columns:
            self.data['earthquake'] = None
        
        for i,row in self.data.iterrows():
            Earthquake = row['SP1'] + row['SP2']
            self.data.at[i,'earthquake'] = Earthquake
            print(f"Computed earthquake value for row {i} : {Earthquake}")
        
        return "the ranking element added successfully."

ans = earthquake()
print(f"ranking initializes \n{ans.ranking()}")
