#an example use of the SalesDataCleaner class to write to another CSV file the cleaned DataFrame obtained from an original CSV file

from SalesDataCleaner import SalesDataCleaner


url = 'https://raw.githubusercontent.com/FrancescoMariottini/project3/main/inputs/all_sales_data.csv'

sdc = SalesDataCleaner(url)

sdc.clean()

sdc.write_to_csv('clean_sales_dataset.csv')