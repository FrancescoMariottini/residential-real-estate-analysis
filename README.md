# "Collecting real estate sales in Belgium" (What)
TBD
A tool to scrap real estate sales data from Belgium to obtain a valuable insight of the real estate market.

# The Mission (Why)
TBD
The real estate company "ImmoEliza" wants to create a machine learning model to make price predictions on real estate sales in Belgium. 

## Features 
The dataset holds the following information.

information|column name|variable type|example(s) or description|notes
---|---|---|---|---
Source (team)|source|int|avoid overlaps with the other groups <br> 1 : Didier - Sravanthi - Mikael <br> 2 : Abdelilah - Naomi - Manasa <br> 3 : Ankita - Adam - Selma <br> 4 : Joachim - Sara - Emre <br> 5 : Dilara - Saba - Christophe G <br> 6 : Orhan - Christophe S. - Davy <br> 7 : Philippe - Francesco - Opaps||
Hyperlink|hyperlink|str|||
Locality|locality|str|||
Postcode|postcode|int|||
Type of property (House/apartment)|house_is|bool|||
Subtype of property|property_subtype|str|Bungalow, Chalet, Mansion, ...||
Price|price|int|||
Type of sale (Exclusion of life sales)|sale|str||
Number of rooms|rooms_number|int||group 1: number of bedrooms
Area|area|int||
Fully equipped kitchen (Yes/No)|kitchen_has|bool||
Furnished (Yes/No)|furnished|bool||
Open fire (Yes/No)|open_fire|bool||
Terrace (Yes/No)|terrace|bool||
Terrace Area|terrace_area|int||
Garden (Yes/No)|garden|bool||
Garden Area|garden_area|int||
Surface of the land|land_surface|int||
Surface area of the plot of land|land_plot_surface|int||
Number of facades|facades_number|int||
Swimming pool (Yes/No)|swimming_pool_has|bool||
State of the building|building_state|str|(New, to be renovated, ...)|

Everything in a csv file.

## Highlights
TBD
- Data for all of Belgium.
- Minimum 10 000 inputs
- No empty row. If information is missing, the value is set to None.
- No duplicates. 
- Binary values replacing "Yes" or "Not" 

# Who did the project (Who):
Contributors : Joachim Kotek (JK), Francesco Mariottini (FM), Orhan Nurkan (ON), Saba Yahyaa (SY)

# Development (How)
TBD
First agreed on dataset column names and variable types.

## Take over
TBD
1. Input(s) and output(s) must be fully clarified and agreed when working independently on modules.
1. A clearer workflow, including responsibilities and deadlines, could help to make coding more effective.
1. Every team members should be able to run the used packages to allow also parallel testing
1. Previous training necessary to effectively code and support team members.

# Collecting Data (When)
- Repository: `project3`
- Type of Challenge: `data visualisation`
- Duration: `3 days * 3 people` 
- Deadline: `23/10/2020 17:00`



