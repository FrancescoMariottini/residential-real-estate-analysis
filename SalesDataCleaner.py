import pandas as pd
import numpy as numpy
import re
 
class SalesDataCleaner:
    def __init__(self, url):
        self.url = url
        self.sales_data = pd.read_csv(url)
    
    def display(self):
        print(self.sales_data)

    def merge_postcodes_localities(self):
        self.sales_data = self.sales_data.apply(SalesDataCleaner.extract_postcodes, axis='columns')
        self.sales_data = self.sales_data.drop('locality', axis='columns')

    @staticmethod
    def extract_postcodes(row):
        if(pd.isna(row.postcode)):
            legal_belgian_postcode_pattern = '[1-9][0-9][0-9][0-9]'
            extracted_postcodes = re.findall(legal_belgian_postcode_pattern, row.locality)
            if len(extracted_postcodes) > 0 :
                row.postcode = str(int(extracted_postcodes[0]))
        else:
            row.postcode = str(int(row.postcode))
        return row


url = 'https://raw.githubusercontent.com/FrancescoMariottini/project3/main/inputs/all_sales_data.csv'
sdc = SalesDataCleaner(url)
sdc.merge_postcodes_localities()
sdc.display()
