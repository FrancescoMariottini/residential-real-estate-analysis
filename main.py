from SalesDataCleaner import SalesDataCleaner


url = 'https://raw.githubusercontent.com/FrancescoMariottini/project3/main/inputs/all_sales_data.csv'

sdc = SalesDataCleaner(url)

# print(sdc.sales_data.dtypes)

sdc.delete_hyperlink_column()
sdc.delete_land_plot_surface_column()

# sdc.merge_postcodes_localities_columns()

# sdc.clean_house_subtype_column()

# sdc.clean_sale_column()

# sdc.clean_building_state_column()

sdc.clean_price_column()

# sdc.display()

# print(sdc.sales_data.dtypes)
