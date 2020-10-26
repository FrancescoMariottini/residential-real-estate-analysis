
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import pdb


url='https://raw.githubusercontent.com/FrancescoMariottini/project3/main/clean_sales_dataset.csv'
sales_data=pd.read_csv(url)
print(sales_data.columns.tolist())


###this is before removing outliers
sales_data_STAT=sales_data[['price', 'rooms_number', 'area', 'terrace_area', 'garden_area', 'land_surface', 'facades_number']]

'''
the following code is done in the clean_sales_dataset.csv, and this because in reality there is no price=0, no area=0, no facade_face=0 

sales_data_STAT.loc[sales_data_STAT.price == 0, 'price'] = np.nan
sales_data_STAT.loc[sales_data_STAT.area == 0, 'area'] = np.nan
sales_data_STAT.loc[sales_data_STAT.facades_number == 0, 'facades_number'] = np.nan
#sales_data_STAT.loc[sales_data_STAT.land_surface == 0, 'land_surface'] = np.nan
sales_data_STAT.loc[sales_data_STAT.facades_number >4 , 'facades_number'] = np.nan

sales_data_STAT=sales_data_STAT.loc[(sales_data['price'] >0)]
sales_data_STAT=sales_data_STAT.loc[(sales_data['area'] >0)]
sales_data_STAT=sales_data_STAT.loc[(sales_data['facades_number'] >0)]
#sales_data_STAT=sales_data_STAT.loc[(sales_data['land_surface'] >0)]

'''

print(sales_data_STAT.describe(percentiles =[.05, .25, .75, .95]))
#           price      rooms_number          area  terrace_area   garden_area  land_surface  facades_number
# count  1.128800e+04  11288.000000  11288.000000  11288.000000  11288.000000  1.128800e+04       64.000000
# mean   4.927968e+05      3.199947    195.134036     12.608965    230.076364  8.396805e+02        2.687500
# std    5.676955e+05      3.786751    219.598588     28.274838   2053.797648  1.368982e+04        0.852168
# min    2.500000e+04      0.000000      5.000000      0.000000      0.000000  0.000000e+00        1.000000
# 5%     1.290000e+05      1.000000     60.000000      0.000000      0.000000  0.000000e+00        2.000000
# 25%    2.250000e+05      2.000000     97.000000      0.000000      0.000000  0.000000e+00        2.000000
# 50%    3.290000e+05      3.000000    146.000000      0.000000      0.000000  0.000000e+00        2.500000
# 75%    5.300000e+05      4.000000    227.000000     15.000000      0.000000  4.220000e+02        3.000000
# 95%    1.400000e+06      6.000000    471.650000     55.000000    800.000000  2.420000e+03        4.000000
# max    1.500000e+07    204.000000   9250.000000    708.000000  94000.000000  1.379000e+06        4.000000


#############################################
## Detecting Removing Outliers using zscore
##############################################

'''
Because I can not use zscore to compute outliers since there are None Values,
I will return to the sales_data before changing, price, area, facade_
'''
sales_data_to_zscore=sales_data[['price', 'rooms_number', 'area', 'terrace_area', 'garden_area', 'land_surface']]

#

# sales_data_to_zscore.loc[sales_data_STAT.price == np.nan, 'price'] = 0
# sales_data_to_zscore.loc[sales_data_STAT.area == np.nan, 'area'] = 0
# sales_data_to_zscore.loc[sales_data_STAT.land_surface == np.nan, 'land_surface'] = 0


sales_data_to_zscore.loc[sales_data_STAT.price == np.nan, 'price'] = sales_data_to_zscore['price'].mean()
sales_data_to_zscore.loc[sales_data_STAT.area == np.nan, 'area'] = sales_data_to_zscore['area'].mean()
#I cannot change it because, the csv file is updated by Joachim
# sales_data_to_zscore.loc[sales_data_STAT.land_surface == np.nan, 'facades_number'] = float(sales_data_to_zscore['facades_number'].mean())


from scipy import stats
z = np.abs(stats.zscore(sales_data_to_zscore))
threshold = 3
print(np.where(z > 3))
print(np.shape(np.where(z > 3)))
sales_data_to_zscore= sales_data_to_zscore[(z <3).all(axis=1)]

print(sales_data_to_zscore.shape)
print(sales_data_to_zscore.describe(percentiles =[.05, .25, .75, .95]))
# print(sales_data_to_zscore.area.describe())
# print(sales_data_to_zscore.area.min())





