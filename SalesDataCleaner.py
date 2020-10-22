import pandas as pd
import numpy as np
import re
 
class SalesDataCleaner:
    def __init__(self, url):
        self.url = url
        self.import_and_format()
    

    def import_and_format(self):
        columns_types = {
            "source":               int,
            "hyperlink":            str,
            "locality":             str,
            "postcode":             str,
            "house_is":             bool,
            "property_subtype":     str,
            "sale":                 str,
            "rooms_number":         float, #cannot convert float NaN to integer
            "garden_area":          float, #ValueError: Integer column has NA values in column 16
            "land_surface":         float,
            "facades_number":       float, #changed to float to deal with None
            "building_state":       str
        }

        columns_converters = {
            #read_csv has issue with None in Boolean (interpreted as object). I am using "kitchen_has": lambda x: bool(x) if type(x) is bool else Non
            "kitchen_has": lambda x: SalesDataCleaner.bool_or_keep(x),
            "furnished": lambda x: SalesDataCleaner.bool_or_keep(x),
            "open_fire": lambda x: SalesDataCleaner.bool_or_keep(x),
            "terrace": lambda x: SalesDataCleaner.bool_or_keep(x),
            "garden": lambda x: SalesDataCleaner.bool_or_keep(x),
            "swimming_pool_has": lambda x: SalesDataCleaner.bool_or_keep(x),
            "terrace_area": lambda x: SalesDataCleaner.float_or_zero(x),
            "land_plot_surface": lambda x: SalesDataCleaner.float_or_text_to_nan(x),
            "area": lambda x: SalesDataCleaner.area_remove_m2(x)
        }

        columns = columns_types.keys()
        na_identifiers = ["NA","None", "Not specified", "NaN", "NAN"]

        self.sales_data = pd.read_csv(self.url,  sep=",", dtype=columns_types, skipinitialspace=True, converters=columns_converters, na_values=na_identifiers, low_memory=False)

    @staticmethod
    def bool_or_keep(x):
        output = None
        try:
            if isinstance(x, str):
                if (x == "1") or (x.upper() == "TRUE"):
                    output = True
                elif (x == "0") or (x.upper() == "FALSE"):
                    output = False
            elif x.isnumeric():
                if x == 1:
                    output = True
                elif x == 0:
                    output = False
            elif isinstance(x, bool):
                output = x
            return output
        except ValueError:
            return None

    @staticmethod
    def float_or_zero(x):
        try:
            float(x)
            return float(x)
        except ValueError:
            #keeping information of terrace if lost
            if x == True or x == 1 or x == "True" or x == "TRUE":
                return 0
            else:
                return None
    
    @staticmethod
    def float_or_text_to_nan(x):
        try:
            return float(x)
        except ValueError:
            return None

    @staticmethod
    def area_remove_m2(x):
        try:
            return int(x)
        except ValueError:
            numbers = [int(s) for s in x.split() if s.isdigit()]
            if len(numbers) == 1:
                return float(numbers[0])
            elif len(numbers) > 1:
                return False
            else:
                return None

    def display(self):
        print(self.sales_data)

    def delete_hyperlink_column(self):
        self.sales_data.drop('hyperlink', axis='columns', inplace=True)

    def delete_land_plot_surface_column(self):
        self.sales_data.drop('land_plot_surface', axis='columns', inplace=True)

    @staticmethod
    def extract_postcodes(row):
        if(pd.isna(row.postcode)):
            legal_belgian_postcode_pattern = '[1-9][0-9][0-9][0-9]'
            extracted_postcodes = re.findall(legal_belgian_postcode_pattern, row.locality)
            if len(extracted_postcodes) > 0:
                row.postcode = str(int(extracted_postcodes[0]))
            else:
                row.postcode = None
        else:
            row.postcode = str(int(row.postcode))
        return row
    

    def merge_postcodes_localities_columns(self):
        self.sales_data = self.sales_data.apply(SalesDataCleaner.extract_postcodes, axis='columns')
        self.sales_data.drop('locality', axis='columns', inplace=True)

    def process_house_subtype_column(self):
        to_be_deleted_subtypes = ['Wohnung', 'Triplexwohnung', 'Sonstige', 'Loft / �tico', 'Loft / Dachgeschoss', 'Loft / Attic',
               'Gewerbe', 'Etagenwohnung', 'Erdgeschoss', 'Attico', 'Appartamento duplex', 'Apartamento', 'Altbauwohnung']

        to_be_deleted_filter = self.sales_data['property_subtype'].apply(lambda x: x in to_be_deleted_subtypes)
        self.sales_data['property_subtype'][to_be_deleted_filter] = None
        
        to_be_deleted_filter = self.sales_data['property_subtype'].apply(lambda x: type(x) in [int, float])
        self.sales_data['property_subtype'][to_be_deleted_filter] = None
        
        to_be_deleted_filter = self.sales_data['property_subtype'].apply(lambda x: "sqft" in str(x))
        self.sales_data['property_subtype'][to_be_deleted_filter] = None
    
    def process_sale_column(self):
        to_be_deleted_filter = self.sales_data['sale'].str.contains('annuity', na=False)
        print(type(to_be_deleted_filter))
        print(len(self.sales_data['sale'][to_be_deleted_filter]))
        self.sales_data['property_subtype'][to_be_deleted_filter] = None
        
        # c = 0
        # for i,v in self.sales_data['property_subtype'].items():
        #     if self.sales_data['property_subtype'][i] is None:
        #         c += 1
        # print(c)