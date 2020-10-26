
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import pdb


url='https://raw.githubusercontent.com/FrancescoMariottini/project3/main/inputs/all_sales_data.csv'
sales_data=pd.read_csv(url)
print(sales_data.shape)
print(sales_data.columns.tolist())


ColumnName=sales_data.columns.tolist()
MissingValue=[]
total_number_missing=0
for s in range(0,len(ColumnName)):
    MissingValues=sales_data[ColumnName[s]].isnull().sum()
    total_number_missing +=MissingValues
    PercentageMissing=(100*MissingValues)/float(sales_data.shape[0])
    #dic[ColumnName[s]]=np.round(PercentageMissing, 2)
    MissingValue.append(np.round(PercentageMissing, 2))




print(MissingValue)
print(sum(MissingValue))
print(total_number_missing)
print([100-i for i in MissingValue])

dic1={'col_name':ColumnName, 'missing_percentage':MissingValue}
dic2={'col_name':ColumnName, 'not_missing_percentage':[100-i for i in MissingValue]}

missing_data1=pd.DataFrame(dic1)
missing_data2=pd.DataFrame(dic2)

plt.figure(1, figsize=(10,10)) #we can use either ax or plt options
ax = plt.subplot(111)
plt.plot(MissingValue,'-',color='black')
plt.plot(MissingValue, color='red', alpha=0.6, marker='o', markersize=9)
ax.xaxis.set_ticks(np.arange(0,22))
n=['Source', 'Hyperlink', 'Locality', 'Postcode', 'House', 'Prop-Type', 'Price', 'Sale', 'RoomsNo', 'Area','Kitchen', 'Furnished', 'OpenFire', 'Terrace', 'TerraceArea', 'Garden', 'GardenArea', 'LandSur.', 'landPlotSur.', 'FacadesNo', 'Swimming', 'Build.State']
px = 6.5
py = 70
plt.text(px, py, "sales_data shape=$(93068, 22)$", ha="right",color="blue", weight="heavy", fontsize=11,)
plt.text(3, 60, "Target: $Price$", ha="right",color="blue", weight="heavy", fontsize=11,)
ax.xaxis.set_ticklabels(n)
plt.xticks(rotation=45)
plt.grid(True)
plt.title("Data Analysis\nPercentage of missing values in each Variable", fontsize=14)
plt.xlabel("Column_name", fontsize=5)
plt.ylabel("Percentage of missing values (%)")



total_number_available=(sales_data.shape[0] * sales_data.shape[1])-total_number_missing
plt.figure(2, figsize=(10,10)) #we can use either ax or plt options
plt.title("Data Analysis\nPercentage of Missing and Available Values", fontsize=14)
labels = 'Missing_Values', 'Available_Values'
sizes = [total_number_missing, total_number_available]
colors = [ 'lightcoral', 'lightskyblue']
plt.pie(sizes, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')


plt.show()




# print(MissingValue)