#
#               price  rooms_number          area  terrace_area   garden_area  land_surface
# count  1.073000e+04  10730.000000  10730.000000  10730.000000  10730.000000  10730.000000
# mean   4.174627e+05      2.980988    173.226841      9.733551    108.972973    457.332060
# std    3.216070e+05      1.597840    113.730132     16.436081    421.797047   1570.278456
# min    2.500000e+04      0.000000      5.000000      0.000000      0.000000      0.000000
# 5%     1.280000e+05      1.000000     59.000000      0.000000      0.000000      0.000000
# 25%    2.200000e+05      2.000000     95.000000      0.000000      0.000000      0.000000
# 50%    3.175000e+05      3.000000    140.000000      0.000000      0.000000      0.000000
# 75%    4.950000e+05      4.000000    216.000000     14.750000      0.000000    369.000000
# 95%    1.100000e+06      6.000000    400.000000     45.000000    644.550000   1983.850000
# max    2.195000e+06     14.000000    850.000000     97.000000   6160.000000  40500.000000

import seaborn as sns
# ##########################################################
# ##############       BOX             #####################
# ##########################################################
# # # use box plot for the Age feature
# #fig=plt.figure(f
plt.figure(1, figsize=(15,10)) #we can use either ax or plt options
plt.suptitle('Statistical Analysis for Quantitative Variables')

plt.title("")

ax = plt.subplot2grid((3,3), (0,0))
area= sales_data['area']
ax.boxplot(area[(area >= 5 ) & (area <= 850 )])
#sns.boxplot(sales_data['area'])
#ax.yaxis.set_ticks([ 0, 1000, 2000, 3000, 4000])
ax.title.set_text("Area")

ax = plt.subplot2grid((3,3), (0,1))
garden_area= sales_data['garden_area']
ax.boxplot(garden_area[(garden_area > 0 ) & (garden_area <= 6160 )])
plt.grid(False)
ax.xaxis.set_ticklabels([])
ax.title.set_text("Garden_area")



ax = plt.subplot2grid((3,3), (0,2))
land_surface= sales_data['land_surface']
ax.boxplot(land_surface[(land_surface >0 ) & (land_surface < 40000 )])
ax.xaxis.set_ticklabels([])
ax.title.set_text("Land_surface")

ax = plt.subplot2grid((3,3), (1,0))
terrace_area= sales_data['terrace_area']
ax.boxplot(terrace_area[(terrace_area >=0 ) & (terrace_area <=97)])
ax.xaxis.set_ticklabels([])
ax.title.set_text('Terrace_area')

ax = plt.subplot2grid((3,3), (1,1))
price= sales_data['price']
ax.boxplot( price[(price >= 2.500000e+04 ) & (price <= 2.195000e+06 )] ) #for drawing, I considered less than the min and greater
    # than the max is an outlier. The outlier is detecting using zscore.I remove them from the original data.
plt.grid(False)
ax.xaxis.set_ticklabels([])
ax.title.set_text('Price')

ax = plt.subplot2grid((3,3), (1,2))
room_number= sales_data['rooms_number']
ax.boxplot( room_number[(room_number >= 0 ) & (room_number <= 14 )] ) #for drawing, I considered less than the min and greater
#ax.hist(sales_data['rooms_number'].astype(int), bins = [0,1,2,3,4,5,6,7,8,9,10,11, 12, 13,14,15], rwidth=0.95)
plt.title('Rooms_number')
ax.xaxis.set_ticklabels([])

ax = plt.subplot2grid((3,3), (2,0))
#plt.hist(sales_data['facades_number'], rwidth=0.95, bins = [0,1, 2, 3, 4])
sales_data['facades_number'].value_counts().plot(kind='bar', alpha=.6,color='red',fontsize=10)
ax.set_xticklabels(["2","3","4","1"], rotation=0)
plt.title('Facades_number')

'''
fig 2
'''


plt.figure(2, figsize=(15,10)) #we can use either ax or plt options
plt.suptitle('Statistical Analysis for Qualitative Variables')
ax = plt.subplot2grid((4,3), (0,0))
sales_data['house_is'].value_counts().plot(kind='bar', alpha=.6,color='red',fontsize=10)
ax.set_xticklabels(["House","Appartement"], rotation=0)
plt.title('house_is')

