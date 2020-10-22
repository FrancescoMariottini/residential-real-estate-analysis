from SalesDataCleaner import SalesDataCleaner


url = 'https://raw.githubusercontent.com/FrancescoMariottini/project3/main/inputs/all_sales_data.csv'

sdc = SalesDataCleaner(url)

sdc.clean()