ax = plt.subplot2grid((4,3), (0,1))
postcode=sales_data.postcode.value_counts().reset_index(name='value_counting')[0:5] #select the most postcode
ax.bar(postcode.index, postcode.value_counting,alpha=.6,color='red')
labels_x=sales_data.postcode.value_counts().index[0:5]
#ax.xaxis.set_ticklabels(labels_x)
ax.xaxis.set_ticklabels([])
#plt.text(8300,1180,1000,9000,1050)
ax.xaxis.set_ticklabels([" ","8300","1180","1000"," 9000","1050" ])
#ax.xaxis.set_ticklabels([" 8300","1180","1000","9000","1050" ])
plt.grid(False)
plt.title('postcode')




ax = plt.subplot2grid((4,3), (0,2))
#plt.hist(sales_data['region'], rwidth=0.95, bins = [0,1,2,3,4])
sales_data['region'].value_counts().plot(kind='bar', alpha=.6,color='red',fontsize=10)
ax.set_xticklabels(["F","W", "B"], rotation=0)
plt.title('region')

ax = plt.subplot2grid((4,3), (1,0))
sales_data['garden'].value_counts().plot(kind='bar', alpha=.6,color='red',fontsize=10)
ax.set_xticklabels(["No", "Yes"], rotation=0)
plt.grid(False)
plt.title('garden')

ax = plt.subplot2grid((4,3), (1,1))
#plt.bar(sales_data['furnished'], width = 0.4, height=)
sales_data['furnished'].value_counts().plot(kind='bar', alpha=.6,color='red',fontsize=10)
ax.set_xticklabels(["No","Yes"], rotation=0)
plt.grid(False)
plt.title('furnished')



ax = plt.subplot2grid((4,3), (1,2))
sales_data['building_state_agg'].value_counts().plot(kind='bar', alpha=.6,color='red',fontsize=10)
ax.set_xticklabels(["Good", "To_ren.","Ren."], rotation=0)
plt.grid(False)
plt.title('building_state')

ax = plt.subplot2grid((4,3), (2,0))
sales_data['swimming_pool_has'].value_counts().plot(kind='bar', alpha=.6,color='red',fontsize=10)
ax.set_xticklabels(["No", "Yes"], rotation=0)
plt.grid(False)
plt.title('swimming_pool_has')


ax = plt.subplot2grid((4,3), (2,1))
sales_data['equipped_kitchen_has'].value_counts().plot(kind='bar', alpha=.6,color='red',fontsize=10)
ax.set_xticklabels(["Yes","No"], rotation=0)
plt.title('equipped_kitchen_has')


ax = plt.subplot2grid((4,3), (2,2))
sales_data['terrace'].value_counts().plot(kind='bar', alpha=.6,color='red',fontsize=10)
ax.set_xticklabels(["Yes", "No"], rotation=0)
plt.grid(False)
plt.title('terrace')


ax = plt.subplot2grid((4,3), (3,0))
sales_data['open_fire'].value_counts().plot(kind='bar', alpha=.6,color='red',fontsize=10)
ax.set_xticklabels(["No","Yes"], rotation=0)
plt.grid(False)
plt.title('open_fire')


ax = plt.subplot2grid((4,3), (3,1))
sales_data['source'].value_counts().plot(kind='bar', alpha=.6,color='red',fontsize=10)
ax.set_xticklabels(["Group_6", "Group_4"], rotation=0)
plt.grid(False)
plt.title('source')


ax = plt.subplot2grid((4,3), (3,2))
property_subtype=sales_data.property_subtype.value_counts().reset_index(name='value_counting')[0:5] #select the most postcode
ax.bar(property_subtype.index, property_subtype.value_counting,alpha=.6,color='red')
labels_x=sales_data.postcode.value_counts().index[0:5]
#ax.xaxis.set_ticklabels(labels_x)
ax.xaxis.set_ticklabels([])
#plt.text(8300,1180,1000,9000,1050)
ax.xaxis.set_ticklabels([" ","Apart.","House","Villa"," Apart._block","Mixed_sub_build." ])
#ax.xaxis.set_ticklabels([" 8300","1180","1000","9000","1050" ])
plt.xticks(rotation=45)
plt.grid(False)
plt.title('postcode')

'''
fig 3
I will remove the outliers from the price, to get nice figure
'''
df_PriceHouseRegion=sales_data[['price', 'house_is', 'region']]

df_PriceHouseRegion=df_PriceHouseRegion.loc[(df_PriceHouseRegion['price'] > 2.500000e+04)]
df_PriceHouseRegion=df_PriceHouseRegion.loc[(df_PriceHouseRegion['price'] <2.195000e+06)]
df_PriceHouseRegion['price']=df_PriceHouseRegion['price'].div(1000)
print(df_PriceHouseRegion.groupby('region').price.mean())
# B    601.755459
# F    427.956031
# W    332.822316
# pdb.set_trace()
print(df_PriceHouseRegion.groupby('region').house_is.first(

))

plt.figure(3, figsize=(15,10)) #we can use either ax or plt options
# Set theme
sns.set_style('whitegrid')
# Violin plot
sns.violinplot(x='region', y='price', data=df_PriceHouseRegion, hue="house_is",  split=True)
plt.ylabel("Price in thousand")
plt.xlabel("Region")
plt.show()



plt.show()

##########################
#  Polar projection
##########################
#using projection attribute is polar
# radius = 1
# theta = np.linspace(0, 2*np.pi*radius, 1000)
#
# plt.subplot(111, projection='polar')
# plt.plot(theta, np.sin(5*theta), "g-")
# plt.plot(theta, 0.5*np.cos(20*theta), "b-")
# plt.show()















# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import re
# import pdb
#
# url = 'https://raw.githubusercontent.com/FrancescoMariottini/project3/main/inputs/all_sales_data.csv'
# sales_data=pd.read_csv(url, low_memory=False, na_values='na_identifiers',  sep=",", skipinitialspace=True)
#
# #######################
# #####  function  #############
# ########################
# def float_or_text_to_nan(x):
#     try:
#         return float(x)
#     except ValueError:
#         return np.nan
#
#
# #if the input is string, the output is string, else the output is None
# def TextInteger_to_StrNan(x):
#     try:
#         if bool(re.search(r'\d', x)) == True:
#             return (np.nan)
#         else:
#             return (str(x))
#     except TypeError:
#         return np.nan
#
# #(TRUE, True, False, FALSE, 1, 0, 3333, 'eee') to bool
# def bool_or_keep(x):
#         output = np.nan
#         try:
#             if isinstance(x, str):
#                 if (x == "1") or (x.upper() == "TRUE"):
#                     output = True
#                 elif (x == "0") or (x.upper() == "FALSE"):
#                     output = False
#             elif str(x).isnumeric():
#                 if x == 1:
#                     output = True
#                 elif x == 0:
#                     output = False
#             elif isinstance(x, bool):
#                 output = x
#             return output
#         except ValueError:
#             return np.nan
#
# def f_t(x):
#     try:
#         if (x =='True' or x=='False' or x=='FALSE' or x=='TRUE'):
#             x=x.capitalize()
#             if x=="True":
#                 return(bool(True))
#             else:
#                 return(bool(False))
#         elif (x =='1' or x=='0'):
#             if x =='1':
#                 return(bool(True))
#             else:
#                 return(bool(False))
#         else:
#             return (np.nan)
#     except ValueError:
#         return np.nan
#
# def float_or_zero(x):
#         try:
#             float(x)
#             return float(x)
#         except ValueError:
#             # keeping information of terrace if lost
#             if x == True or x == 1 or x == "True" or x == "TRUE":
#                 return 0
#             else:
#                 return np.nan
#
# def area_remove_m2(x):
#         try:
#             return int(x)
#         except ValueError:
#             numbers = [int(s) for s in str(x).split() if s.isdigit()]
#             if len(numbers) == 1:
#                 return float(numbers[0])
#             elif len(numbers) > 1:
#                 return False
#             else:
#                 return np.nan
#
# print(sales_data.shape)
# #(75876, 22)
#
# print((sales_data.columns.tolist()))
# ['source', 'hyperlink', 'locality', 'postcode', 'house_is',
#  'property_subtype', 'price', 'sale', 'rooms_number', 'area', 'kitchen_has',
#  'furnished', 'open_fire', 'terrace', 'terrace_area', 'garden', 'garden_area',
#  'land_surface', 'land_plot_surface', 'facades_number', 'swimming_pool_has', 'building_state']
#
#
#
#
#
#
# #1 OKAY, del
# print("-----------'hyperlink' ----------------")
# sales_data.drop('hyperlink', axis='columns', inplace=True)
# print("---------------------------")
#
# #2 OKAY, del
# print("-----------'land_plot_surface' ----------------")
# sales_data.drop('land_plot_surface', axis='columns', inplace=True)
# print("---------------------------")
#
# #OKAY
# #3 int,  not IN BOX PLOT
# print("----------- source ----------------")
# sales_data["source"]=sales_data["source"].astype(int)
# # print(sales_data["source"].unique())
# print("---------------------------")
#
# #OKAY
# #4 str, not IN BOX PLOT
# print("----------- locality ----------------")
# sales_data["locality"]=sales_data["locality"].astype(str)
# #print(sales_data["locality"].unique())
# print(sales_data["locality"].dtype)
# print("---------------------------")
#
#
# #OKAY
# #5 str, not IN BOX PLOT
# print("----------- postcode ----------------")
# sales_data["postcode"]=sales_data["postcode"].astype(str)
# print(sales_data["postcode"].unique())
# print(sales_data["postcode"].dtype)
# print("---------------------------")
#
# #OKAY, not IN BOX PLOT
# #6 bool, not IN BOX PLOT
# print("----------- house_is ----------------") #when the column contais mixed type or empty cell, then it is an object
# sales_data["house_is"]=sales_data["house_is"].astype(bool)
# # print(sales_data["house_is"].unique())
# print(sales_data["house_is"].dtype)
# print("---------------------------")
#
# #7, not IN BOX PLOT
# print("----------- property_subtype ----------------") #when the column contais mixed type or empty cell, then it is an object
# sales_data["property_subtype"]=sales_data["property_subtype"].apply(TextInteger_to_StrNan)
# #print(sales_data["property_subtype"].unique())
# print(sales_data["property_subtype"].dtype)
# print("---------------------------")
#
#
# #8,  not IN BOX PLOT
# print("----------- sale ----------------") #when the column contais mixed type or empty cell, then it is an object
# sales_data["sale"]=sales_data["sale"]
# # print(sales_data["sale"].unique())
# print(sales_data["sale"].dtype)
# print("---------------------------")
#
# #9 OKAY
# print("----------- rooms_number ----------------") #when the column contais mixed type or empty cell, then it is an object
# sales_data["rooms_number"]=sales_data["rooms_number"].apply(float_or_text_to_nan)
# # print(sales_data["rooms_number"].unique())
# print(sales_data["rooms_number"].dtype)
# print("---------------------------")
#
# #10,  OKAY
# print("----------- garden_area ----------------") #when the column contais mixed type or empty cell, then it is an object
# sales_data["garden_area"]=sales_data["garden_area"].apply(float_or_text_to_nan)
# # print(sales_data["garden_area"].unique())
# print(sales_data["garden_area"].dtype)
# print("---------------------------")
#
#
# #11, OKAY
# print("----------- land_surface ----------------") #when the column contais mixed type or empty cell, then it is an object
# sales_data["land_surface"]=sales_data["land_surface"].apply(float_or_text_to_nan)
# # print(sales_data["land_surface"].unique())
# print(sales_data["land_surface"].dtype)
# print("---------------------------")
#
# #12 OKAY
# print("----------- facades_number ----------------") #when the column contais mixed type or empty cell, then it is an object
# sales_data["facades_number"]=sales_data["facades_number"].apply(float_or_text_to_nan)
# # print(sales_data["facades_number"].unique())
# print(sales_data["facades_number"].dtype)
# print("---------------------------")
#
# #13  not IN BOX PLOT
# #To Do, by orhan
# print("----------- building_state ----------------") #when the column contais mixed type or empty cell, then it is an object
# sales_data["building_state"]=sales_data["building_state"]
# print(sales_data["building_state"].unique())
# print(sales_data["building_state"].dtype)
# print("---------------------------")
#
# #14, OKAY, not IN BOX PLOT
# print("----------- kitchen_has ----------------") #when the column contais mixed type or empty cell, then it is an object
# sales_data["kitchen_has"]=sales_data["kitchen_has"].apply(bool_or_keep)
# print(sales_data["kitchen_has"].unique())
# print(sales_data["kitchen_has"].dtype)
# print("---------------------------")
#
# #15,  OKAY, not IN BOX PLOT
# print("----------- furnished ----------------") #when the column contais mixed type or empty cell, then it is an object
# sales_data["furnished"]=sales_data["furnished"].apply(bool_or_keep)   #apply(bool_or_keep)
# print(sales_data["furnished"].unique())
# print(sales_data["furnished"].dtype)
# print("---------------------------")
#
#
# #16,  OKAY, not IN BOX PLOT
# print("----------- open_fire ----------------") #when the column contais mixed type or empty cell, then it is an object
# sales_data["open_fire"]=sales_data["open_fire"].apply(bool_or_keep)   #apply(bool_or_keep)
# print(sales_data["open_fire"].unique())
# print(sales_data["open_fire"].dtype)
# print("---------------------------")
#
# #17, OKAY, not IN BOX PLOT
# print("----------- terrace ----------------") #when the column contais mixed type or empty cell, then it is an object
# sales_data["terrace"]=sales_data["terrace"].apply(bool_or_keep)   #apply(bool_or_keep)
# print(sales_data["terrace"].unique())
# print(sales_data["terrace"].dtype)
# print("---------------------------")
#
# #18,  OKAY, not IN BOX PLOT
# print("----------- garden ----------------") #when the column contais mixed type or empty cell, then it is an object
# sales_data["garden"]=sales_data["garden"].apply(bool_or_keep)   #apply(bool_or_keep)
# #print(sales_data["garden"].unique())
# print(sales_data["garden"].dtype)
# print("---------------------------")
#
#
# #19,  OKAY, not IN BOX PLOT
# print("----------- swimming_pool_has ----------------") #when the column contais mixed type or empty cell, then it is an object
# sales_data["swimming_pool_has"]=sales_data["swimming_pool_has"].apply(bool_or_keep)   #apply(bool_or_keep)
# #print(sales_data["garden"].unique())
# print(sales_data["swimming_pool_has"].dtype)
# print("---------------------------")
#
# #20 OKAY
# print("----------- terrace_area ----------------") #when the column contais mixed type or empty cell, then it is an object
# sales_data["terrace_area"]=sales_data["terrace_area"].apply(float_or_zero)   #apply(bool_or_keep)
# # print(sales_data["terrace_area"].unique())
# print(sales_data["terrace_area"].dtype)
# print("---------------------------")
#
# #21 NOT OKay, I delete it, do not extract it
# #print("----------- land_plot_surface ----------------") #when the column contais mixed type or empty cell, then it is an object
# # sales_data["land_plot_surface"]=sales_data["land_plot_surface"]#.apply(float_or_text_to_nan)   #apply(bool_or_keep)
# # print(sales_data["land_plot_surface"].unique())
# # print(sales_data["land_plot_surface"].dtype)
# #print("---------------------------")
#
# #22 OKAY
# print("----------- area ----------------") #when the column contais mixed type or empty cell, then it is an object
# sales_data["area"]=sales_data["area"].apply(area_remove_m2)   #apply(bool_or_keep)
# #print(sales_data["area"].unique())
# print(sales_data["area"].dtype)
# print("---------------------------")
#
# #22 OKAY
# print("----------- Price ----------------")
# def price_correction(x):
#     try:
#         if str(x).isdigit() == True:
#             x=float(x)
#         else:
#             x=re.search(r'\d+', str(x)).group()
#         return (float(x))
#     except AttributeError:
#         return np.nan
# sales_data['price']=sales_data['price'].apply(price_correction)
# print(sales_data['price'].unique())
# # df['price']=pd.to_numeric(df['price'], errors='coerce').div(1000)
# # df['price']=df['price'].replace(0,np.nan)
#
# print(sales_data['price'].unique())
# print("---------------------------")
#
#
#
# #we have a lot of ouliers in the price
# # import seaborn as sns
# # import matplotlib.pyplot as plt
# # sns.set_theme(style="whitegrid")
# # sns.boxplot(x=df['price_k'])
# #plt.show()
#
#
# # def extract_postcodes(row):
# #     if (pd.isna(row.postcode)):
# #         legal_belgian_postcode_pattern = '[1-9][0-9][0-9][0-9]'
# #         extracted_postcodes = re.findall(legal_belgian_postcode_pattern, row.locality)
# #         if len(extracted_postcodes) > 0:
# #             row.postcode = str(int(extracted_postcodes[0]))
# #         else:
# #             row.postcode = None
# #     else:
# #         row.postcode = str(int(row.postcode))
# #     return row
# #
# #
# # sales_data =sales_data.apply(extract_postcodes, axis='columns')
# # sales_data.drop('locality', axis='columns', inplace=True)
# #
# #
# #
# #
# #
# # pdb.set_trace()
#
# sales_data_STAT=sales_data[['rooms_number', 'garden_area', 'land_surface', 'facades_number',  'terrace_area', 'area','price' ]]
# print(sales_data_STAT.shape)
# sales_data_STAT.dropna(axis=0, inplace=True)
# sales_data_STAT.drop_duplicates(subset=None, keep='first', inplace=False) #we do not have duplicated
#
# print(sales_data_STAT.shape)
#
#
# ###this is before removing outliers
# print(sales_data_STAT.describe(percentiles =[.05, .25, .75, .95]))
#
#
#
# ####################"
# ###  routlier
# #######################
# # number of rooms
# sales_data_STAT.price=sales_data_STAT.price.div(1000)
# Q1 = sales_data_STAT.quantile(0.25)
# Q3 = sales_data_STAT.quantile(0.75)
# IQR = Q3 - Q1
# print(IQR)
#
# #print(sales_data_STAT < (Q1 - 1.5 * IQR)) | (sales_data_STAT > (Q3 + 1.5 * IQR))
# sales_data_out = sales_data_STAT[~((sales_data < (Q1 - 1.5 * IQR)) |(sales_data > (Q3 + 1.5 * IQR))).any(axis=1)]
#
# print(sales_data_out.describe(percentiles =[.05, .25, .75, .95]))
# #pdb.set_trace()
# # missing_percentage_rooms_number=(sales_data_STAT['rooms_number'].isnull().sum() * 100)/sales_data_STAT.shape[0]
# # print("Percentage of missing values in rooms_number is {} %".format(int(missing_percentage_rooms_number)))
#
#
# print(sales_data_out.shape)
# # ##########################################################
# # ##############       BOX             #####################
# # ##########################################################
# # # # use box plot for the Age feature
# # #fig=plt.figure(f
# plt.figure(1, figsize=(15,10)) #we can use either ax or plt options
# plt.title("statistical analysis")
# ax = plt.subplot(331)
# ax.boxplot(sales_data_STAT['area'])
# plt.grid(True)
# ax.title.set_text("area")
#
# ax = plt.subplot(332)
# ax.boxplot(sales_data_STAT['garden_area'])
# plt.grid(True)
# plt.title("garden_area")
#
#
#
# ax = plt.subplot(333)
# ax.boxplot(sales_data_STAT['land_surface'])
# plt.grid(True)
# plt.title("garden_area")
#
# ax = plt.subplot(334)
# ax.boxplot(sales_data_STAT['terrace_area'])
# plt.grid(True)
# plt.title('terrace_area')
#
# ax = plt.subplot(335)
# ax.boxplot(sales_data_STAT['price'])
# plt.grid(True)
# plt.title('price')
#
# ax = plt.subplot(336)
# plt.hist(sales_data_STAT['rooms_number'], bins = [0,25, 50, 75, 100], rwidth=0.95)
# plt.grid(True)
# plt.title('rooms_number')
#
# ax = plt.subplot(337)
# plt.hist(sales_data_STAT['facades_number'], rwidth=0.95, bins = [1, 2, 3, 4,5,6])
# plt.grid(True)
# plt.title('facades_number')
#
# #plt.hist(data, bins = [1, 1.5, 2, 2.5, 3], rwidth=0.95)
#
#
# # ax = plt.subplot(133)
# # plt.plot(x, x**3)
# # plt.minorticks_on()
# # ax.tick_params(axis='x', which='minor', bottom='off')
# # ax.xaxis.set_ticks([-2, 0, 1, 2])
# # ax.yaxis.set_ticks(np.arange(-5, 5, 1))
# # ax.yaxis.set_ticklabels(["min", -4, -3, -2, -1, 0, 1, 2, 3, "max"])
# # plt.title("Manual ticks and tick labels\n(plus minor ticks")
# # plt.grid(True)
# plt.show()
#
# ##########################
# #  Polar projection
# ##########################
# #using projection attribute is polar
# # radius = 1
# # theta = np.linspace(0, 2*np.pi*radius, 1000)
# #
# # plt.subplot(111, projection='polar')
# # plt.plot(theta, np.sin(5*theta), "g-")
# # plt.plot(theta, 0.5*np.cos(20*theta), "b-")
# # plt.show()
#
#
